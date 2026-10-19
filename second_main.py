from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.routs import router, notifier

load_dotenv()
token = getenv('BOT_TOKEN')

dp = Dispatcher()

dp.include_router(router)

async def main():
    bot = Bot(token=token)

    asyncio.create_task(notifier(bot))

    print("Start...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())