from responses import get_response

def chatbot():
    print("=" * 55)
    print("🤖        RULE-BASED AI CHATBOT")
    print("=" * 55)
    print("Type 'help' to see available commands.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You : ").strip().lower()

        if user_input == "exit":
            print("\nBot : Thank you for chatting. Goodbye!")
            break

        response = get_response(user_input)
        print("Bot :", response)

if __name__ == "__main__":
    chatbot()
