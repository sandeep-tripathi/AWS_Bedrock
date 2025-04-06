# Format the prompt with role and required Claude format
prompt = 'You are an AWS expert. What is Amazon Bedrock?'

request_body = json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 100, 
                           "messages": [{"role": "user", "content": prompt}]})
response = bedrock.invoke_model(modelId='anthropic.claude-3-5-sonnet-20240620-v1:0', 
                                body=request_body)

# Extract completion from response
output = json.loads(response['body'].read())['content'][0]['text'] # Parse JSON and get completion       
      
print(output)
