from main import bot, dp
from typing import Optional
from config import admins_id
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

async def adm_start_notif(dp) -> None:
    for admin_id in admins_id:
        try:
            starting_text = 'Бот запущен. Мы готовы принимать заказы!'
            await bot.send_message(chat_id=admin_id, text=starting_text)
        except Exception:
            print(f'Не удалось доставить сообщение администратору с id: {admin_id}')

def get_reply_keyboard(list: list[tuple], cols_num: int = 2, buttons_text_index: int = 0, optional_buttons: Optional[list[KeyboardButton]] = None, opt_buttons_cols_num: Optional[int] = None) -> ReplyKeyboardMarkup:
    buttons = _get_reply_buttons(list=list, button_text_index=buttons_text_index)
    keyboard = _get_reply_keyboard(buttons=buttons, cols_num=cols_num)
    if optional_buttons != None:
        if opt_buttons_cols_num != None:
            keyboard.keyboard.extend(_get_chunked((optional_buttons), chunk_size=opt_buttons_cols_num))
        else:
            keyboard.keyboard.append(optional_buttons)
    return keyboard

def get_inline_keyboard(list: list[tuple], cols_num: int = 3, buttons_text_index: int = 0, callback_data_index: int = 0, optional_buttons: Optional[list[InlineKeyboardButton]] = None) -> InlineKeyboardMarkup:
    buttons = _get_inline_buttons(list=list, button_text_index=buttons_text_index, callback_data_index=callback_data_index)
    if optional_buttons != None:
        buttons.extend(optional_buttons)
    keyboard = _get_inline_keyboard(buttons=buttons, cols_num=cols_num)
    return keyboard

def _get_reply_buttons(list: list[tuple], button_text_index: int = 0) -> list[KeyboardButton]:
    buttons_list = []
    for elem in list:
        button = KeyboardButton(text=elem[button_text_index])
        buttons_list.append(button)
    return buttons_list

def _get_inline_buttons(list: list[tuple], button_text_index: int = 0, callback_data_index: int = 0) -> list[InlineKeyboardButton]:
    buttons_list = []
    for elem in list:
        button = InlineKeyboardButton(text=elem[button_text_index], callback_data=elem[callback_data_index])
        buttons_list.append(button)
    return buttons_list

def _get_reply_keyboard(buttons: list[KeyboardButton], cols_num: int = 2):
    kb = ReplyKeyboardMarkup(
       keyboard=_get_chunked(buttons, cols_num), 
       resize_keyboard=True
    )
    return kb

def _get_inline_keyboard(buttons: list[InlineKeyboardButton], cols_num: int = 3):
    kb = InlineKeyboardMarkup(
    inline_keyboard=_get_chunked(buttons, cols_num), 
    )
    return kb

def _get_chunked(list: list, chunk_size: int) -> list[list]:
    sub_list = []
    new_list = list.copy()
    chunk_list = []
    while len(new_list) >= chunk_size:
        for _ in range(chunk_size):
            sub_list.append(new_list.pop(0))
        chunk_list.append(sub_list)
        sub_list = []
    if len(new_list) > 0:
        chunk_list.append(new_list)
    return chunk_list
