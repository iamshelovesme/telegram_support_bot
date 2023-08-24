import smtplib

sender = "ReusedHelp@yandex.ru"
password = "halzyoltyfufdmyc"

email_server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
try:
    email_server.login(sender, password)
except Exception as _ex:
    print('Не удалось подключиться к почтовому серверу.')
