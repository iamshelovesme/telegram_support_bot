from bot_start import bot
from bot_ui.markups.markup_profile import markup_profile as markupProfile


def init_button_profile():

    @bot.message_handler(func=lambda message: message.text == "Профиль")
    def back_to_main_menu(message):
        bot.send_message(message.chat.id, 'Вы перешли в меню "Профиль".', reply_markup=markupProfile)
