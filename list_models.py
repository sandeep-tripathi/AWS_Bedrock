# Import the boto 3 library
import boto3

# Initialize with your chosen region
bedrock = boto3.client(
    'bedrock', region_name='us-east-1'
)

# Verify the connection by printing available models
models = bedrock.list_foundation_models()

print(f"Connected successfully! Found {len(models['modelSummaries'])} available models.")
