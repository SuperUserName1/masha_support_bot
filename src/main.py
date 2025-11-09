import asyncio
from contextlib import asynccontextmanager

from aiogram import types, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from database.connection import db
from handlers import command, emotional, schedule, self_care, mini_games

@asynccontextmanager
async def init_db():
    try:
        await db.connect()
        print("connect")
    except Exception as e:
        print(e)

    yield

    await db.disconnect()
    print("disconnect")


async def main():
    async with init_db():
        bot = Bot(token="8246549794:AAG6qJiA9Zecd8V1LPTlaMEz8dQYcwvKSPk", default=DefaultBotProperties(parse_mode="HTML"))

        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)

        dp.include_router(command.rt)
        dp.include_router(emotional.rt)
        dp.include_router(schedule.rt)
        dp.include_router(self_care.rt)
        dp.include_router(mini_games.rt)

        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())