import requests
import time
import asyncio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for percentile calculations

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# API keys and endpoint
OAI_API_TYPE = os.getenv("OAI_API_TYPE", "azure").lower()
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_API_ENDPOINT = os.getenv("AZURE_API_ENDPOINT") + "/openai"
API_VERSION = os.getenv("API_VERSION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")


def get_api_config():
    """
    Get the appropriate API configuration based on the OAI_API_TYPE environment variable.

    Returns:
        dict: A dictionary containing the base URL and headers for the API.
    """
    if OAI_API_TYPE == "openai":
        return {
            "base_url": OPENAI_API_BASE + "/v1",
            "headers": {"Authorization": f"Bearer {OPENAI_API_KEY}"},
        }
    else:
        return {
            "base_url": AZURE_API_ENDPOINT,
            "headers": {"api-key": AZURE_API_KEY},
        }


async def create_eval( name: str, grader_model: str, pass_threshold: float):
    """
    Create an evaluation with the given parameters.

    Args:
        pass_threshold (float): The pass threshold for the evaluation.
        grader_model (str): The grader model to use.
        name (str): The name of the evaluation.

    Returns:
        str: The ID of the created evaluation, or None if creation failed.
    """
    api_config = get_api_config()

    GRADER_PROMPT = """
        You are an evaluator that compares the "final_answer" field from a model-generated JSON response against a known ground truth answer. Use step-by-step reasoning to assign a similarity score from 1 to 5, reflecting how closely the final answer matches the expected result.

        Evaluation Criteria:
        - 5: Highly similar - The answer is logically and semantically equivalent. Minor differences in formatting, case, or rounding are allowed.
        - 4: Somewhat similar - Mostly correct but contains small inaccuracies (e.g., rounded too far, partial string mismatch, slightly off number).
        - 3: Moderately similar - The answer shows partial correctness or intent, but includes significant detail errors or incomplete logic.
        - 2: Slightly similar - Weak overlap with the correct answer. Shows some related thinking but mostly wrong.
        - 1: Not similar - The final answer is clearly incorrect or irrelevant.

        Evaluation Steps:
        1. Extract the value of "final_answer" from the model's JSON output.
        2. Normalize both the final answer and ground truth:
        - Convert to lowercase if text.
        - Strip leading/trailing whitespace.
        - If numeric, round to 2 decimal places for comparison.
        3. Compare the normalized answers for logical equivalence.
        4. Analyze whether differences (if any) impact correctness meaningfully.
        5. Decide the similarity score using the criteria above.
        6. Explain your reasoning.
        7. Return a score from 1 to 5.

        Output Format:
        Score: <1 - 5>
        Reasoning: <brief justification>

        Only respond with the score and reasoning. Focus solely on the final_answer field.
        """


    response = await asyncio.to_thread(
        requests.post,
        f'{api_config["base_url"]}/evals',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
        json={
            'name': name,
            'data_source_config': {
                "type": "custom",
                "include_sample_schema": True,
                "item_schema": {
                    "type": "object",
                    "properties": {
                        "input": {"type": "string"},
                        "solution": {"type": "string"},
                        "final_answer": {"type": "string"}
                    }
                }
            },
            'testing_criteria': [
                {
                    "name": "final_answer_string_check",
                    "type": "string_check",
                    "operation": "like",
                    "input": "{{sample.output_text}}",
                    "reference": "\"final_answer\": \"{{item.final_answer}}\""
                },
                {
                    "name": "custom grader",
                    "type": "score_model",
                    "model": grader_model,
                    "input": [
                        {
                            "type": "message",
                            "role": "developer",
                            "content": {
                                "type": "input_text",
                                "text": GRADER_PROMPT
                            }
                        },
                        {
                            "type": "message",
                            "role": "user",
                            "content": {
                                "type": "input_text",
                                "text": f"**Ground Truth**\n\n{{{{item.final_answer}}}}\n\n**JSON Response to evaluate**\n\n{{{{sample.output_text}}}}\n\n"
                            }
                        }
                    ],
                    "pass_threshold": pass_threshold,
                    "range": [0.0, 5.0]
                }

            ]
        }
    )

    if response.status_code in (200, 201):
        eval_id = response.json().get('id')
        print(f"Evaluation created successfully with ID: {eval_id}")
        return eval_id
    else:
        print(f"Failed to create evaluation. Status Code: {response.status_code}")
        print(response.text)
        return None


