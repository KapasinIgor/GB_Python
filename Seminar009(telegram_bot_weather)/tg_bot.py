import requests
import datetime
from config import bot_token, weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from find_city import find_city

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название российского города и я пришлю сводку погоды!")


@dp.message_handler()
async def get_weather(message: types.Message):
    lat, lon, city = find_city(message.text)
    try:
        url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&lang=ru_RU"
        header = {'X-Yandex-API-Key': weather_token}
        r = requests.get(url, headers=header)
        data = r.json()

        brand_yandex = "По данным сервиса Яндекс.Погода"
        temperature = data['fact']['temp']
        humidity = data['fact']['humidity']
        pressure = data['fact']['pressure_mm']
        wind = data['fact']['wind_speed']

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"{brand_yandex}\nСейчас в городе {city}:\n"
                            f"Температура: {temperature}С°\n"
                            f"Влажность: {humidity}%\n"
                            f"Давление: {pressure} мм.рт.ст.\n"
                            f"Скорость ветра: {wind} м/с\n"
                            f"***Хорошего вам дня!***")

    except:
        await message.reply("\U00002620 Проверьте правильность написания города! \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)
