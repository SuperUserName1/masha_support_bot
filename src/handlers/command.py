from aiogram import Router, types
from aiogram.filters import Command

from keyboards.reply import start_reply_button

rt = Router()

@rt.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer("Привет, Маша, я твой личный помощник, можешь посмотреть в меню что я умею!", reply_markup=await start_reply_button())


@rt.message(Command("help"))
async def start_message(message: types.Message):
    await message.answer("Привет, запуталась? Я помогу! \nЭтот бот создан специально что бы помощь тебе,\nОн может показывать расписание, помогать в трудных минутах и быть дневником.\nНадеюсь он поможет тебе, Удачи!")

