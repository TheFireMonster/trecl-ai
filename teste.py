from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot(
    'Emerald',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
#        'chatterbot.logic.MathematicalEvaluation',
#        'chatterbot.logic.TimeLogicAdapter'
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

conversation = [
    "Can you teach me something in japanese?",
    "Do you want something simple to begin?",
    "Yes",
    "Okay let me see... Well... How about we try to learn about a japanese greeting?"
    "Okay!"
    "We could say 'おはよう'(ohayou), that means good morning in a casual way. If you want to say it politely. You can use 'おはようございます'(ohayou gozaimasu) to say it in a polite way"
    "I see, thank you!",
    "You're welcome! Anything you have mind, just ask me."

]

trainer = ListTrainer(bot)
trainer2 = ChatterBotCorpusTrainer(bot)

trainer.train(conversation)

trainer.train([
    "Can you teach me something in japanese?",
    "Do you want something simple to begin?",
    "Yes",
    "Okay let me see... Well... How about we try to learn about a japanese greeting?"
    "Okay!"
    "We could say 'こんにちは'(konnichiwa), this is how you say 'hello' during the day in a formal way in japanese"
    "I see, thank you!",
    "You're welcome! Anything you have mind, just ask me."
])

trainer.train([
    "Can you teach me something in japanese?",
    "Do you want something simple to begin?",
    "Yes",
    "Okay let me see... Well... How about we try to learn about a japanese greeting?"
    "Okay!"
    "We could say 'こんばんは'(konbanwa), this is how you say 'good evening' in japanese"
    "I see, thank you!",
    "You're welcome! Anything you have mind, just ask me."
])

trainer.train([
    "Can you teach me something in japanese?",
    "Do you want something simple to begin?",
    "Yes",
    "Okay let me see... Well... How about we try to learn about a japanese greeting?"
    "Okay!"
    "We could say 'おやすみなさい'(oyasuminasai). You can say this as a 'good night' when going to sleep."
    "That's cool, thank you!",
    "You're welcome! Anything you have mind, just ask me."
])

""" response = bot.get_response("Can you help me with something?")
print(response)

trainer2.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
) """