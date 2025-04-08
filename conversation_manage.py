class ConversationManager:
    def __init__(self):
        self.bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        # Create an empty list for the conversation history
        self.conversation_history = []

    # Add the method to append messages    
    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})
