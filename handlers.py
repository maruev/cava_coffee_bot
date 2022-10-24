from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from main import dp
from keybords import default_keyboard

@dp.message_handler(Command('start'))
async def main_menu(message: Message) -> None:
    await message.answer(text='Hello!', reply_markup=default_keyboard)
