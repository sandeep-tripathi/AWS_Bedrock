# Import the boto 3 library
import boto3

# Initialize with your chosen region
bedrock = boto3.client(
    'bedrock', region_name='us-east-1'
)

# Verify the connection by printing available models
models = bedrock.list_foundation_models()

print(f"Connected successfully! Found {len(models['modelSummaries'])} available models.")


# Retrieve model details
response = bedrock.get_foundation_model(modelIdentifier='anthropic.claude-3-5-sonnet-20240620-v1:0')

model_info = response['modelDetails']

# Print model details
print(model_info['modelName'])
print(model_info['providerName'])
