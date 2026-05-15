import time
def chatbot():
    print("I'm ready to chat")
    while True:
        user = input("you:" ).lower()
        if user == "hello":
            print("chatbot:Hi")
        elif user == "how are you":
            print("chatbot:I'am fine,thanks")
        elif "python"in user:
            print("chatbot:python is a power full language")
        elif "time"in user:
            current_time=time.ctime()
            print("bot:",current_time)
        elif user =="bye":
            print("chatbot:Goodbye!")
            break
        else:
            print("sorry i dont understand")
chatbot()
