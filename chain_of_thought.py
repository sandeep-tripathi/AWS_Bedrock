def generate_message_content(text_data):
    steps = [
        "1. Understand the target audience",
        "2. Outline key points",
        "3. Draft a promotional email"
    ]
    # Append the steps to the prompt text
    text_data["text"] += "\nSteps: " + ' '.join(steps)
    return text_data

text_data = {"text": "Create a promotional email for a new cloud platform."}
  
print(generate_message_content(text_data))
