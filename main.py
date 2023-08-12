import re

import telebot
import time
import mysql_handler
from markups.client.markup_client import markup as markupClient
from markups.seller.markup_seller import markup as markupSeller
from markups.markup_main_menu import markup as markupMainMenu
from markups.client.markup_payment_troubles import markup as markupPaymentTroubles
from markups.client.markup_refund_troubles import markup as markupRefundTroubles
from markups.client.markup_troubles_with_seller import markup as markupTroublesWithSeller
from markups.seller.markup_site_troubles import markup as markupSiteTroubles
from markups.seller.markup_delivery_troubles import markup as markupDeliveryTroubles
from markups.seller.markup_troubles_with_client import markup as markupTroublesWithClient
from markups.seller.markup_trade_troubles import markup as markupTradeTroubles
from utility import read_text_message

bot = telebot.TeleBot("6411391507:AAF2hHIKF11BGDvubaZ0OwMBncpZX2tQLBU")
owner_chat_id = "1098631749"
user_last_message = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я телеграм-бот техподдержки reused team. В '
                                      'интерактивном меню снизу выбери кто ты, чтобы я помог '
                                      'решить твою проблему.', reply_markup=markupMainMenu)


@bot.message_handler(func=lambda message: message.text == "Связаться с поддержкой ☎️")
def forward_messages(message):
    current_time = int(time.time())
    user_id = message.from_user.id
    if user_id in user_last_message and current_time - user_last_message[user_id]['timestamp'] < 24 * 60 * 60:
        bot.send_message(message.chat.id, 'Вы уже отправили сообщение в течение последних 24 часов.')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, введите сообщение, которое вы хотите отправить')
        bot.register_next_step_handler(message, send_message_to_owner)


@bot.message_handler(func=lambda message: message.text == "Вернуться в главное меню 🏠")
def back_to_main_menu(message):
    bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markupMainMenu)


@bot.message_handler(func=lambda message: message.text == "Клиент 🧑‍💼")
def client_menu(message):
    bot.send_message(message.chat.id, 'Выберите свою проблему', reply_markup=markupClient)


@bot.message_handler(func=lambda message: message.text == "Проблема с возвратом 📦")
def refund_troubles(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupRefundTroubles)


@bot.message_handler(func=lambda message: message.text == "Проблема с оплатой 💳")
def payment_troubles(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupPaymentTroubles)


@bot.message_handler(func=lambda message: message.text == "Проблема с продавцом 💬")
def troubles_with_seller(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupTroublesWithSeller)


@bot.message_handler(
    func=lambda message: message.text == "Не могу оформить возврат товара от продавца из Китая 🚫🔄🇨🇳")
def china_refund_troubles(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Не могу оформить возврат '
                                                        'товара от продавца из Китая.txt'))


@bot.message_handler(func=lambda message: message.text == "Не вернулись деньги после возврата "
                                                          "товара от продавца из Китая 🚫💸🇨🇳")
def china_payment_troubles(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Не вернулись деньги после '
                                                        'возврата товара от продавца из Китая.txt'))


@bot.message_handler(func=lambda message: message.text == "Не могу привязать свою карту 🚫💳")
def client_credit_card_troubles(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Не могу привязать свою карту.txt'))


@bot.message_handler(func=lambda message: message.text == "Не могу привязать электронный кошелёк 🚫📱")
def client_wallet_troubles(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Не могу привязать электронный '
                                                        'кошелёк.txt'))


@bot.message_handler(func=lambda message: message.text == "Не вернулись деньги после отмены заказа от продавца "
                                                          "из Китая 🚫💸🇨🇳")
def china_refund_and_payment_troubles(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Не вернулись деньги после отмены '
                                                        'заказа от продавца из Китая.txt'))


@bot.message_handler(func=lambda message: message.text == "Продавец не отправляет заказ 🚫📦")
def delivery_troubles(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Продавец не отправляет заказ.txt'))


@bot.message_handler(func=lambda message: message.text == "Продавец перенаправляет на другие сервисы 👀")
def suspicious_seller(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Продавец перенаправляет на другие '
                                                        'сервисы.txt'))


@bot.message_handler(func=lambda message: message.text == "Продавец 👨‍💼")
def seller_menu(message):
    bot.send_message(message.chat.id, 'Выберите свою проблему', reply_markup=markupSeller)


@bot.message_handler(func=lambda message: message.text == "Проблeмы с сайтом 💻")
def site_troubles(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupSiteTroubles)


@bot.message_handler(func=lambda message: message.text == "Проблемы с доставкой 📦")
def delivery_troubles(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupDeliveryTroubles)


@bot.message_handler(func=lambda message: message.text == "Проблемы с обменом 🔄")
def trade_troubles(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupTradeTroubles)


