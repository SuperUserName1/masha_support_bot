from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext 

import asyncpg
import asyncio

from keyboards import reply
from keyboards.reply import start_reply_button, emotional_reply_button, cancel_reply_button
from states.state import EmotionalState
from database.connection import db

rt = Router()

@rt.message(F.text == "Настроение")
async def emotional_masha(message: types.Message, state: FSMContext):

    await message.answer("Выбери свое настроение на сегодня", reply_markup=await emotional_reply_button())

    await state.set_state(EmotionalState.emotional)


@rt.message(EmotionalState.emotional)
async def save_emotional_masha(message: types.Message, state: FSMContext):
    emotional = message.text
    
    if emotional == "Посмотреть свои записи":
        user_data = await db.get_emotional()
        i = 1
        for i in range(len(user_data)):
            await message.answer(text=f"Вот твои старые записи\n {str(user_data[i]["emotional"])}, {str(user_data[i]["description"])}", reply_markup=await start_reply_button())
        
        await state.clear()
    
    elif emotional != "Отмена":

        await state.update_data(emotional=emotional)

        emotional_data = await state.get_data()

        state_emotional = f"Привет машундра, ты чувствуешь {emotional_data['emotional']} хочешь поговорить об этом? \n можешь написать сюда все о чем думаешь"

        await message.answer(state_emotional, reply_markup=await cancel_reply_button())

        await state.set_state(EmotionalState.description)
    else:
        await message.answer(text="Возвращайся когда будешь готова", reply_markup=await start_reply_button())
        await state.clear()


@rt.message(EmotionalState.description)
async def save_description_masha(message: types.Message, state: FSMContext):
    description = message.text

    if description != "Отмена":
        await state.update_data(description=description)

        state_description= f"Спасибо, что поделилась!"

        await message.answer(state_description, reply_markup=await start_reply_button())

        user_data = await state.get_data()

        print(user_data)
        await db.register_emotional(user_data["emotional"], user_data["description"])

        await state.clear()
    else:
        await message.answer(text="Возвращайся когда будешь готова", reply_markup=await start_reply_button())
        await state.clear()

