import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot

router = Router()

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id, "Hello everynyawn!")
                except Exception:
                    pass

        await asyncio.sleep(10)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Я помогаю с рассылкой!\n\n"
        "Команды:\n"
        "/subscribe - подписаться на уведомления\n"
        "/unsubscribe - отписаться от уведомлений\n"
        "/subscribers - список подписчиков"
    )

@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.add(user_id)
    await message.answer("Вы подписались!")

@router.message(Command("unsubscribe"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    if user_id in subscribers:
        subscribers.discard(user_id)
        await message.answer("Вы отписались")
    else:
        await message.answer("Вы не были подписаны")

@router.message(Command("subscribers"))
async def get_subscribers(message: Message):
    if not subscribers:
        await message.answer("Пока никого нет")
        return

    text = "Подписчики:\n"

    for uid in subscribers:
        text += f"{uid}\n"
    await message.answer(text)