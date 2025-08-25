import random
import datetime

# Conversation history
history = []

# Predefined responses
responses = {
    "greeting": ["Hello! 👋", "Hi there!", "Hey, how are you?"],
    "goodbye": ["Goodbye! 👋", "See you later!", "Take care!"],
    "help": ["I can help you with time, jokes, or just chat!", "Ask me about time, jokes, or weather.", "Try saying 'tell me a joke' 😄"],
    "default": ["Sorry, I don't understand that.", "Can you rephrase?", "Hmm... interesting!"],
    "jokes": [
        "Why don’t scientists trust atoms? Because they make up everything! 😂",
        "I told my computer I needed a break, and now it won’t stop sending me KitKats 🍫",
        "Why did the math book look sad? Because it had too many problems 📘"
    ],
    "weather": [
        "It looks sunny outside! ☀️",
        "Looks like it might rain today 🌧️",
        "Cloudy with a chance of Python code 🐍☁️"
    ]
}

# Simple chatbot logic
def chatbot(user_input):
    user_input = user_input.lower()
    response = ""

    if any(word in user_input for word in ["hello", "hi", "hey"]):
        response = random.choice(responses["greeting"])
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        response = random.choice(responses["goodbye"])
    elif "help" in user_input or "support" in user_input or "problem" in user_input:
        response = random.choice(responses["help"])
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {now} ⏰"
    elif "date" in user_input or "day" in user_input:
        today = datetime.date.today().strftime("%A, %B %d, %Y")
        response = f"Today is {today} 📅"
    elif "joke" in user_input:
        response = random.choice(responses["jokes"])
    elif "weather" in user_input:
        response = random.choice(responses["weather"])
    elif any(word in user_input for word in ["+","-","%"]):
        try:
            ans = eval(user_input)
            print(ans)
        except Exception as e:
            print("Error: ",e)
            print("Try to write like2 : '2+3' ")
    else:
        response = random.choice(responses["default"])

    # Save to history
    history.append({"user": user_input, "bot": response})
    return response


# Run chatbot
print("🤖 Chatbot: Hi! Type 'quit' to exit.")
while True:
    msg = input("You: ")
    if msg.lower() in ["quit", "exit"]:
        print("🤖 Chatbot: Bye! 👋")
        break
    reply = chatbot(msg)
    print("🤖 Chatbot:", reply)

# Show conversation history at the end
print("\n📜 Conversation History:")
for turn in history:
    print(f"You: {turn['user']}")
    print(f"Bot: {turn['bot']}")
