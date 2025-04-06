def generate_story_with_temperature(bedrock, temperature):
    messages = [{"role": "user", 
                 "content": "Write a short story about a cooking robot teaching other robots to cook."}]
    request_body=json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 100,
                 "temperature": temperature, "messages": messages})
    response = bedrock.invoke_model(body=request_body, modelId='anthropic.claude-3-5-sonnet-20240620-v1:0')
    response_body = json.loads(response.get('body').read().decode())
    return response_body["content"][0]["text"]

# Test low and high temperature
low_temp = generate_story_with_temperature(bedrock, 0.1)
high_temp = generate_story_with_temperature(bedrock, 0.9)

print("Low temperature (more focused):", low_temp, "High temperature (more creative):", high_temp)
