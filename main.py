from remove_background import remove_back
from aiogram import Dispatcher, Bot, types
import asyncio

dp = Dispatcher()


async def main():
    token = ""
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
