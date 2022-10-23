from main import bot
from config import admins_id

async def bot_start_notif() -> None:
    for admin_id in admins_id:
        try:
            starting_text = 'Бот запущен. Мы готовы принимать заказы!'
            await bot.send_message(chat_id=admin_id, text=starting_text)
        except Exception:
            print(f'Не удалось доставить сообщение для администратора с id: {admin_id}')

