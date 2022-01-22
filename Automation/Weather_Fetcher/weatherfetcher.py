import requests
import sys

API_KEY = "26a10569819d32bfdd2ff6fe6510aba0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(request_url)


if response.status_code == 200:
	data = response.json()
	weather = data['weather'][0]['description']
	temperature = data['main']['temp']
else:
	print("An error occured.")


parameters = sys.argv[1:]

if len(parameters) == 1:
	if parameters[0] == "list":
		for key, value in data.items():
			print(key, value)

	else:
		print("Invalid command!")

elif len(parameters) == 0:
	print(f'Weather is {weather}')
	print(f'Temperature: {temperature} celsius')

else:
	print("Too many commands")








