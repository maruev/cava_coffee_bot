import sqlite3
from utils import format_row_sql_select


def select(table: str, col: str):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = f'SELECT DISTINCT {col} FROM {table}'
    cursor.execute(query)
    data = cursor.fetchall()
    sql_select = format_row_sql_select(data)
    return sql_select


print(select('category', 'category_name'))
