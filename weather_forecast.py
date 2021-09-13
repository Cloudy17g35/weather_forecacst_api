import requests

api_key = input('your_key :> ')
base_url = 'api.openweathermap.org/data/2.5/weather?'
city_name = input('Your city name:> ')

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
json_map = response.json()


if response.status_code != '404':
    print(f'Your weather for {city_name}:')
    print()
    print(f'Temperature (NOW) in Kelvins // Temperature in Celsius: {json_map["main"]["temp"]} K // {int(json_map["main"]["temp"]- 273)} C')
    print()
    print(f'Weather description: {json_map["weather"][0]["description"]}')
    print()
else:
    print('City not found')
