from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API



HELP_COMMAND = """
/help - Список комманд
/start - Начать работу с ботом
"""
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)  # диспетчер бота


async def on_startup(_):
    print('Бот запущен!')

# список команд что может бот
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # if message.text.count(' ') >= 1:
    await message.reply(text=HELP_COMMAND)  # ответить на сообщение пользователю

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    # if message.text.count(' ') >= 1:
    await message.reply(text="Welcome to AIOgram Bot")
    await message.delete()


# добовляем отправку стикеров
@dp.message_handler(commands=['give'])
async def start_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJQXBkgew2AWDhztB4EKUs9sQkIQy2_gAC0QEAAladvQqqhX62Km8uzC8E")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
