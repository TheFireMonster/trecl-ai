import tkinter as tk
from datetime import datetime

from chatterbot import ChatBot
from deep_translator import GoogleTranslator

#from config import lang_token


class Chat:

    def __init__(self):
        self.msg1 = None
        self.msg2 = None
        self.bot = ChatBot(
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


    def send(self):
        input_text = tl_text.get()
        text_input.delete(0, tk.END)
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d|%H:%M:%S')
        if "traduza" in input_text.lower():
            word_to_translate = input_text.lower().split("traduza")[1].split("para")[0].strip()
            target_language = input_text.lower().split("para")[-1].strip()
            print("Word to translate:", word_to_translate)
            print("Target language:", target_language)
            if target_language in ["japonês", "japones", "jp"]:
                response = f'A palavra {word_to_translate} em japonês é {translate(word_to_translate, "ja")}'
            elif target_language in ["inglês", "ingles", "en"]:
                response = f'A palavra {word_to_translate} em inglês é {translate(word_to_translate, "en")}'
            else:
                    response = "Não posso traduzir isso"
        else:
            response = self.bot.get_response(input_text)

        self.msg1 = tk.Message(
            frame_inner, 
            text=f"{timestamp} You:\n{input_text}", 
            width=100,
            font=app_font, 
            justify="left",
            bg="#001900", 
            fg="#009600"
        )
        
        now2 = datetime.now()
        timestamp2 = now2.strftime('%Y-%m-%d|%H:%M:%S')
        
        self.msg2 = tk.Message(
            frame_inner, 
            text=f"{timestamp2} Emerald:\n{response}",
            width=100,
            font=app_font,
            justify="left",
            bg="#001900", 
            fg="#009600"
        )
    
        self.msg1.grid(column=2, sticky='ew')
        self.msg2.grid(column=0, sticky='ew')
        frame_inner.grid_columnconfigure(1, weight=1)

        canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_resize(event):
    canvas.itemconfig(frame_window, width=event.width)

def on_enter(event):
    chat_start.send()

def update_msg_width(event):
    new_width = root.winfo_width() // 3
    if chat_start.msg1 and chat_start.msg2:
        chat_start.msg1.config(width=new_width)
        chat_start.msg2.config(width=new_width)

def translate(tl_text, lang):
    return GoogleTranslator(source='auto', target=lang).translate(tl_text)

chat_start = Chat()


root = tk.Tk()

root.geometry("800x800")
root.minsize(300, 300)

root['bg'] = "#001900"

app_font = ('Fixedsys Excelsior', 12)

#api_key = lang_token

frame_top = tk.Frame(root, bg="#001900")
frame_top.grid(row=0, column=0, columnspan=2, sticky="ew")
frame_bottom = tk.Frame(root, bg="#001900")
frame_bottom.grid(row=2, column=1, columnspan=2, sticky='ew')

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=3, rowspan=3, sticky='ns')

canvas = tk.Canvas(
    root, 
    bg="#001900", 
    bd=0, 
    highlightthickness=0, 
    yscrollcommand=scrollbar.set
)
canvas.grid(row=1, column=0, columnspan=3, sticky='nsew')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

scrollbar.config(command=canvas.yview)

frame_inner = tk.Frame(canvas, bg="#001900")
frame_window = canvas.create_window((0, 0), window=frame_inner, anchor='nw')

canvas.bind('<Configure>', on_canvas_resize)

frame_inner.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

message = tk.Label(
    frame_top, 
    text="TRECL-AI", 
    font=app_font, 
    bg="#001900", 
    fg="#009600"
)
message.pack(expand=True)
tl_text = tk.StringVar()
text_input = tk.Entry(
    frame_bottom, 
    textvariable=tl_text, 
    width=50, 
    font=app_font
)
text_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
send_button = tk.Button(
    frame_bottom, 
    text="Send", 
    font=app_font, 
    command=chat_start.send
)
send_button.pack(side=tk.RIGHT)

root.bind('<Return>', on_enter)

root.bind('<Configure>', update_msg_width)


root.mainloop() 
#while test:
#  text_test = input("")
#  if str(text_test):
#    lang_test = single_detection(tl_text.get(), api_key)
#    message_show = tk.Label(root, text=text_test)
#    message_show.pack
#  else:
#    lang_test = None

#user_text = input("Digite o texto a ser traduzido: ")
#user_lang = input("Digite a língua alvo: ")

#print(f"{translate(user_text, user_lang)}")




# if str(lang_test):
#       if text_test == str(translate("exit", lang_test)) or text_test == str(translate("sair", lang_test)):
#         test = False