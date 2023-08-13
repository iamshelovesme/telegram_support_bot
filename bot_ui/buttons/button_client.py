from bot_start import bot
from utility import read_text_message
from bot_ui.markups.client.markup_client import markup_client as markupClient
from bot_ui.markups.client.markup_refund_troubles import markup_refund_troubles as markupRefundTroubles
from bot_ui.markups.client.markup_payment_troubles import markup_payment_troubles as markupPaymentTroubles
from bot_ui.markups.client.markup_troubles_with_seller import markup_troubles_with_seller as markupTroublesWithSeller


def init_button_client():
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
        bot.send_message(message.chat.id,
                         read_text_message('txt_files/client_troubles/Не могу привязать свою карту.txt'))

    @bot.message_handler(func=lambda message: message.text == "Не могу привязать электронный кошелёк 🚫📱")
    def client_wallet_troubles(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/client_troubles/Не могу привязать электронный '
                                                            'кошелёк.txt'))

    @bot.message_handler(func=lambda message: message.text == "Не вернулись деньги после отмены заказа от продавца "
                                                              "из Китая 🚫💸🇨🇳")
    def china_refund_and_payment_troubles(message):
        bot.send_message(message.chat.id,
                         read_text_message('txt_files/client_troubles/Не вернулись деньги после отмены '
                                           'заказа от продавца из Китая.txt'))

    @bot.message_handler(func=lambda message: message.text == "Продавец не отправляет заказ 🚫📦")
    def delivery_troubles(message):
        bot.send_message(message.chat.id,
                         read_text_message('txt_files/client_troubles/Продавец не отправляет заказ.txt'))

    @bot.message_handler(func=lambda message: message.text == "Продавец перенаправляет на другие сервисы 👀")
    def suspicious_seller(message):
        bot.send_message(message.chat.id,
                         read_text_message('txt_files/client_troubles/Продавец перенаправляет на другие '
                                           'сервисы.txt'))
