import sqlite3
from utils import get_reply_keyboard

def get_sql_response(request: str) -> list[tuple]:
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.execute(request)
    data = cursor.fetchall()
    return data

prices = get_sql_response(f'''SELECT "Размер: " || product_size_name || "\n Цена: " || product_price || ".00 руб"
                                FROM price''')
kb = get_reply_keyboard(prices)
print(kb)
