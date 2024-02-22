from modules.weather import Weather

def main():
    api_key = "3ac4781dd923325964bf74f0c4e1b05d"  # API anahtarınızı buraya ekleyin
    city_name = input("Enter the city name: ")

    weather_client = Weather(api_key)
    result = weather_client.get_weather(city_name)

    print(result)

if __name__ == "__main__":
    main()
