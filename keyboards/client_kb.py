from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

quiz_button = KeyboardButton("/quiz")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(quiz_button)
