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

# conversation = [
#     "Can you teach me something in japanese?",
#     "Do you want something simple to begin?",
#     "Yes",
#     "Okay let me see... Well... How about we try to learn about a japanese greeting?"
#     "Okay!"
#     "We could say 'おはよう'(ohayou), that means good morning in a casual way. If you want to say it politely. You can use 'おはようございます'(ohayou gozaimasu) to say it in a polite way"
#     "I see, thank you!",
#     "You're welcome! Anything you have mind, just ask me."

# ]

trainer = ListTrainer(bot)
trainer2 = ChatterBotCorpusTrainer(bot)

# trainer.train(conversation)

trainer.train([
    "Qual o seu nome?",
    "Meu nome é Emerald ou Esmeralda em português!",
    "O que você é?",
    "Sou um chatbot criado para ajudar no aprendizado de línguas!",
    "Você gosta do que faz?",
    "Como um chatbot, eu não tenho a capacidade de gostar de algo"
   
])

trainer.train([
    "Me ensine como dizer 'Oi, como vai você?' em inglês",
    "Para dizer 'Oi, como vai você?', você pode dizer 'Hi, how are you?'",
    "Obrigado",
    "Disponha! Qualquer dúvida que você tiver, pode me perguntar!"

])

trainer.train([
    "Me ensine como dizer 'Como vai você?' em japonês",
    "Para dizer 'Como vai você?' ou 'Como você está?' em japonês, você pode dizer 'Genki?(元気?/furigana = げんき?)' de uma forma informal. Caso queira ser mais formal, você pode usar 'O genki desu ka?(お元気ですか？/furigana = おげんきですか？)",
    "Obrigado",
    "Disponha! Qualquer dúvida que você tiver, pode me perguntar! Estou aqui para ajudar!"

])



# trainer.train([
#     "Can you teach me something in japanese?",
#     "Do you want something simple to begin?",
#     "Yes",
#     "Okay let me see... Well... How about we try to learn about a japanese greeting?"
#     "Okay!"
#     "We could say 'おやすみなさい'(oyasuminasai). You can say this as a 'good night' when going to sleep."
#     "That's cool, thank you!",
#     "You're welcome! Anything you have mind, just ask me."
# ])

""" response = bot.get_response("Can you help me with something?")
print(response)

trainer2.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
) """