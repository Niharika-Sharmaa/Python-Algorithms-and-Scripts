print("Chatbot: Hello! I am a Rule-Based AI Chatbot.")
print("Chatbot: You can ask me about greetings, my name, AI, help, or say bye to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Chatbot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Chatbot: I am doing well! Thanks for asking.")

    elif user_input == "what is your name" or user_input == "your name":
        print("Chatbot: I am a Rule-Based AI Chatbot.")

    elif user_input == "what is ai" or user_input == "define ai":
        print("Chatbot: AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.")

    elif user_input == "help":
        print("Chatbot: You can greet me, ask about AI, ask my name, or ask how I am.")

    elif user_input == "thank you" or user_input == "thanks":
        print("Chatbot: You're welcome!")

    elif user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")