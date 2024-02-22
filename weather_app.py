# weather_app.py

import requests
import os

api_key = os.getenv("api_key")  # API anahtarını çevresel değişkenden al

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"] - 273.15  # Kelvin to Celsius
            city_name = data["name"]

            print(f"Weather in {city_name}: {weather_description}")
            print(f"Temperature: {temperature:.2f} °C")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    
    get_weather(city_name)
