from aiogram import F, Router, types

from keyboards.catalog import generate_catalog_kb

router = Router()

CATALOG = {
    "Record": {"text":"Запись"},
    "Mixing": {"text":"Сведение"},
    "Beat": {"text":"Бит"},
    "Acoustic Panels": {"text":"Аккустические панели"},}

@router.message(F.text == "Каталог")
async def catalog(message: types.Message):
    await message.answer(
        "Вот мой каталог:",
        reply_markup=generate_catalog_kb(CATALOG)


    )
