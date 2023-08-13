from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_refund_troubles = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу оформить возврат товара от продавца из Китая 🚫🔄🇨🇳')
markup_refund_troubles.row(btn1)
btn2 = types.KeyboardButton('Не вернулись деньги после возврата товара от продавца из Китая 🚫💸🇨🇳')
markup_refund_troubles.row(btn2)
markup_refund_troubles.row(button_main_menu)