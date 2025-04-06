# Add two more shape descriptions
messages = [
    {"role": "user", "content": """Here are descriptions of geometric shapes:
Shape - Triangle. Description: 3 sides, angles sum to 180°. Seen in roofs.
Shape - Square. Description: 4 equal sides, 90° angles. Found in tiles.
Shape - Circle. Description: Round, no corners. Seen in wheels.
Now describe this shape: Hexagon"""}  
]

request_body = json.dumps({"anthropic_version": "bedrock-2023-05-31","max_tokens": 100, "messages": messages})
response = bedrock.invoke_model(modelId='anthropic.claude-3-5-sonnet-20240620-v1:0', body=request_body)
response_body = json.loads(response['body'].read().decode())

print(response_body['content'][0]['text'])
