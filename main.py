from aiogram.client.session import aiohttp
from aiogram.types import InputFile

from remove_background import remove_back
from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import Command
import asyncio
dp = Dispatcher()
token = ""
bot = Bot(token)

@dp.message(Command("start"))
async def hello(message):
    kb = [
        [types.KeyboardButton(text="Отправить фотографию")],
        [types.KeyboardButton(text="Удалить фон")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(f"Привет, {message.from_user.full_name}\n",
                         reply_markup=keyboard)


@dp.message()
async def input_image(message: types.Message) -> None:
    # await message.answer("Отправляй фото, на котором хочешь удалить фон!")
    if message.document:
        pass
    elif message.photo:
        photo_obj = message.photo[-1]
        file_id = photo_obj.file_id
        file_path = await bot.get_file(file_id)
        file_name = f"photo_{file_id}.jpg"
        await bot.download_file(file_path.file_path, file_name)
        await remove_back(file_name, "done.png")
        await bot.send_photo(chat_id=message.chat.id, photo="done.png")


async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())


