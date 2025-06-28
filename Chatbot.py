
import re

# Define patterns and responses
responses = {
    "greeting": {
        "patterns": [r"hi", r"hello", r"hey", r"good (morning|afternoon|evening)"],
        "response": "Hello! How can I assist you today?"
    },
    "product_info": {
        "patterns": [r"tell me about (product|item)", r"what is (product|item)", r"product details"],
        "response": "Sure! Can you please specify the product you're interested in?"
    },
    "delivery": {
        "patterns": [r"delivery time", r"when.*deliver", r"shipping info", r"how long.*arrive"],
        "response": "Standard delivery takes 3-5 business days."
    },
    "return_policy": {
        "patterns": [r"return policy", r"how to return", r"can I return"],
        "response": "You can return items within 30 days of delivery. Please visit our returns page for more info."
    },
    "contact": {
        "patterns": [r"contact", r"customer support", r"talk to agent"],
        "response": "You can reach our customer support at support@example.com or call 1-800-123-4567."
    },
    "default": {
        "response": "I'm sorry, I didn't understand that. Can you rephrase your question?"
    }
}

def match_intent(user_input):
    user_input = user_input.lower()
    for intent, data in responses.items():
        for pattern in data.get("patterns", []):
            if re.search(pattern, user_input):
                return responses[intent]["response"]
    return responses["default"]["response"]

def chatbot():
    print("Customer Service Chatbot: (type 'exit' to end)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Thank you for visiting! Goodbye.")
            break
        response = match_intent(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
