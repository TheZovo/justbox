import asyncio
from aiogram import Bot, Dispatcher
from config import config
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties 
from handlers import router
from db import init_db


async def main():
    init_db()
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())