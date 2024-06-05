from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot(
    'Emerald',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sinto muito, mas eu não entendo',
            'maximum_similarity_threshold': 0.90
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
    "Me diga algo sobre a cultura japonesa",
    "Claro! Sobre o que você quer saber?",
    "Quero saber sobre uma comida típica japonesa",
    "Okay! Aqui vai uma comida típica japonesa: Sushi(寿司). O sushi é um prato típico japonês que consiste em arroz enrolado num rolinho de alga recheado com peixe cru e legumes. Acredita-se que seu surgimento aconteceu na China por volta de IV a.C. E apareceu no Japão anos depois através da Coreia. A palavra sushi tem um significado de 'arroz com vinagre'"
])

trainer.train([
    "O que é um chatbot?",
    "Um chatbot é um programa de computador que simula uma conversa humano com um usuário. Ele é capaz de responder a perguntas, fornecer informações, realizar tarefas e até mesmo interagir com o usuário."
])

trainer.train([
   "Tudo bem?",
    "Estou bem, obrigado por perguntar!"

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