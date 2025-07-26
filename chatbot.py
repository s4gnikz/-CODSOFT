# chatbot.py

import datetime

def get_current_time():
    return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

def get_current_date():
    return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"

def chatbot():
    # Knowledge base as a dictionary
    knowledge_base = {
        "greetings": {
            "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
            "response": "Hello! How can I assist you today?"
        },
        "goodbye": {
            "patterns": ["bye", "goodbye", "exit"],
            "response": "Goodbye! Have a great day!"
        },
        "name": {
            "patterns": ["your name", "who are you", "what's your name"],
            "response": "I'm a simple Python chatbot here to help you."
        },
        "time": {
            "patterns": ["time", "current time", "what time is it"],
            "response": get_current_time
        },
        "date": {
            "patterns": ["date", "today's date", "what date is it"],
            "response": get_current_date
        },
        "how_are_you": {
            "patterns": ["how are you", "how's it going"],
            "response": "I'm just code, but I'm running perfectly. How about you?"
        }
    }

    print("Chatbot: Hello! I'm a rule-based chatbot. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower().strip()
        matched = False

        for intent, data in knowledge_base.items():
            for pattern in data["patterns"]:
                if pattern in user_input:
                    response = data["response"]
                    if callable(response):
                        print("Chatbot:", response())
                    else:
                        print("Chatbot:", response)
                    matched = True
                    break
            if matched:
                break

        if not matched:
            print("Chatbot: I'm not sure how to respond to that.")

        if any(exit_word in user_input for exit_word in knowledge_base["goodbye"]["patterns"]):
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
