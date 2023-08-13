from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_troubles_with_client = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Покупатель испортил товар 🤜👖')
markup_troubles_with_client.add(btn1)
btn2 = types.KeyboardButton('Покупатель перенаправляет на сторонние сервисы 👀')
markup_troubles_with_client.add(btn2)
markup_troubles_with_client.add(button_main_menu)