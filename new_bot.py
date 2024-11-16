# from aiogram import Bot, Dispatcher,F
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message
# import asyncio, logging
# from config import token

# bot = Bot(token=token)
# dp = Dispatcher()

# logging.basicConfig(level=logging.INFO)

# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer("Привет, как дела ?")

# @dp.message(Command("help"))
# async def help(message: Message):
#         await message.reply("Чем могу помочь ?")

# @dp.message(Command("contact"))
# async def help(message: Message):
#         await message.answer_contact(last_name="sodiq",first_name="Muhammad",phone_number="+996554005089")

# @dp.message(Command("location"))
# async def location(message: Message):
#             await message.answer_location(40.5103624795111, 72.50247177307789)

# @dp.message(Command("photo"))
# async def photo(message: Message):
#             await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4ii4_6NE2r_GhG6m_ZWtwwadDgOy46vp2lw&s')

# @dp.message(F.text.lower() == "привет как дела?")
# async def hello(message: Message):
#     await message.reply("У меня все отлично, а как у тебя ? 😁")

# @dp.message(F.text == "Backend")
# async def hello(message: Message):
#     await message.reply("Бэкэнд — серверная часть сайта, отвечающая за логику, базы данных и обработку запросов.")

# @dp.message(F.text == "Front")
# async def hello(message: Message):
#     await message.reply("Фронтенд — это интерфейс сайта, видимый пользователю, отвечает за внешний вид и взаимодействие.")

# @dp.message(F.text == "UX-UI")
# async def hello(message: Message):
#     await message.reply("UX/UI — дизайн для удобства и красоты: UX — удобство использования, UI — внешний вид.")

# @dp.message(Command("about"))
# async def location(message: Message):
#             await message.reply("МНе 15-лет я учусь по направлении Разработчик и изучаю разные языки мира")

# async def main():
#     await dp.start_polling(bot)
    
# if __name__ == "__main__":
#     asyncio.run(main())
