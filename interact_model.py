# Initialize the client for inference
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

messages = [{"role": "user", "content": "What are some ways to track project milestones?"}]

# Format the request
request_body=json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 20,
                 "messages": messages})  

response = bedrock.invoke_model(body=request_body, modelId='anthropic.claude-3-5-sonnet-20240620-v1:0')
response_body = json.loads(response.get('body').read())

print(response_body)

# => : [{'type': 'text', 'text': 'Tracking project milestones is crucial for monitoring progress, managing expectations, and ensuring project success.'}], 'stop_reason': 'max_tokens', 'stop_sequence': None, 'usage': {'input_tokens': 18, 'output_tokens': 20}}
