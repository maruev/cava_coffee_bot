import sqlite3
from utils import format_row_sql_select


def select(table: str, col: str, where: str | None):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    if where != None:
        query = f'SELECT DISTINCT {col} FROM {table} WHERE {where}'
    else:
        query = f'SELECT DISTINCT {col} FROM {table}'
    cursor.execute(query)
    data = cursor.fetchall()
    sql_select = format_row_sql_select(data)
    return sql_select

w = 'Классика'
print(select('subcategory', 'subcategory_name', where= f'category_name = "{w}"'))

