# Import required libraries
import requests
import time
import json
import asyncio

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(override=True)

# API keys and endpoint
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_API_ENDPOINT = os.getenv("AZURE_API_ENDPOINT")
API_VERSION = os.getenv("API_VERSION")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_ENDPOINT = os.getenv("OPENAI_API_BASE")

import json

def convert_rft_to_sft(input_path, output_path):
    system_prompt = (
        "You are an API that returns predictions in strict JSON format. "
        "Given a chemical structure, respond only with a JSON object using this exact format (including spaces and punctuation):\n\n"
        "{\"donors\": 0, \"acceptors\": 5}\n\n"
        "Replace the numbers with your predicted values, but preserve the exact formatting — no extra text, no line breaks, and no variations."
    )

    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            user_msg = data.get("messages", [{}])[0].get("content", "")
            ref = data.get("reference_answer", {})

            donors = ref.get("donors", 0)
            acceptors = ref.get("acceptors", 0)

            assistant_output = f'{{"donors": {donors}, "acceptors": {acceptors}}}'

            sft_record = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "content": assistant_output}
                ]
            }

            outfile.write(json.dumps(sft_record) + '\n')

    print(f"✅ Converted to SFT format and saved to {output_path}")




def save_dataset(dataset, output_path):
    """
    Saves the training dataset in JSONL format.

    Args:
        dataset: The dataset to save (e.g., training dataset).
        output_path: Path to save the JSONL file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for row in dataset:
            record = {
                "target": row['target'],
                "nums": row['nums'] 
            }
            f.write(json.dumps(record) + '\n')
    print(f"✅  dataset saved to {output_path}")


import json

def convert_to_rft_countdown_training_dataset(input_path, output_path, max_records=10):
    """
    Converts the dataset to RFT format for fine-tuning and saves it.

    Args:
        input_path: Path to the input dataset file.
        output_path: Path to save the converted dataset.
        dataset_size: Maximum number of records to process.
    """
    instruction = (
        "You are an expert in arithmetic problem solving. Given a target number and a list of numbers, "
        "your task is to combine all of the numbers exactly once using addition (+), subtraction (-), "
        "multiplication (x), or division (÷) to reach the target.\n\n"
        "- You must use every number exactly once.\n"
        "- Use parentheses as needed to control the order of operations.\n"
        "- Return only a valid JSON object with the following exact syntax:\n"
        "  {\n    \"expression\": \"...\",\n    \"result\": \"...\"\n  }\n"
        "- Both the expression and the result must be returned as strings.\n"
        "- If the exact target is not possible, return the closest valid result using all numbers.\n\n"
        "Example 1\nTarget: 812\nNumbers: [100, 75, 50, 25, 6, 3]\nOutput:\n"
        "{\n  \"expression\": \"((100 * 6) + (75 + 25) + (3 * 50))\",\n  \"result\": \"812\"\n}\n\n"
        "Example 2\nTarget: 952\nNumbers: [25, 100, 9, 3, 6, 2]\nOutput:\n"
        "{\n  \"expression\": \"((100 * 9) + (6 * 3) + (25 + 2))\",\n  \"result\": \"952\"\n}\n\n"
        "Example 3\nTarget: 301\nNumbers: [7, 50, 75, 3, 8, 2]\nOutput:\n"
        "{\n  \"expression\": \"((75 * 3) + (50 * 2) - (8 + 7))\",\n  \"result\": \"301\"\n}\n\n"
    )

    count = 0
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if count >= max_records:
                break
            data = json.loads(line)
            target = str(data.get("target", ""))
            nums = str(data.get("nums", ""))
            
            rft_record = {
                "messages": [
                    {
                        "role": "user",
                        "content": f"{instruction}Input:: \n\n Target: \"{target}\" Numbers: \"{nums}\""
                    }
                ],
                "target": f"{target}",
                "nums": f"{nums}"
            }

            outfile.write(json.dumps(rft_record) + '\n')
            count += 1

    print(f"✅ Converted {count} records to RFT format and saved to {output_path}")
