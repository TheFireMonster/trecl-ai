from deep_translator import GoogleTranslator, single_detection
import tkinter

def translate(text, lang):
    return GoogleTranslator(source='auto', target=lang).translate(text)

api_key = input("Digite sua chave de API: ")
test = True

while test:
  text_test = input("")
  if str(text_test):
    lang_test = single_detection(text_test, api_key)
    if str(lang_test):
       if text_test == str(translate("exit", lang_test)) or text_test == str(translate("sair", lang_test)):
         test = False
    print(lang_test)
  else:
    lang_test = None








user_text = input("Digite o texto a ser traduzido: ")
user_lang = input("Digite a língua alvo: ")

print(f"{translate(user_text, user_lang)}")

