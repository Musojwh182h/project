import asyncio
import os

from aiogram import Bot, Dispatcher, types


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

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

asyncio.run(main())