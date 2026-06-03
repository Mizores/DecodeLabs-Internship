
def chatbot():
    print("Chatbot: Hello! Type 'bye' to stop.")

    while True:
        user = input("You: ").lower().strip()

        if user == "bye":
            print("Chatbot: Goodbye!")
            break

        elif user == "hello":
            print("Chatbot: Hi there!")

        elif user == "how are you":
            print("Chatbot: I am fine, thank you!")
    
        elif user == "what is your name":
            print("Chatbot: My name is RuleBot.")

        elif user == "help":
            print("Chatbot: You can say hello, ask my name, or say bye.")

        else:
            print("Chatbot: Sorry, I do not understand.")

if __name__ == "__main__":    chatbot()