async def create_eval_run(eval_id, file_id, model_deployment=None, eval_run_name=None, use_sample=True):
    """
    Create an evaluation run for a specific model deployment or a custom evaluation run.

    Args:
        eval_id (str): The evaluation ID.
        file_id (str): The file ID to use for the evaluation.
        model_deployment (str, optional): The model deployment name. Required if `use_sample` is True.
        eval_run_name (str, optional): The evaluation run name. Required if `use_sample` is False.
        use_sample (bool, optional): Whether to use the sample-based evaluation. Defaults to True.

    Returns:
        None
    """
    api_config = get_api_config()

    system_prompt = (
        "You are an API that returns predictions in strict JSON format. "
        "Given a chemical structure, respond only with a JSON object using this exact format (including spaces and punctuation):\n\n"
        "{\"final_answer\": \"<final answer>\", \"solution\":  \"<solution>\"}\n\n"
        "Replace the placeholder text with your computed solution and final answer, but preserve the exact formatting — no extra text, no additional line breaks, and no variations."
    )

    # Construct the JSON payload based on the `use_sample` flag
    if use_sample:
        if not model_deployment:
            raise ValueError("`model_deployment` is required when `use_sample` is True.")
        payload = {
            "name": f"sc_{model_deployment}",
            "data_source": {
                "type": "completions",
                "source": {"type": "file_id", "id": file_id},
                "input_messages": {
                    "type": "template",
                    "template": [
                        {"type": "message", "role": "developer", "content": {"type": "input_text", "text": system_prompt}},
                        {"type": "message", "role": "user", "content": {"type": "input_text", "text": "{{item.input}}"}}
                    ]
                },
                "model": model_deployment,
                "sampling_params": {
                    "max_completions_tokens": 20000
                }
            },
        }
    else:
        if not eval_run_name:
            raise ValueError("`eval_run_name` is required when `use_sample` is False.")
        payload = {
            "name": eval_run_name,
            "data_source": {
                "type": "jsonl",
                "source": {"type": "file_id", "id": file_id}
            },
        }

    # Make the API request
    response = await asyncio.to_thread(
        requests.post,
        f'{api_config["base_url"]}/evals/{eval_id}/runs',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
        json=payload)

    # print response code and error message if any
    if response.status_code not in (200, 201):
        print(f"Failed to create evaluation run. Status Code: {response.status_code}")
        print(response.text)
        return None
    

    # Log the response status
    if use_sample:
        print(f"Create Eval Run Status for {model_deployment}: {response.status_code}")
    else:
        print(f"Create Eval Run Status for {eval_run_name}: {response.status_code}")


# Main function to handle multiple deployments
async def run_evaluations(eval_id, file_id, deployments):
    for deployment in deployments:
        await create_eval_run(eval_id, file_id, model_deployment=deployment)
    print(f"Evaluation ID: {eval_id}")


async def get_eval_runs_list(eval_id: str) -> list:
    """
    Fetch the list of evaluation runs for a given evaluation ID.

    Args:
        eval_id (str): The evaluation ID.

    Returns:
        list: A list of evaluation runs with their details.
    """
    api_config = get_api_config()
    response = await asyncio.to_thread(
        requests.get,
        f'{api_config["base_url"]}/evals/{eval_id}/runs',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
    )

    print(f"Get Evaluation Runs: {eval_id}")
    content = response.json().get('data', None)
    list_runs = []

    if content:
        for run in content:
            r = {
                'id': run.get('id', None),
                'name': run.get('name', None),
                'status': run.get('status', None),
                'model': run.get('model', None),
            }
            result = run.get('result_counts', None)
            if result:
                passed = result.get('passed', 0)
                errored = result.get('errored', 0)
                failed = result.get('failed', 0)
                total = result.get('total', 0)
                pass_percentage = (passed * 100) / (passed + failed) if (passed + failed) > 0 else 0
                error_percentage = (errored * 100) / total if total > 0 else 0
                r['pass_percentage'] = pass_percentage
                r['error_percentage'] = error_percentage

            list_runs.append(r)

    return list_runs


