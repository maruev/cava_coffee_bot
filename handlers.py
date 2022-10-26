from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from main import dp, bot
from keyboards import default_kb, product_kb
from sql import select
from utils import get_reply_keyboard


# Хэндлер для отправки пользователю стартового меню
@dp.message_handler(Command('start'))
async def main_menu(message: Message) -> None:
    await message.answer(text='Hello!', reply_markup=default_kb)
    
# Хэндлер для отправки пользователю списка категорий товаров
@dp.message_handler(Text('Сделать заказ'))
async def category_menu(message: Message) -> None:
    categorys = select(
        table='category',
        col='category_name'
        )
    category_keyboard = get_reply_keyboard(list=categorys, cols_num=2)
    await message.answer(text='Категории', reply_markup=category_keyboard)

# Хэндлер для отправка пользователю списка подкатегорий из выбранной категории
@dp.message_handler(Text(
    equals=select('category', 'category_name', where=None))
    )
async def subcategory_menu(message: Message) -> None:
    subcategorys = select(
        table='subcategory', 
        col='subcategory_name', 
        where=f'category_name = "{message.text}"'
    )
    subcategory_keyboard = get_reply_keyboard(list=subcategorys, cols_num=2)
    await message.answer(text=message.text, reply_markup=subcategory_keyboard)

 # Хэндлер для отправки пользователю списка товаров из выбранной подкатегории
@dp.message_handler(Text(equals=select('subcategory', 'subcategory_name', where=None)))
async def product_menu(message: Message) -> None:
    products = select(
        table='product', 
        col='product_name', 
        where=f'subcategory_name = "{message.text}"'
    )
    product_keyboard = get_reply_keyboard(list=products, cols_num=2)
    await message.answer(text=message.text, reply_markup=product_keyboard)

# Хэндлер заглушка для отправки фото пользователю при нажатии на товар
@dp.message_handler(Text(equals=select('product', 'product_name', where=None)))
async def product_card(message: Message) -> None:
    f = open('./img/капучино.jpg', 'rb')
    bytes_photo = f.read()
    f.close()
    await bot.send_photo(
        chat_id=message.from_user.id, 
        photo=bytes_photo, 
        reply_markup=product_kb
    )

