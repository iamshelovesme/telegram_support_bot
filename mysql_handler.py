import pymysql
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1q2w3e4rASDF2007!',
    db='telebot',
    cursorclass=pymysql.cursors.DictCursor)
connection.cursor().execute('''CREATE TABLE IF NOT EXISTS sellers (
        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
        user_id int,
        nickname TEXT NOT NULL,
        email TEXT NOT NULL,
        pass TEXT NOT NULL)''')

