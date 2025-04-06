response = bedrock.invoke_model(modelId='amazon.nova-lite-v1:0', body=request_body)
data = json.loads(response['body'].read().decode())

# Check for the output key
if 'output' in data:
    # Truncate the response
    response = data['output']['message']['content'][0]['text'][:100]
    print(response)
else:
    print('Key not found')
