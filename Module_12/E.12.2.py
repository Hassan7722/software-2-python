import json
import requests

ask_user = input("Enter a city name: ")
city_name = ask_user
api_key = "94c3ee22ae6c09fea689df85226d9f4a"

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key + "&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print("Weather:", description)
        print("Temperature:", temperature, "°C")

    else:
        print("City not found.")

except requests.exceptions.RequestException:
    print("Request could not be completed.")