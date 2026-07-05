from aiogram import F, Router, types

router = Router()

@router.message(F.text == "О боте")
async def inf(message: types.Message):
    await message.answer(
        (   "Это бот-каталог, здесь вы можете преобрести наши услуги, или связаться с нами.\n"
            "Для того, что бы заказать у нас услугу, вам нужно нажать на кнопку"
            " 'каталог' и выбрать интересующую вас услугу.\n"
            "С уважением, Station Корба.\n\n"
        )
    )
