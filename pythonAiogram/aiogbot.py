import asyncio
import os

from aiogram import Bot, Dispatcher, types

from sqlalchemy.engine import URL
from dotenv import find_dotenv, load_dotenv
from sqlalchemy.util import await_only

load_dotenv(find_dotenv())
from db import create_async_engine, proced_schemas, get_session_maker, Base
from common.handler import handler_router
from common.usr_cmnds import private


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(handler_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
    postgres_url = "sqlite+aiosqlite:///database.db"

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)

    await proced_schemas(async_engine, BaseModel.metadata)
asyncio.run(main())