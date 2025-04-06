import boto3
import json

# Initialize the Bedrock Runtime client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# Set the input message for the model
message = {
    "role": "user",
    "content": [
        {"text": "Write an engaging email subject line for a coffee company’s New Year marketing campaign."}
    ]
}

# Prepare the request payload
payload = json.dumps({"messages": [message]})

# Invoke the model
nova_response = bedrock.invoke_model(modelId='amazon.nova-lite-v1:0', body=payload)

# Decode the response and extract the text
response_body = json.loads(nova_response.get("body").read().decode())
email_subject_line = response_body["output"]["message"]["content"][0]["text"]

# Print the email subject line
print("Subject:", email_subject_line)
