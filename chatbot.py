def chatbot_response(user_input: str) -> str:
    user_input = user_input.lower().strip()

    # Predefined rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! Welcome to CodeAlpha, How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you! Ready to help you build and automate software."
    elif "help" in user_input:
        return "I am a simple rule-based chatbot. You can say 'hello', ask 'how are you', or type 'goodbye' to exit."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day and happy coding!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello' or 'help'."

def run_chatbot():
    print("=== Welcome to CodeAlpha Chatbot ===")
    print("Chatbot: Hello! I am your CodeAlpha assistant. Type 'help' for assistance or 'goodbye' to exit.")

    while True:
        user_text = input("You: ")
        if user_text.lower().strip() in ["goodbye", "exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day and happy coding!")
            break

        response = chatbot_response(user_text)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    run_chatbot()