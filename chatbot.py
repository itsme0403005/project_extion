import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of pattern-response
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm just a chatbot created by you!", "You can call me Bot."]
    ],
    [
        r"how are you ?",
        ["I'm doing fine, thank you!", "Great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm just code running in your machine 😉"]
    ],
    [
        r"quit|exit",
        ["Goodbye!", "See you soon!", "Bye!"]
    ],
    [
        r"(.*)",
        ["Tell me more...", "That's interesting!", "I'm listening..."]
    ]
]

# Create Chat instance
chatbot = Chat(pairs, reflections)

# Start conversation
print("SimpleBot is ready! Type 'quit' or 'exit' to stop.")
chatbot.converse()
