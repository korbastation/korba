import asyncio
from aiogram import Bot, Dispatcher

from handlers import register_routes


TOKEN = "8187462573:AAECNAI8GTd_q0KDCPTuCz9BP_kRr6h25jo"


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    register_routes(dp)

    await dp.start_polling(bot)

    

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print("Бот остановлен!")