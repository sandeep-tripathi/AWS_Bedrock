def smart_retry(prompt, max_attempts=3):
  base_delay = 0.5
  
  for attempt in range(max_attempts):
    try:
      # Complete the API request string with the prompt
      response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 100,
                         "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}]}))
      return json.loads(response["body"].read().decode())["content"][0]["text"]
    
    except Exception as e:
      if "ThrottlingException" in str(e):
        # Implement exponential backoff
        time.sleep(base_delay * (2 ** attempt))
      else: raise e
  return "Max retries exceeded"

print(smart_retry("Tell me about podcasting."))
