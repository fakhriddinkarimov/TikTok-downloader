from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from tgbot.bot.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"""Salom, {message.from_user.full_name}! 
I'm a bot for downloading tiktok videos inside telegram.
I can download video with watermark or without watermark and download audio from url.Simply send me a tiktok url."""
                        )
    