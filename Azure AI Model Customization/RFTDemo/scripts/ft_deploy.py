import json
import os
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(override=True)

token= os.getenv("TOKEN") 

subscription = "856c80fd-f14e-436b-b434-fbc44a9103f7" # <DESTINATION_SUBSCRIPTION_ID>
resource_group = "omieus2" # <DESTINATION_RESOURCE_GROUP>
resource_name = "omieastus2" # <DESTINATION_RESOURCE_NAME>

source_subscription = "6a6fff00-4464-4eab-a6b1-0b533c7202e0" # <SOURCE_SUBSCRIPTION_ID>
source_resource_group = "omirg7" # <SOURCE_RESOURCE_GROUP>
source_resource = "omiswc" # <SOURCE_RESOURCE_NAME>


source = f'/subscriptions/{source_subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.CognitiveServices/accounts/{source_resource}'

# model_deployment_name = "ft-o3-mini-hydo-2" # custom deployment name that you will use to reference the model when making inference calls.
model_deployment_name = "ft-o3-mini-puzzle-300" # custom deployment name that you will use to reference the model when making inference calls.

deploy_params = {'api-version': "2025-04-01-preview"} 
deploy_headers = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}



deploy_data = {
    "sku": {"name": "standard", "capacity": 100}, 
    # "sku": {"name": "globalstandard", "capacity": 100}, 
    "properties": {
        "model": {
            "format": "OpenAI",
            # "name": "o3-mini-2025-01-31.ft-4a1fc29eed57408fb540e8111d64365c-hydrobond", # This value will look like gpt-35-turbo-0125.ft-0ab3f80e4f2242929258fff45b56a9ce 
            "name": "o3-mini-2025-01-31.ft-4ced6623d5244a1fb40c0cc3727479b0-o3mini_puzzles_300_100", # This value will look like gpt-35-turbo-0125.ft-0ab3f80e4f2242929258fff45b56a9ce 
            "version": "1",
            "source": source
        }
    }
}
deploy_data = json.dumps(deploy_data)

request_url = f'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/deployments/{model_deployment_name}'

print('Creating a new deployment...')

r = requests.put(request_url, params=deploy_params, headers=deploy_headers, data=deploy_data)

print(r)
print(r.reason)
print(r.json())