import sqlite3

def get_sql_response(request: str) -> list[tuple]:
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.execute(request)
    data = cursor.fetchall()
    return data

