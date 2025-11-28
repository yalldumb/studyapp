from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import WebAppInfo
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

# ---- Токен Telegram ----
BOT_TOKEN = "8560279215:AAFUL0g6bfqYYdEqf95Hi7p6iA-C5zS4ACU"

# ---- Настройка бота ----
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# ---- /start обработчик ----
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_button = types.KeyboardButton(
        text="Открыть мини-приложение PRO 📚",
        web_app=WebAppInfo(url="https://yalldumb.github.io/studuapp/?v=8")
    )
    keyboard.add(webapp_button)
    await message.answer("Нажми кнопку, чтобы открыть мини-приложение 👇", reply_markup=keyboard)

# ---- Запуск бота ----
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
