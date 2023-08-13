from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_payment_troubles = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу привязать свою карту 🚫💳')
markup_payment_troubles.row(btn1)
btn2 = types.KeyboardButton('Не могу привязать электронный кошелёк 🚫📱')
markup_payment_troubles.row(btn2)
btn3 = types.KeyboardButton('Не вернулись деньги после отмены заказа от продавца из Китая 🚫💸🇨🇳')
markup_payment_troubles.row(btn3)
markup_payment_troubles.row(button_main_menu)