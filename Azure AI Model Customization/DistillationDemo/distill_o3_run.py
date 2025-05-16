from scripts.distill_utils import distill_from_teacher_model

# Define parameters
TEACHER_MODEL = "o3"  # Replace with your teacher model
INPUT_PATH = "C:\\Users\\omkarm\\src\\build_demo\\data\\train_set_1000.jsonl"  # Path to input file
OUTPUT_PATH = "C:\\Users\\omkarm\\src\\build_demo\\data\\distilled_o3_1000.jsonl"  # Path to output file

# Call the function
distill_from_teacher_model(
    teacher_model=TEACHER_MODEL,
    input_path=INPUT_PATH,
    output_path=OUTPUT_PATH,
    max_records=1000,  # Optional: Adjust the number of records
    retries=3,         # Optional: Adjust the number of retries
    retry_delay=10     # Optional: Adjust the retry delay
)

