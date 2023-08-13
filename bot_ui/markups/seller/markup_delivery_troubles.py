from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_delivery_troubles = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу отследить посылку или товар был потерян в пути ✈️')
markup_delivery_troubles.add(btn1)
markup_delivery_troubles.add(button_main_menu)