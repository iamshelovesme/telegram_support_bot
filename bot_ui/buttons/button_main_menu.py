from telebot import types
from bot_start import bot
from bot_ui.markups.markup_main_menu import markup_main_menu

button_main_menu = types.KeyboardButton('Вернуться в главное меню 🏠')


@bot.message_handler(func=lambda message: message.text == "Вернуться в главное меню 🏠")
def back_to_main_menu(message):
    bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup_main_menu)
