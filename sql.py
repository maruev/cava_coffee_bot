import sqlite3
from typing import Optional

def sql_select(querry: str) -> list[tuple]:
    connect = sqlite3.connect('/mnt/d/db.db')
    cursor = connect.cursor()
    cursor.execute(querry)
    data = cursor.fetchall()
    return data

def sql_insert(querry: str, values: Optional[list] = None) -> None:
    connect = sqlite3.connect('/mnt/d/db.db')
    cursor = connect.cursor()
    if values == None:
        cursor.execute(querry)
    else:
        cursor.execute(querry, values)
    cursor.close()
    connect.commit()
    connect.close()
