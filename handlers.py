from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from main import dp, bot
from keybords import default_kb, category_kb
from sql import select
from utils import get_sql_keyboard


@dp.message_handler(Command('start'))
async def main_menu(message: Message) -> None:
    await message.answer(text='Hello!', reply_markup=default_kb)
    
@dp.message_handler(Text('Сделать заказ'))
async def category_menu(message: Message) -> None:
    await message.answer(text='Категории', reply_markup=category_kb)

@dp.message_handler(Text(equals=select('category', 'category_name', where=None)))
async def subcategory_menu(message: Message) -> None:
    kb = get_sql_keyboard('subcategory', 'subcategory_name', where= f'category_name = "{message.text}"')
    await message.answer(text=message.text, reply_markup=kb)

@dp.message_handler(Text(equals=select('subcategory', 'subcategory_name', where=None)))
async def product_menu(message: Message) -> None:
    kb = get_sql_keyboard('product', 'product_name', where= f'subcategory_name = "{message.text}"')
    await message.answer(text=message.text, reply_markup=kb)

@dp.message_handler(Text(equals=select('product', 'product_name', where=None)))
async def product_card(message: Message) -> None:
    f = open('./img/капучино.jpg', 'rb')
    bytes_photo = f.read()
    await bot.send_photo(chat_id=message.from_user.id, photo=bytes_photo)
