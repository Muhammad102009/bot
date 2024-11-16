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
#             await message.answer_location(latitude= 40.5215627656306,longitude= 72.79996219481133)

# @dp.message(Command("photo"))
# async def photo(message: Message):
#             await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4ii4_6NE2r_GhG6m_ZWtwwadDgOy46vp2lw&s')

# @dp.message(F.text.lower() == "привет как дела?")
# async def hello(message: Message):
#     await message.reply("У меня все отлично, а как у тебя ? 😁")

# async def main():
#     await dp.start_polling(bot)
    
# if __name__ == "__main__":
#     asyncio.run(main())
