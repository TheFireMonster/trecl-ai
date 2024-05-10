from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Ron Obvious")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("How are you?")
print(response)