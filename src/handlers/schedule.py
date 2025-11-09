from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext 
from aiogram.types import InputMediaPhoto, FSInputFile

from keyboards.reply import start_reply_button, raspisanie_reply_button

rt = Router()

@rt.message(F.text == "Расписание")
async def raspisanie(message: types.Message, state: FSMContext):

    await message.answer(text="Выбери день недели!", reply_markup=await raspisanie_reply_button())
    await state.clear()


@rt.message(F.text == "Понедельник")
async def raspisanie(message: types.Message, state: FSMContext):

    monday = FSInputFile("img/raspisanie/monday.jpg")

    await message.answer_photo(
        photo=monday, 
        caption="Расписание на понедельник",
        reply_markup=await start_reply_button())
    
    await state.clear()


@rt.message(F.text == "Вторник")
async def raspisanie(message: types.Message, state: FSMContext):
    tuesday = FSInputFile("img/raspisanie/tuesday.jpg")

    await message.answer_photo(
        photo=tuesday, 
        caption="Расписание на вторник",
        reply_markup=await start_reply_button())
 
    await state.clear()


@rt.message(F.text == "Среда")
async def raspisanie(message: types.Message, state: FSMContext):
    wednesday = FSInputFile("img/raspisanie/wednesday.jpg")

    await message.answer_photo(
        photo=wednesday, 
        caption="Расписание на среду",
        reply_markup=await start_reply_button())
 
    await state.clear()


@rt.message(F.text == "Четверг")
async def raspisanie(message: types.Message, state: FSMContext):
    thursday = FSInputFile("img/raspisanie/thursday.jpg")

    await message.answer_photo(
        photo=thursday, 
        caption="Расписание на четверг",
        reply_markup=await start_reply_button())
 
    await state.clear()


@rt.message(F.text == "Пятница")
async def raspisanie(message: types.Message, state: FSMContext):
    friday = FSInputFile("img/raspisanie/friday.jpg")

    await message.answer_photo(
        photo=friday, 
        caption="Расписание на пятницу",
        reply_markup=await start_reply_button())
 
    await state.clear()


