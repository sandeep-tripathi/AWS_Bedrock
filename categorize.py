def categorize_ticket(sample_ticket, categories):
    bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
    # Create prompt with allowed categories and pass in the ticket variable
    prompt = f"""Categorize this support ticket into exactly one of these categories: {', '.join(categories)}. 
    Respond with only the category name. Ticket: {sample_ticket}"""
    # Send request to Bedrock 
    response = bedrock.invoke_model(modelId='amazon.nova-lite-v1:0', 
                                    body=json.dumps({"messages": [{"role": "user", "content": [{"text": prompt}]}]}))
    # Extract the response
    return json.loads(response.get("body").read().decode())["output"]["message"]["content"][0]["text"]

result = categorize_ticket(sample_ticket, categories)
print(f"Ticket Category: {result}")
