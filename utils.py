from main import bot, dp
from config import admins_id

async def bot_start_notif(dp) -> None:
    '''
    Функция отправляет сообщения о запуске бота всем админам в личный чат
    '''
    for admin_id in admins_id:
        try:
            starting_text = 'Бот запущен. Мы готовы принимать заказы!'
            await bot.send_message(chat_id=admin_id, text=starting_text)
        except Exception:
            print(f'Не удалось доставить сообщение администратору с id: {admin_id}')

def get_chunked_list(list: list, chunk_size: int) -> list[list]:
    '''
    Функция разбивает список на список с подсписками нужной длины 
    и возвращает "чанкнутый список".
    '''
    sub_list = []
    chunk_list = []
    while len(list) >= chunk_size:
        for _ in range(chunk_size):
            sub_list.append(list.pop(0))
        chunk_list.append(sub_list)
        sub_list = []
    if len(list) > 0:
        chunk_list.append(list)
    return chunk_list
