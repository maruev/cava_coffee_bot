import sqlite3
from typing import Optional

def format_row_sql_select(sql_select):
    import re
    g = []
    for string in sql_select:
        a = re.sub('|\(|\'|\,|\)', '', str(string))
        g.append(a)
    return g

def select(table: str, col: str, where: Optional[str] = None):
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
