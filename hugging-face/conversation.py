from transformers import pipeline
from transformers import Conversation

chatbot = pipeline(task="conversational",
                   model="./models/facebook/blenderbot-400M-distill")
user_message = """
What are some fun activities I can do in the winter?
"""
conversation = Conversation(user_message)
print(conversation)
conversation.add_message(
    {"role": "user",
     "content": """
What else do you recommend?
"""
     })
