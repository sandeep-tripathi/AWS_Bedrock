def process_with_fallback(prompt):
    # Handle errors with a try-except block
    try:
        response = bedrock.invoke_model(
          modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
          body=json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 100,
                           "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}]}))
        return json.loads(response["body"].read().decode())["content"][0]["text"]
    except ClientError:
        fallback = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0",
            body=json.dumps({"messages": [{"role": "user", "content": [{"text": prompt}]}]}))
        return json.loads(fallback["body"].read().decode())["output"]["message"]["content"][0]["text"]

print(process_with_fallback("Explain AWS Lambda"))
