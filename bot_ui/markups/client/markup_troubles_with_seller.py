from telebot import types

from bot_ui.buttons.button_main_menu import button_main_menu

markup_troubles_with_seller = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Продавец не отправляет заказ 🚫📦')
markup_troubles_with_seller.row(btn1)
btn2 = types.KeyboardButton('Продавец перенаправляет на другие сервисы 👀')
markup_troubles_with_seller.row(btn2)
markup_troubles_with_seller.row(button_main_menu)