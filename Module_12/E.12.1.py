import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke = data["value"]
        print(joke)
    else:
        print("Something went wrong.")

except:
    print("Error occurred while fetching data")