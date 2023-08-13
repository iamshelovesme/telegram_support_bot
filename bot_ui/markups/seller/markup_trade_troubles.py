from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_trade_troubles = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Товар не высвечивается в меню обмена 🚫👖')
markup_trade_troubles.add(btn1)
btn2 = types.KeyboardButton('Хочу отменить обмен 🚫🤝')
markup_trade_troubles.add(btn2)
btn3 = types.KeyboardButton('Пришло не то, что было в заказе 🙅👖')
markup_trade_troubles.add(btn3)
markup_trade_troubles.add(button_main_menu)