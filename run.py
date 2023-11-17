from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from app.database.models import asymc_main

import asyncio
import logging
import sys


async def main():
    await asymc_main()

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')