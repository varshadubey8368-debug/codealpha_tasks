def chatbot():
    print("Chatbot: Hi! I am a simple chatbot.")
    print("Chatbot: you can say 'hello', 'how are you', 'bye'.")
     
    while True:
        user_input = input("you:").lower()
        
        if user_input == "hello":
            print("chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
            
        elif user_input == "bye" :
            print("Chatbot : Goodbye!")
            break
        else :
            print("chatbot: Sorry, I don't understand that.") 
            
chatbot()                  