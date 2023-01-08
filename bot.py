import telebot
from config import TOKEN, open_weather_token
import requests
import datetime


dp = telebot.TeleBot(TOKEN)


@dp.message_handler(commands=["start"])
def start(message):
    dp.send_message(message.chat.id, "Привет! Напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
def get_weather(message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Haze": "Туман \U0001F32B",
        "Smoke": "Туман \U0001F32B"
        }
    try:
        r = requests.get("http://api.openweathermap.org/data/2.5/weather", # + weather
                 params={'q':message.text , 'units': 'metric', 'lang':"ru", 'APPID': open_weather_token})
        
        data = r.json()

        city = data["name"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        temp = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        answer= (f"🔹🔹{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}🔹🔹\n"
                f"Погода в городе: {city}\nТемпература на сегодня:\n  мин.{temp_min}C° - макс.{temp_max}C°\n"
                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n\n"
                f"В городе {city} сейчас {wd}.\n\n")
        answer += f"Температура сейчас около: {temp}C°\n"
        if temp <=-30:
            answer += "На улице так холодно, лучше сиди дома!"
        elif temp  >-30 and  temp <= 0:
            answer += "Холодно. Оденься потеплее!"   
        elif temp > 0 and temp <= 15:
            answer+= "Холодновато. Куртку накинь!"
        elif temp > 15 and temp <= 30:
            answer += "Тепло. Можешь погуляйть в парке!" 
        elif temp > 30 and temp <=50:
            answer += "На улице жарко!"    
        elif temp > 50:
            answer += "Там такая жара, лучше сиди дома!"
        else:
            answer +="На улице нормально!"

        dp.send_message(message.chat.id, answer)      
        

    except:
        dp.send_message(message.chat.id,"\U00002620 Проверьте название города \U00002620")

    


if __name__ == '__main__':
    dp.polling(none_stop=True)

