from aiogram.types import InputMediaPhoto, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

async def start_reply_button():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Расписание")
    builder.button(text="Мини игры")
    builder.button(text="Настроение")
    builder.button(text="Забота о себе")
    builder.adjust(2, 2)

    return builder.as_markup(resize_keyboard=True)


async def raspisanie_reply_button():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Понедельник")
    builder.button(text="Вторник")
    builder.button(text="Среда")
    builder.button(text="Четверг")
    builder.button(text="Пятница")
    builder.adjust(1, 3, 1)

    return builder.as_markup(resize_keyboard=True)


async def emotional_reply_button():
    emotionals = ["Я такой виселий", "Я такой печалик", "Радость", "Грусть", "Злость", "Пубертат", "Отмена", "Посмотреть свои записи"]
    
    builder = ReplyKeyboardBuilder()

    for emotional in emotionals: 
        builder.button(text=emotional)

    builder.adjust(2, 2, 2, 2)

    return builder.as_markup(resize_keyboard=True)

async def cancel_reply_button():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Отмена")
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)


async def self_care_reply_button():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Тревожность и стресс")
    builder.button(text="Низкая самооценка")
    builder.button(text="Проблема со сном")
    builder.button(text="Концентрация в работе")
    builder.button(text="Эмоциональные качели")

    builder.adjust(1, 2, 3)
    return builder.as_markup(resize_keyboard=True)