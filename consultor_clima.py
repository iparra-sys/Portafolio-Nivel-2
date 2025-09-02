import requests

# 🔑 Reemplaza con tu API Key de OpenWeatherMap
API_KEY = "TU_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Diccionario de emojis para condiciones climáticas
EMOJIS_CLIMA = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "💨",
    "Haze": "🌁",
    "Dust": "🌪️",
    "Fog": "🌫️",
    "Sand": "🏜️",
    "Ash": "🌋",
    "Squall": "💨",
    "Tornado": "🌪️"
}

def obtener_clima(ciudad):
    params = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        datos = response.json()
        temp = datos["main"]["temp"]
        humedad = datos["main"]["humidity"]
        condicion = datos["weather"][0]["main"]
        descripcion = datos["weather"][0]["description"]

        emoji = EMOJIS_CLIMA.get(condicion, "🌍")

        print(f"\n🌍 Clima en {ciudad.capitalize()}")
        print(f"{emoji} Condición: {descripcion.capitalize()}")
        print(f"🌡️ Temperatura: {temp}°C")
        print(f"💧 Humedad: {humedad}%\n")
    else:
        print("⚠️ Ciudad no encontrada. Intenta de nuevo.\n")


if __name__ == "__main__":
    while True:
        ciudad = input("🏙️ Ingrese el nombre de la ciudad (o 'salir' para terminar): ").strip()
        if ciudad.lower() == "salir":
            print("👋 Hasta luego, gracias por usar el consultor de clima.")
            break
        obtener_clima(ciudad)
