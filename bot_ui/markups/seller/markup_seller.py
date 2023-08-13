from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_seller = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Проблeмы с сайтом 💻')
btn2 = types.KeyboardButton('Проблемы с доставкой 📦')
markup_seller.add(btn1, btn2)
btn3 = types.KeyboardButton('Проблемы с покупателем 💬')
btn4 = types.KeyboardButton('Проблемы с обменом 🔄')
markup_seller.add(btn3, btn4)
markup_seller.add(button_main_menu)
