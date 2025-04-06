def generate_story_with_params(bedrock, top_p, max_tokens):
    messages = [{"role": "user", 
                 "content": "Write a story about our robot writing a bestselling AI cookbook memoir."}]
    request_body=json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": max_tokens,
                 "top_p": top_p, "messages": messages})
    response = bedrock.invoke_model(body=request_body, modelId='anthropic.claude-3-5-sonnet-20240620-v1:0')
    response_body = json.loads(response.get('body').read().decode())
    return response_body["content"][0]["text"]
    
# Modify the parameters to create the two stories
short_focused = generate_story_with_params(bedrock, 0.1, 50)
long_diverse = generate_story_with_params(bedrock, 0.9, 200)

print("More focused: ", short_focused, "More creative: ", long_diverse)
