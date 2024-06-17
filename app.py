import logging
from db import Database
from Button import menu_keyboard, address_keyboard

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7247111795:AAE8vC54W0Cxrtw9CL5xmo1L5R22FOqkyvM"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users (username, full_name, user_id) VALUES ('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"yana bir bor salom @{full_name}", reply_markup=menu_keyboard)
    else:
        await Database.connect(query, "insert")
        await message.reply(f"salom @{full_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu")
async def menu(message: types.Message):
    await message.answer("Menular", reply_markup=address_keyboard)


@dp.message_handler(lambda message: message.text == "orqaga")
async def menu(message: types.Message):
    await message.answer("Menular", reply_markup=menu_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
