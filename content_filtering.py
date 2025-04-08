# Define the function
def moderate_content(text, strictness_level="medium"):
    # Define the dictionary of moderation instructions
    instruction = {"high": "Strictly analyze for inappropriate content. ",
                   "medium": "Check for obviously toxic language. ",
                   "low": "Check the tone. "}

    request_body = json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 50,
                               # Add a low temperature
                               "temperature": 0.2,
                               "messages": [{"role": "user", "content": f"{instruction[strictness_level]}\n{text}"}]})
    
    response = bedrock.invoke_model(body=request_body, modelId=model_id)
    response_body = json.loads(response.get('body').read().decode())
    return response_body["content"][0]["text"]
