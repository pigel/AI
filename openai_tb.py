import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import openai


logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
openai.api_key = "телеграм @tobe177"

@dp.message_handler()
async def echo(message: types.Message):
    response = openai.Completion.create(
     model="text-davinci-003",
     prompt=message.text,
     temperature=0.9,
     max_tokens=150,
     top_p=1,
     frequency_penalty=0.0,
     presence_penalty=0.6,
     stop=[" Human:", " AI:"]
    )
    await message.answer(response['choices'][0]['text'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
