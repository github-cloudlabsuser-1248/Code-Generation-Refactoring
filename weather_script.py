import requests
import os

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        temp = main.get('temp')
        humidity = main.get('humidity')
        condition = weather.get('description')
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    else:
        print(f"Failed to get weather data for {city_name}. Error: {response.status_code}")

def main():
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
        return
    city_name = input("Enter city name: ")
    get_weather(city_name, api_key)

if __name__ == "__main__":
    main()