@bot.message_handler(func=lambda message: message.text == "Проблемы с покупателем 💬")
def troubles_with_client(message):
    bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupTroublesWithClient)


@bot.message_handler(func=lambda message: message.text == "Не могу выложить объявление 🚫")
def troubles_with_announcement(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Не могу выложить объявление.txt'))


@bot.message_handler(func=lambda message: message.text == "Не была выдана табличка оригинальности ✅")
def troubles_with_legit_check(message):
    bot.send_message(message.chat.id, read_text_message(
        'txt_files/seller_troubles/Не была выдана табличка оригинальности.txt'))


@bot.message_handler(func=lambda message: message.text == "Не могу отследить посылку или товар был потерян в пути ✈️")
def troubles_with_package(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Не могу отследить посылку или '
                                                        'товар был потерян в пути.txt'))


@bot.message_handler(func=lambda message: message.text == "Покупатель испортил товар 🤜👖")
def client_ruined_clothes(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Покупатель испортил товар.txt'))


@bot.message_handler(func=lambda message: message.text == "Покупатель перенаправляет на сторонние сервисы 👀")
def suspicious_client(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Покупатель перенаправляет '
                                                        'на сторонние сервисы.txt'))


@bot.message_handler(func=lambda message: message.text == "Товар не высвечивается в меню обмена 🚫👖")
def troubles_with_site(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Товар не высвечивается в меню '
                                                        'обмена.txt'))


@bot.message_handler(func=lambda message: message.text == "Хочу отменить обмен 🚫🤝")
def canceled_trade(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Хочу отменить обмен.txt'))


@bot.message_handler(func=lambda message: message.text == "Пришло не то, что было в заказе 🙅👖")
def wrong_clothes(message):
    bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Пришло не то,'
                                                        ' что было в заказе.txt'))


@bot.message_handler(func=lambda message: message.text == "Зарегистрироваться 🤝")
def try_register(message):
    cur = mysql_handler.connection.cursor()
    cur.execute('SELECT * FROM sellers WHERE user_id = %s', message.from_user.id)
    myresult = cur.fetchone()
    if myresult is None:
        bot.send_message(message.chat.id, 'Привет, сейчас Вас зарегистрируем! Введите ваше настоящее имя.')
        bot.register_next_step_handler(message, user_name)
        return
    bot.send_message(message.chat.id, 'Вы уже зарегистрированы.')


def user_name(message):
    if message.text is None or not re.search('^[a-zA-Zа-яА-Я]+$', message.text):
        bot.send_message(message.chat.id, 'Введите имя ещё раз')
        bot.register_next_step_handler(message, user_name)
        return
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите вашу фамилию')
    bot.register_next_step_handler(message, user_surname, name)


def user_surname(message, name):
    if message.text is None or not re.search('^[a-zA-Zа-яА-Я]+$', message.text):
        bot.send_message(message.chat.id, 'Введите вашу фамилию ещё раз')
        bot.register_next_step_handler(message, user_surname, name)
        return
    surname = message.text.strip()
    bot.send_message(message.chat.id, 'Введите вашу почту')
    bot.register_next_step_handler(message, user_email, name, surname)


def user_email(message, name, surname):
    if message.text is None or not re.search('^[\w.]+@([\w-]+.)+[\w-]{2,4}$', message.text):
        bot.send_message(message.chat.id, 'Введите почту ещё раз')
        bot.register_next_step_handler(message, user_email, name, surname)
        return
    email = message.text.strip()
    bot.send_message(message.chat.id, 'Введите ваш пароль')
    bot.register_next_step_handler(message, user_pass, name, surname, email)


def user_pass(message, name, surname, email):
    if message.text is None:
        bot.send_message(message.chat.id, 'Введите пароль ещё раз')
        bot.register_next_step_handler(message, user_pass, name, surname, email)
        return
    password = message.text.strip()
    cur = mysql_handler.connection.cursor()

    cur.execute("INSERT INTO telebot.sellers (name, surname, email, pass, user_id) VALUES (%s, %s, %s, %s, %s)",
                (name, surname, email, password, message.from_user.id))
    mysql_handler.connection.commit()
    bot.send_message(message.chat.id, 'Вы успешно зарегистрированы!')


def send_message_to_owner(message):
    user_id = message.from_user.id
    msg = (f'Ссылка на телеграм аккаунт пользователя: t.me/{message.from_user.username}\n\nСообщение '
           f'от пользователя {message.from_user.id}:\n\n{message.text}')
    bot.send_message(owner_chat_id, msg)
    bot.send_message(message.chat.id, 'Ваше сообщение успешно отправлено владельцу бота.')
    user_last_message[user_id] = {'timestamp': int(time.time())}


print('Бот запустился')

bot.infinity_polling()
