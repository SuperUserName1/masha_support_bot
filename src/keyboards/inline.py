from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

async def self_care_video():
    builder = InlineKeyboardBuilder()
    builder.button(text="Включить таймер", callback_data="turn_on_timer")

    builder.adjust(1)

    return builder.as_markup()




