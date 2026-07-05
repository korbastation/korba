from aiogram import Router, types
from aiogram.filters import Command

from keyboards.menu import main_menu_keyboard

router = Router()

@router.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\nЯ бот от Station Корба!\n",
        reply_markup=main_menu_keyboard()
    )
    