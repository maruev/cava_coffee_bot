import sqlite3
import re

def select(col: str, table: str):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = f'SELECT {col} FROM {table}'
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)

if __name__ == '__main__':
    select('category_name', 'category')
