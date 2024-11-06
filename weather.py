import requests
import json
API_KEY = 'b1b98451b7d2f97863e7dead570d4c43'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
def get_weather(city):
    params = {
	'q' : city,
        'appid' : API_KEY,
        'units' : 'metric'
    }
    response =requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_data = data['weather'][0]
        description = weather_data['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
       print("Failed to retrieve data. Plase Check City name.")
if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)




