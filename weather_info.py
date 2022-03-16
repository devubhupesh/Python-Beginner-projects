import requests
from pprint import pprint

API_Key = 'da06dd4aeb79d846fb5256e342d509a9'

city = input("Enter a city: ")
#url from openweather site  and q stands for query
base_url = "api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q"+city 

weather_data = requests.get(base_url).json()

pprint(weather_data)