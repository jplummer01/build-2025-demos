import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Determine API type (Azure or OpenAI)
OAI_API_TYPE = os.getenv("OAI_API_TYPE", "azure").lower()

# Define run IDs and file IDs for OpenAI
if OAI_API_TYPE == "openai":
    RUN_IDS = {
        "eval_id_10": "eval_680dc3e37b4081908df4fa8e7805f7fd",
        "file_id_10": "file-PpJo6RXynNGMUjHpwTQ62o",
        "eval_id_500": "eval_680eae4acde481909b4b30edf3ec180a",
        "file_id_500": "file-X8piTqm2dCyX4LnwfwLJNr",
        "train_file_id_o3_1000": "file-At3eTWpTcZKEJwSXrWw3pi",
        "finetune_id_4o_o3_1000": "ftjob-1fCQfFyGGGjFfK4zGl60TSDw",
        "finetune_id_41_o3_1000": "ftjob-muVQqLofHCO5so5fLG4oQUsH",
        "finetune_id_41_mini_o3_1000": "ftjob-Voo3GW7syU2wxe8Z7UOy560x",
        "ft_model_4o_o3_1000": "ft:gpt-4o-2024-08-06:microsoft-azure-ai-engineering:o3-1000:BQsw6Nmp",
        "ft_model_41_o3_1000": "ft:gpt-4.1-2025-04-14:microsoft-azure-ai-engineering:o3-1000:BQtolTT5",
        "ft_model_41_mini_o3_1000": "ft:gpt-4.1-mini-2025-04-14:microsoft-azure-ai-engineering:o3-1000:BQsuVl7f",
        "ft_eval_id_500": "eval_680e558c989481908350f0f79f160629",
    }
else:
    # Define run IDs and file IDs for Azure
    RUN_IDS = {
        "preffered_eval_id": "eval_6815a49442a881909e15ee909a99ffe1",
        "eval_preferred_file_id": "file-e0d7a82381ea47ecb4eb4b5f90699986",
        "rejected_eval_id": "eval_6815a49557a081908fe27a0d2f1c29ba",
        "eval_rejected_file_id": "file-899c2a3169ab4139aa1d1b8f6cc36f53",
        "eval_id_500": "eval_6815c225c0b481909e9ab9d76ead26b3",
        "ft_eval_id_500": "eval_6815abc0c93c8190a80c558abd964da3",
        "file_id_500": "file-722f7c1941ca4dc4927913904cedd3f0",
        

        "eval_id_10": "eval_680dc6cf4a4081909026da1a830b7978",
        "file_id_10": "file-f1dcb487583a42cfadaeba80ae2a1ba6",
        "train_file_id_o3_1000": "file-3b5a62fe2103422e8a1e6042d06c6ff0",
        "finetune_id_4o_o3_1000": "ftjob-568e52cbc65c4b38a9bcd40df0a7129a",
        "finetune_id_4o_o3_1000_hp": "ftjob-47261bd4152649dfbd4551b162f2f0e9",
        "finetune_id_41_o3_1000": "ftjob-2854606cbf244b7895a0fe4951671952",
        "finetune_id_41_mini_o3_1000": "ftjob-19227e0aa7fa40a98977f9c07670ee97",
        "ft_model_4o_o3_1000": "ft-gpt-4o-o3-1000",
        "ft_model_4o_o3_1000_hp": "ft-gpt-4o-o3-1000-hp",
        "ft_model_41_o3_1000": "ft-gpt-41-o3-1000",
        "ft_model_41_mini_o3_1000": "ft-gpt-41-mini-o3-1000",
        "ft_eval_id_500": "eval_680e57660fb08190bc13630bba1b9ea5",
    }