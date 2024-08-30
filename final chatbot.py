def simple_chatbot(user_input):
    user_input=user_input.lower()
    if "hello" in user_input:
       return "hello! how can I help you?"
    elif"who is you are bestfriend"in user_input:
       return"its you teju"
    elif"tell me a joke"in user_input:
       return" What does a storm cloud wear under his raincoat? Thunderwear."
    elif "how are you" in user_input:
       return "I'm chatbot, I am doing good,how can I help you"
    elif "who are you" in user_input:
       return "I am chatbot"
    elif"what is chatbot?" in user_input:
       return"A chatbot is a computer program that simulates human conversation with an end user"
    elif "bye"in user_input:
       return "goodbye! have a great day"
    else:
       return " sorry, I didn't understand that. Can you please put in other words"
def run_chatbot():
    print(" hello Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day")
            break
        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    run_chatbot()