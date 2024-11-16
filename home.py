from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio, logging
from config import token
import random
bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

random_number = random.randint(1, 3)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Я загадал число от 1 до 3 Угадайте его")

@dp.message(F.text == "1")
async def ugadaniy_chislo(message: Message):
    if random_number == 3:
        await message.reply("Правильно вы отгадали")
        await message.answer_photo(photo = "https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.reply("Неправильно попробуйте снова")
        await message.answer_photo(photo = "https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message(F.text == "2")
async def ugadaniy_chislo(message: Message):
    if random_number == 2:
        await message.reply("Правильно вы отгадали")
        await message.answer_photo(photo = "https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.reply("Неправильно попробуйте снова")
        await message.answer_photo(photo = "https://media.makeameme.org/created/sorry-you-lose.jpg")
        

@dp.message(F.text == "3")
async def ugadaniy_chislo(message: Message):
    if random_number == 3:
        await message.reply(f"Правильно вы отгадали")
        await message.answer_photo(photo = "https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.reply("Неправильно попробуйте снова")
        await message.answer_photo(photo = "https://media.makeameme.org/created/sorry-you-lose.jpg")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())