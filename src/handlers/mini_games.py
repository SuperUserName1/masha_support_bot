from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext 
from aiogram.types import InputMediaPhoto, FSInputFile

from keyboards.reply import start_reply_button, raspisanie_reply_button

rt = Router()

URL_MINI_APPS = "https://superusername1.github.io/masha_support_bot_mini_app/"

@rt.message(F.text == "Мини игры")
async def mini_games(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text=" Играыть в Pasha Кликер!!!",
                    web_app=types.WebAppInfo(url=URL_MINI_APPS)
                )
            ]
        ]
    )

    await message.answer(
        "Привет, выбери игру!!!",
        reply_markup=keyboard
    )
