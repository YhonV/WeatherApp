import os
import requests #Libreria para hacer solicitud HTTP

api_key = "d7377058fc23f59096634f153a494122"


os.system('clear')
user_input = input("Enter city: ")

# Haciendo la solicitud GET a la API de OpenWeatherMap
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# Verificando si se encontró la ciudad en la respuesta de la API
if weather_data.json()["cod"] == "404":
    print("No city found")
else:
    # Extrayendo los datos de clima y temperatura de la respuesta de la API
    weather = weather_data.json()["weather"][0]["main"]
    temp = weather_data.json()["main"]["temp"]

     # Convertir de Fahrenheit a Celsius
    temp_celsius = round((temp - 32) * 5/9,1)
    # Imprimiendo los resultados
    print(f"The weather in {user_input} is: {weather}") 
    print(f"The temperature in {user_input} is: {temp_celsius}°C")
