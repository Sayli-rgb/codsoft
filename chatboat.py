print("👋 Hello! I’m Sayli’s AI Chatbot.")
print("📝 Type 'quit' anytime to end the conversation.\n")

while True:
    message = input("You: ").strip().lower()

    if message in ["hi", "hello","hii","Hii"]:
        print("Bot: Hey there! What can I do for you?")
    elif message == "how are you":
        print("Bot: I’m functioning perfectly, thanks for asking! 😊")
    elif message == "your name":
        print("Bot: I’m your virtual helper, made by Sayli!")
    elif message == "thank you":
        print("Bot: You're welcome! I'm always here to help.")
    elif message == "who made you":
        print("Bot: I was built by Sayli Ambadas Shinde during her AI internship at CodSoft.")
    elif message == "bye":
        print("Bot: Goodbye! Have a wonderful day 🌸")
        break
    elif message == "quit":
        print("Bot: Chat ended. See you soon!")
        break
    else:
        print("Bot: Sorry, I’m not sure how to respond to that.")
