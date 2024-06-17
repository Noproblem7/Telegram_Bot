from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Menyu"))

address_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard.add(KeyboardButton("1- yaqin kunlarda"))
address_keyboard.add(KeyboardButton("2- tez orada"))
address_keyboard.add(KeyboardButton("orqaga"))
