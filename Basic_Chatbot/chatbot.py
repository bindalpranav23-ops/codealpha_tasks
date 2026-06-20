# Welcome message
print("Hi! I'm a simple chatbot. Type 'bye' to exit.")

# Loop runs continuously until user types 'bye'
while True:
    # Take input and convert to lowercase for easier matching
    user_input = input("You: ").lower()
    
    # Check input against predefined options and respond accordingly
    if user_input == "hello":
        print("Bot: Hi there!")
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break  # Exit the loop and end the chatbot
    else:
        print("Bot: Sorry, I didn't understand that.")
