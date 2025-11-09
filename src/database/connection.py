import asyncpg
import asyncio


class Database():
    def __init__(self):
        self.pool = None


    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user="postgres",
            password="1342",
            database="masha_bot",
            host="localhost",
            min_size=10,
            max_size=20
        )


    async def disconnect(self):
        if self.pool:
            await self.pool.close()


    async def get_emotional(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch('select * from diary;')


    async def register_emotional(self, emotional: str, description: str):
        async with self.pool.acquire() as conn:
            return await conn.fetch('insert into diary(emotional, description) values ($1, $2)', emotional, description)


db = Database()