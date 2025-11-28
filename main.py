from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import WebAppInfo

BOT_TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_button = types.KeyboardButton(
        text="Открыть учебное приложение 📚",
        web_app=WebAppInfo(url="https://yalldumb.github.io/studyapp/")
    )
    keyboard.add(webapp_button)
    await message.answer("Нажми кнопку, чтобы открыть мини-приложение 👇", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
