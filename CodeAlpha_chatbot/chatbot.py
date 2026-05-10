def chatbot():
    print("I'm ready to chat")
    while True:
        user = input("you:" ).lower()
        if user == "hello":
            print("chatbot:Hi")
        elif user == "how are you":

            print("chatbot:I'am fine,thanks")
        elif user =="bye":
            print("chatbot:Goodbye!")
            break
        else:
            print("sorry i dont understand")
chatbot() 