async def get_eval_details(eval_id: str) -> dict:
    """
    Fetch the details of a specific evaluation.

    Args:
        eval_id (str): The evaluation ID.

    Returns:
        dict: A dictionary containing evaluation details, including the name.
    """
    api_config = get_api_config()
    response = await asyncio.to_thread(
        requests.get,
        f'{api_config["base_url"]}/evals/{eval_id}',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch evaluation details for ID: {eval_id}. Status Code: {response.status_code}")
        return {"name": f"Unknown Evaluation ({eval_id})"}


async def display_evaluation_summary(eval_ids: list):
    """
    Fetch and display a summary of evaluation runs for a list of evaluation IDs, including a horizontal bar chart
    and average scores, but without score distribution visualization.

    Args:
        eval_ids (list): A list of evaluation IDs.
    """
    all_eval_runs = []
    eval_id_to_name = {}
    eval_id_to_color = {}

    # Assign unique colors for each evaluation ID
    colors = plt.cm.tab10.colors  # Use a colormap for distinct colors
    for i, eval_id in enumerate(eval_ids):
        eval_id_to_color[eval_id] = colors[i % len(colors)]

    # Fetch evaluation runs and details for each evaluation ID
    for eval_id in eval_ids:
        eval_runs = await get_eval_runs_list(eval_id)

        # Fetch evaluation details using the helper method
        eval_details = await get_eval_details(eval_id)
        eval_name = eval_details.get('name', f'Unknown Evaluation ({eval_id})')
        eval_id_to_name[eval_id] = eval_name

        # Add evaluation ID to each run for color coding
        for run in eval_runs:
            run['eval_id'] = eval_id
            all_eval_runs.append(run)

    # Combine all evaluation runs into a single DataFrame
    if all_eval_runs:
        df = pd.DataFrame(all_eval_runs)
        df = df[['id', 'name', 'model', 'status', 'pass_percentage', 'error_percentage', 'eval_id']]  # Select relevant columns
        df['eval_name'] = df['eval_id'].map(eval_id_to_name)  # Map eval_id to eval_name
        df['model'] = df['model'].str[:15]  # Truncate model names to 15 characters
        df = df.sort_values(by=['pass_percentage'], ascending=[False])  # Sort by pass_percentage descending

        print("\n" + "=" * 50)
        print("Combined Evaluation Summary")
        print("=" * 50)
        print(df.to_string(index=False, header=["Run ID", "Run Name", "Model", "Status", "Pass Percentage (%)", "Error Percentage (%)", "Evaluation ID", "Evaluation Name"]))
        print("=" * 50)

        # Dynamically adjust the figure height based on the number of rows
        num_rows = len(df)
        fig_height = max(3, num_rows * 0.5)  # Set a minimum height of 3 and scale with 0.5 per row

        # Create a horizontal bar chart with rows sorted by pass percentage across all eval_ids
        plt.figure(figsize=(12, fig_height))

        df['display_label'] = df['model'].where(
            (df['model'].str.strip() != '') & (df['model'] != 'None') & (df['model'].notna()),
            df['name']
        )
        
        plt.barh(
            df['display_label'], 
            df['pass_percentage'], 
            color=[eval_id_to_color[eval_id] for eval_id in df['eval_id']], 
            edgecolor='black'
        )
        plt.xlabel('Pass Percentage (%)')
        plt.ylabel('Model')
        plt.title("Pass Percentage by Model Across Evaluations")
        plt.xlim(0, 100)  # Set x-axis scale explicitly to 0-100
        plt.gca().invert_yaxis()  # Invert y-axis to show the highest percentage at the top
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("\n" + "=" * 50)
        print("No evaluation runs found for the provided Evaluation IDs.")
        print("=" * 50)


async def list_evaluations() -> list:
    """
    Fetch the list of all evaluations.

    Returns:
        list: A list of evaluations with their details.
    """
    api_config = get_api_config()
    response = await asyncio.to_thread(
        requests.get,
        f'{api_config["base_url"]}/evals',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
    )

    if response.status_code == 200:
        content = response.json().get('data', [])
        print("Fetched evaluations successfully.")
        return content
    else:
        print(f"Failed to fetch evaluations. Status Code: {response.status_code}")
        return []


async def delete_evaluation(eval_id: str) -> bool:
    """
    Delete an evaluation by its ID.

    Args:
        eval_id (str): The evaluation ID to delete.

    Returns:
        bool: True if the evaluation was deleted successfully, False otherwise.
    """
    api_config = get_api_config()
    response = await asyncio.to_thread(
        requests.delete,
        f'{api_config["base_url"]}/evals/{eval_id}',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
    )

    if response.status_code == 204:
        print(f"Evaluation with ID {eval_id} deleted successfully.")
        return True
    else:
        print(f"Failed to delete evaluation with ID: {eval_id}. Status Code: {response.status_code}")
        return False


async def delete_all_evaluations():
    """
    Delete all evaluations.

    Returns:
        None
    """
    # Fetch all evaluations
    evaluations = await list_evaluations()

    if not evaluations:
        print("No evaluations found to delete.")
        return

    # Iterate through each evaluation and delete it
    for evaluation in evaluations:
        eval_id = evaluation.get('id')
        if eval_id:
            success = await delete_evaluation(eval_id)
            if success:
                print(f"Deleted evaluation with ID: {eval_id}")
            else:
                print(f"Failed to delete evaluation with ID: {eval_id}")


async def get_eval_run_output_items(eval_id: str, run_id: str) -> list:
    """
    Fetch the output items for a specific evaluation run and extract the result scores.

    Args:
        eval_id (str): The evaluation ID.
        run_id (str): The run ID.

    Returns:
        list: A list of scores for the output items.
    """
    api_config = get_api_config()
    response = await asyncio.to_thread(
        requests.get,
        f'{api_config["base_url"]}/evals/{eval_id}/runs/{run_id}/output_items',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
    )

    if response.status_code == 200:
        output_items = response.json().get('data', [])
        scores = []
        for item in output_items:
            results = item.get('results', [])
            for result in results:
                score = result.get('score')
                if score is not None:
                    scores.append(score)
        return scores
    else:
        print(f"Failed to fetch output items for run {run_id}. Status Code: {response.status_code}")
        return []
    
import json

def convert_to_eval_format_separate_fields(input_path, output_path):
    converted_records = []

    with open(input_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line)
            messages = data.get("messages", [])
            
            if not messages or not isinstance(messages[0], dict):
                continue  # skip malformed

            prompt = messages[0].get("content", "").strip()
            final_answer_val = str(data.get("final_answer", ""))  # Convert to string
            solution_val = str(data.get("solution", ""))  # Convert to string

            record = {
                "item": {
                    "input": prompt,
                    "final_answer": final_answer_val,
                    "solution": solution_val
                }
            }
            converted_records.append(record)

    # Write to output file in .jsonl format
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for item in converted_records:
            outfile.write(json.dumps(item) + '\n')

    print(f"✅ Converted {len(converted_records)} records to {output_path}")

async def display_evaluation_details(eval_id: str, eval_run_id: str, status_filter: str = None, max_records: int = 10):
    """
    Display detailed information for a specific evaluation run, including sample data, scores, and status.

    Args:
        eval_id (str): The evaluation ID.
        eval_run_id (str): The evaluation run ID.
        status_filter (str, optional): Filter for "pass" or "fail" samples. Defaults to None (no filter).
        max_records (int, optional): Maximum number of records to display. Defaults to 10.
    """
    api_config = get_api_config()

    # Fetch output items for the evaluation run
    response = await asyncio.to_thread(
        requests.get,
        f'{api_config["base_url"]}/evals/{eval_id}/runs/{eval_run_id}/output_items',
        params={'api-version': API_VERSION} if OAI_API_TYPE == "azure" else None,
        headers=api_config["headers"],
    )

    if response.status_code != 200:
        print(f"Failed to fetch output items for run {eval_run_id}. Status Code: {response.status_code}")
        return

    output_items = response.json().get('data', [])
    if not output_items:
        print(f"No output items found for evaluation run {eval_run_id}.")
        return

    # Filter output items based on status (pass/fail) if specified
    if status_filter:
        output_items = [
            item for item in output_items
            if item.get('status', '').lower() == status_filter.lower()
        ]

    # Limit the number of records to display
    output_items = output_items[:max_records]

    # Display details for each sample
    print("\n" + "=" * 50)
    print(f"Evaluation Details for Run ID: {eval_run_id}")
    print("=" * 50)

    for i, item in enumerate(output_items, start=1):
        # Extract details from the item object
        datasource_item = item.get('datasource_item', {})
        input_text = datasource_item.get('input', 'N/A')
        reference_solution = datasource_item.get('solution', 'N/A')
        reference_final_answer = datasource_item.get('final_answer', 'N/A')

        # Extract final_answer and solution from the output field
        output = item.get('sample', {}).get('output', [])
        if output and isinstance(output, list):
            assistant_output = next((o.get('content', 'N/A') for o in output if o.get('role') == 'assistant'), 'N/A')
            try:
                assistant_data = json.loads(assistant_output)
                output_solution = assistant_data.get('solution', 'N/A')
                output_final_answer = assistant_data.get('final_answer', 'N/A')
            except (json.JSONDecodeError, TypeError):
                output_solution = "N/A"
                output_final_answer = "N/A"
        else:
            output_solution = "N/A"
            output_final_answer = "N/A"

        # Extract score and status
        results = item.get('results', [{}])
        score = results[0].get('score', 'N/A') if results else 'N/A'
        status = item.get('status', 'N/A')

        print(f"\nSample {i}:")
        print("-" * 50)
        # print(f"Input: {input_text}")
        # print(f"Reference Solution: {reference_solution}")
        print(f"Reference Final Answer: {reference_final_answer}")
        # print(f"Output Solution: {output_solution}")
        print(f"Output Final Answer: {output_final_answer}")
        print(f"Score: {score}")
        print(f"Status: {status}")
        print("-" * 50)

    print("\n" + "=" * 50)
    print(f"Displayed {len(output_items)} records (filtered by status: {status_filter}).")
    print("=" * 50)