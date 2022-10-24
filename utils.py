from typing import Iterable
from main import bot, dp
from config import admins_id
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def bot_start_notif(dp) -> None:
    for admin_id in admins_id:
        try:
            starting_text = 'Бот запущен. Мы готовы принимать заказы!'
            await bot.send_message(chat_id=admin_id, text=starting_text)
        except Exception:
            print(f'Не удалось доставить сообщение администратору с id: {admin_id}')


def get_buttons_list(list: list) -> list[KeyboardButton]:
    buttons_list = []
    for elem in list:
        buttons_list.append(KeyboardButton(text=str(elem)))
    return buttons_list

def get_chunked(__list: list, chunk_size: int) -> list[list]:
    sub_list = []
    chunk_list = []
    while len(__list) >= chunk_size:
        for _ in range(chunk_size):
            sub_list.append(__list.pop(0))
        chunk_list.append(sub_list)
        sub_list = []
    if len(__list) > 0:
        chunk_list.append(__list)
    return chunk_list

def get_sql_buttons(table: str, col: str, where: str | None) -> list[list[KeyboardButton]]:
    from sql import select
    sql_list = select(table=table, col=col, where=where)
    sql_buttons = get_buttons_list(sql_list)
    chunk_sql_buttons = get_chunked(sql_buttons, 2)
    return chunk_sql_buttons


def get_sql_keyboard(table: str, col: str, where: str | None) -> ReplyKeyboardMarkup:
    new_keyboard = ReplyKeyboardMarkup(
    keyboard=get_sql_buttons(table=table, col=col, where=where), resize_keyboard=True
    )
    return new_keyboard

def format_row_sql_select(sql_select):
    import re
    g = []
    for string in sql_select:
        a = re.sub('|\(|\'|\,|\)', '', str(string))
        g.append(a)
    return g
