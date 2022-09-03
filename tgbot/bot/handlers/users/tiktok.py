from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from downloader import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
from tgbot.bot.loader import dp

@dp.message_handler(Text(startswith='https://www.tiktok.com'))
async def test(message: types.Message):
    result = tk(message.text)
    mp = result['music']
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Download music", url="{}".format(mp))
            ]
        ]
    )
    await message.answer_audio(result['video'],reply_markup=btn)
