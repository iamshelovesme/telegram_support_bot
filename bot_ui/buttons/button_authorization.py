import copy
import re
from telebot import types
from bot_start import bot
import mysql_handler
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_register import markup_register
from bot_ui.markups.markup_main_menu import markup_main_menu as markupMainMenu
from check_is_back import check_is_back


def init_authorization():
    @bot.message_handler(func=lambda message: message.text == "Авторизоваться")
    def try_authorization(message):
        if check_is_back(message):
            return
        bot.send_message(message.chat.id, 'Привет, сейчас Вас авторизуем! Введите Вашу почту.',
                         reply_markup=markup_register)
        bot.register_next_step_handler(message, user_email)

    def user_email(message):
        if check_is_back(message):
            return
        if message.text is None or not re.search('[^@]+@[^@]+\.[^@]+', message.text):
            bot.send_message(message.chat.id, 'Введите Вашу почту ещё раз.')
            bot.register_next_step_handler(message, user_email)
            return
        email = message.text.strip()
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE email = %s', email)
        myresult = cur.fetchone()
        temp_markup = copy.deepcopy(markupMainMenu)
        temp_markup.row(types.KeyboardButton('Зарегистрироваться 🤝'))
        temp_markup.row(types.KeyboardButton('Авторизоваться'))
        if myresult is None:
            bot.send_message(message.chat.id, 'Аккаунта с такой почтой не существует.', reply_markup=temp_markup)
            return
        bot.send_message(message.chat.id, 'Введите Ваш пароль.')
        bot.register_next_step_handler(message, user_pass, email)

    def user_pass(message, email):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', message.text):
            bot.send_message(message.chat.id, 'Введите пароль ещё раз. Минимальная длина пароля - 8 символов.'
                                              ' Пароль должен содержать числа, а также одну заглавную и '
                                              'прописную букву. Пароль НЕ должен содержать спец. символы(@,$,!,%,*,#,?,&)')
            bot.register_next_step_handler(message, user_pass, email)
            return
        password = message.text.strip()
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE pass = %s and email = %s', (password, email))
        myresult = cur.fetchone()
        temp_markup = copy.deepcopy(markupMainMenu)
        if myresult is None:
            bot.send_message(message.chat.id, 'Неправильно указана почта или пароль.', reply_markup=temp_markup)
            return
        bot.send_message(message.chat.id, 'Вы успешно авторизовались',
                         reply_markup=markup_for_registrants)
        cur.execute("UPDATE sellers SET user_id = %s WHERE email = %s", (message.from_user.id, email))
        mysql_handler.connection.commit()