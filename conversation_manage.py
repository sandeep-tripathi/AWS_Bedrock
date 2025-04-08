class ConversationManager:
    def __init__(self):
        self.bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        # Create an empty list for the conversation history
        self.conversation_history = []

    # Add the method to append messages    
    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})


# Make conversation memory aware
conversation = ConversationManager()

user_input = "Tell me about AWS services."

# Add the user input
conversation.add_message("user", user_input)
# Send only the last two messages from conversation history
messages = conversation.conversation_history[-2:]

request_body = json.dumps({"anthropic_version": "bedrock-2023-05-31", "max_tokens": 200, "temperature": 0.2, "messages": messages})
response = conversation.bedrock.invoke_model(modelId="anthropic.claude-3-5-sonnet-20240620-v1:0", body=request_body)
completion = json.loads(response['body'].read().decode())["content"][0]["text"]

conversation.add_message("assistant", completion)
print(completion)
