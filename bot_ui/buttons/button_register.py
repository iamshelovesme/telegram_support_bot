import re
from bot_start import bot
import mysql_handler
from bot_ui.buttons.button_main_menu import back_to_main_menu
from bot_ui.markups.markup_register import markup_register


def check_is_back(message):
    if message.text is None:
        return False
    if message.text == 'Вернуться в главное меню 🏠':
        back_to_main_menu(message)
        return True
    return False


def init_register():
    @bot.message_handler(func=lambda message: message.text == "Зарегистрироваться 🤝")
    def try_register(message):
        if check_is_back(message):
            return
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE user_id = %s', message.from_user.id)
        myresult = cur.fetchone()
        if myresult is None:
            bot.send_message(message.chat.id, 'Привет, сейчас Вас зарегистрируем! Введите Ваше настоящее имя.',
                             reply_markup=markup_register)
            bot.register_next_step_handler(message, user_name)
            return
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы, попробуйте авторизоваться.')

    def user_name(message):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^[a-zA-Zа-яА-Я]+$', message.text):
            bot.send_message(message.chat.id, 'Введите Ваше имя ещё раз.')
            bot.register_next_step_handler(message, user_name)
            return
        name = message.text.strip()
        bot.send_message(message.chat.id, 'Введите Вашу фамилию.')
        bot.register_next_step_handler(message, user_surname, name)

    def user_surname(message, name):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^[a-zA-Zа-яА-Я]+$', message.text):
            bot.send_message(message.chat.id, 'Введите Вашу фамилию ещё раз.')
            bot.register_next_step_handler(message, user_surname, name)
            return
        surname = message.text.strip()
        bot.send_message(message.chat.id, 'Введите Вашу почту.')
        bot.register_next_step_handler(message, user_email, name, surname)

    def user_email(message, name, surname):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^[\w.]+@([\w-]+.)+[\w-]{2,4}$', message.text):
            bot.send_message(message.chat.id, 'Введите Вашу почту ещё раз.')
            bot.register_next_step_handler(message, user_email, name, surname)
            return
        email = message.text.strip()
        bot.send_message(message.chat.id, 'Введите Ваш пароль.')
        bot.register_next_step_handler(message, user_pass, name, surname, email)

    def user_pass(message, name, surname, email):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', message.text):
            bot.send_message(message.chat.id, 'Введите пароль ещё раз. Минимальная длина пароля - 8 символов.'
                                              ' Пароль должен содержать числа, а также одну заглавную и '
                                              'прописную букву. Пароль НЕ должен содержать спец. символы(@,$,!,%,*,#,?,&)')
            bot.register_next_step_handler(message, user_pass, name, surname, email)
            return
        password = message.text.strip()
        cur = mysql_handler.connection.cursor()

        cur.execute("INSERT INTO telebot.sellers (name, surname, email, pass, user_id) VALUES (%s, %s, %s, %s, %s)",
                    (name, surname, email, password, message.from_user.id))
        mysql_handler.connection.commit()
        bot.send_message(message.chat.id, 'Вы успешно зарегистрированы!')
