from config import lang_token

from deep_translator import GoogleTranslator, single_detection

import tkinter as tk


def send():
    label = tk.Label(frame_inner, text='teste', font=app_font, bg="#001900", fg="#009600")
    label1 = tk.Label(frame_inner, text='teste', font=app_font, bg="#001900", fg="#009600")
    label.grid(column=2, sticky='ew')
    label1.grid(column=0, sticky='ew')
    frame_inner.grid_columnconfigure(1, weight=1)

    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_resize(event):
    canvas.itemconfig(frame_window, width=event.width)

#def on_enter(event):
  

def translate(tl_text, lang):
    return GoogleTranslator(source='auto', target=lang).translate(tl_text)


root = tk.Tk()

root.geometry("800x800")
root.minsize(800, 800)
#root.maxsize(800, 800)

root['bg'] = "#001900"

app_font = ('Fixedsys Excelsior', 12)

api_key = lang_token
test = True

frame_top = tk.Frame(root, bg="#001900")
frame_top.grid(row=0, column=0, columnspan=2, sticky="ew")
#frame_middle = tk.Frame(root, bg="#001900")
#frame_middle.grid(row=1, column=1, sticky='nsew') 
frame_bottom = tk.Frame(root, bg="#001900")
frame_bottom.grid(row=2, column=1, columnspan=2, sticky='ew')

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=3, rowspan=3, sticky='ns')

canvas = tk.Canvas(root, bg="red", bd=0, highlightthickness=0, yscrollcommand=scrollbar.set)
canvas.grid(row=1, column=0, columnspan=3, sticky='nsew')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

scrollbar.config(command=canvas.yview)

frame_inner = tk.Frame(canvas, bg="yellow")
frame_window = canvas.create_window((0, 0), window=frame_inner, anchor='nw')

canvas.bind('<Configure>', on_canvas_resize)

frame_inner.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)


message = tk.Label(frame_top, text="TRECL-AI", font=app_font, bg="#001900", fg="#009600")
message.pack(expand=True)
tl_text = tk.StringVar()
text_input = tk.Entry(frame_bottom, textvariable=tl_text, width=50, font=app_font)
text_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
send_button = tk.Button(frame_bottom, text="Send", font=app_font, command=send)
send_button.pack(side=tk.RIGHT)

#root.bind('<Return>', on_enter)




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