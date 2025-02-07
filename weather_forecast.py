
# Citim de la tastatura un oras si ne intoarce vremea
# Avem un anumit config, daca acele valori, configul nostru este depasit, atunci se va face o notificare.
# Notificarea se face pe whatsapp sau pe player notification
# Face prima noastra interfata grafica cu gradio

import json
import os
import pywhatkit as wapp
import requests
from player import notification
import time



def read_config(path: str = "config.json"):
    try:
        with open(path, "r") as f:
            data = json.londs(f.read())
    except FileNotFoundError as e:
        print("Please add the config file")
        return {}

    return data


# pressure
# wind_kph
# temp_c

def get_weather(config: dict, city: str) -> dict:
    try:
        headers = {"key": os.environ['weather_api_key']}
        url = config['url'] + f"?q={city}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
           # return json.loads(response.text)
           weather = json.loads(response.text)

           return {"temp": weather['current']['temp_c'],
                   "pressure": weather['current']['temp_c'],
                   "wind_speed": weather['current']['temp_c']
                   }
        elif response.status_code == 401:
            print("Please add a valid api key")
            return{}
    except Exception as e:
        print(f"Something went wrong..")

def is_worth_notifying(config: dict, weather: dict) -> bool:
    if weather['temp'] > config['max_temp'] or weather['pressure'] > config['max_pressure'] or weather['wind_speed'] > config['max_wind_velocity']:
        return True
    return False


def send_notification(config: dict, weather: dict):
    if is_worth_notifying(config, weather):
        message = f"""
        Temp: {weather['temp']}
        Pressure: {weather['pressure']}
        Wind_speed: {weather['wind_speed']}
         """
        for alert in config['notification_system']:
            if alert == "player":
                notification.notify(title=city, message=message)
    #         elif alert == "whatsapp":
    #             wapp.sendwhatmsg_instantly(phone_no= os.environ['personal_phone_number'], message=message)
    # else:
    #     pass



if __name__ == '__main__':
    config = read_config()

    while True:
        for city in config['cities']:
            weather = get_weather(config, city)
            # print(city + "\n" + json.dumps(weather, indent=4))
            send_notification(config, weather)
            time.sleep(config['sleep_time'])
