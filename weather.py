
# This gives an example of API using

import requests
import os
from pprint import pprint

def getCurrentWeather():
    print("\n*** Get current weather conditions ***\n")
    city = input("\nPlease enter a city name :\n")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    # print(request_url)
    weatherData = requests.get(request_url).json()
    # pprint(weatherData)
    # actually doesn't work -> error : invalid API key, maybe need a subscription to use that API as well or did wrong manipulation on API key, anyways it should work

    print(f"\nCurrent weather for {weatherData["name"]}")
    print(f"\nTempeture is {weatherData["main"]["temp"]}°C")
    print(f"\nFeels like {weatherData["main"]["feels_like"]}°C and {weatherData["weather"][0]["description"]}.")

if __name__ == "__main__":
    getCurrentWeather()