import re
from bot_start import bot
import mysql_handler
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_register import markup_register
from bot_ui.markups.markup_set_avatar import markup_set_avatar
from check_is_back import check_is_back


def init_register():
    @bot.message_handler(func=lambda message: message.text == "Зарегистрироваться 🤝")
    def try_register(message):
        if check_is_back(message):
            return
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE user_id = %s', message.from_user.id)
        myresult = cur.fetchone()
        if myresult is None:
            bot.send_message(message.chat.id, 'Привет, сейчас Вас зарегистрируем! Введите Ваш никнейм.',
                             reply_markup=markup_register)
            bot.register_next_step_handler(message, user_nick_name)
            return
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы, попробуйте авторизоваться.')

    def user_nick_name(message):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^[a-zA-Z]+$', message.text):
            bot.send_message(message.chat.id, 'Введите Ваш никнейм ещё раз.')
            bot.register_next_step_handler(message, user_nick_name)
            return
        nickname = message.text.strip()
        bot.send_message(message.chat.id, 'Хотите ли Вы привязать номер телефона? Позже это можно будет '
                                          'сделать, нажав на кнопку "Профиль".', reply_markup=markup_set_avatar)
        bot.register_next_step_handler(message, user_ask_number, nickname)

    def user_ask_number(message, nickname):
        if check_is_back(message):
            return
        if message.text == 'Да':
            bot.send_message(message.chat.id, 'Введите Ваш номер телефона.')
            bot.register_next_step_handler(message, user_number, nickname)
            return
        if message.text == 'Нет':
            bot.send_message(message.chat.id, 'Хотите ли Вы загрузить аватар? Позже это можно будет сделать, нажав на '
                                              'кнопку "Профиль".', reply_markup=markup_set_avatar)
            bot.register_next_step_handler(message, user_ask_avatar, nickname, None)
            return
        bot.send_message(message.chat.id, 'Нажмите одну из кнопок на клавиатуре.')
        bot.register_next_step_handler(message, user_ask_number, nickname)

    def user_number(message, nickname):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                                 message.text):
            bot.send_message(message.chat_id, 'Введите Ваш номер ещё раз.')
            bot.register_next_step_handler(message, user_number, nickname)
            return
        number = message.text.strip()
        bot.send_message(message.chat.id, 'Хотите ли Вы загрузить аватар? Позже это можно будет сделать, нажав на '
                                          'кнопку "Профиль".', reply_markup=markup_set_avatar)
        bot.register_next_step_handler(message, user_ask_avatar, nickname, number)

    def user_ask_avatar(message, nickname, number):
        if check_is_back(message):
            return
        if message.text == 'Да':
            bot.send_message(message.chat.id, 'Загрузите Ваш аватар.', reply_markup=markup_register)
            bot.register_next_step_handler(message, user_avatar, nickname, number)
            return
        if message.text == 'Нет':
            bot.send_message(message.chat.id, 'Введите Вашу почту.', reply_markup=markup_register)
            bot.register_next_step_handler(message, user_email, nickname, number, None)
            return
        bot.send_message(message.chat.id, 'Нажмите одну из кнопок на клавиатуре.')
        bot.register_next_step_handler(message, user_ask_avatar, nickname, number)

    def user_avatar(message, nickname, number):
        if check_is_back(message):
            return
        if message.json.get('photo') is None:
            bot.send_message(message.chat.id, 'Загрузите Ваш аватар ещё раз.')
            bot.register_next_step_handler(message, user_avatar, nickname, number)
            return
        avatar = message.json['photo'][len(message.json['photo']) - 1]['file_id']
        bot.send_message(message.chat.id, 'Введите Вашу почту.')
        bot.register_next_step_handler(message, user_email, nickname, number, avatar)

    def user_email(message, nickname, number, avatar):
        if check_is_back(message):
            return
        if message.text is None or not re.search('[^@]+@[^@]+\.[^@]+', message.text):
            bot.send_message(message.chat.id, 'Введите Вашу почту ещё раз.')
            bot.register_next_step_handler(message, user_email, nickname, number, avatar)
            return
        email = message.text.strip()
        bot.send_message(message.chat.id, 'Введите Ваш пароль.')
        bot.register_next_step_handler(message, user_pass, nickname, number, avatar, email)

    def user_pass(message, nickname, number, avatar, email):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', message.text):
            bot.send_message(message.chat.id, 'Введите пароль ещё раз. Минимальная длина пароля - 8 символов.'
                                              ' Пароль должен содержать числа, а также одну заглавную и '
                                              'прописную букву. Пароль НЕ должен содержать спец. символы(@,$,!,%,*,#,'
                                              '?,&)')
            bot.register_next_step_handler(message, user_pass, nickname, number, avatar, email)
            return
        password = message.text.strip()

        cur = mysql_handler.connection.cursor()
        cur.execute("INSERT INTO telebot.sellers (nickname, number, email, pass, user_id) VALUES (%s, %s, %s, %s, %s)",
                    (nickname, None, email, password, message.from_user.id))

        sql_id = cur.execute("SELECT id FROM sellers WHERE user_id = %s", message.from_user.id)
        if avatar is not None:
            file = bot.get_file(avatar)
            downloaded_file = bot.download_file(file.file_path)
            with open('user_data/avatars/{}.jpg'.format(sql_id), 'wb') as new_file:
                new_file.write(downloaded_file)
        if number is not None:
            cur = mysql_handler.connection.cursor()
            cur.execute('UPDATE sellers SET number = %s WHERE user_id = %s', (number, message.from_user.id))

        mysql_handler.connection.commit()
        bot.send_message(message.chat.id, 'Вы успешно зарегистрированы!', reply_markup=markup_for_registrants)
