import requests



API_KEY = "1d2a8af15b4046cdbc31ebf2ec458544"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return None
    
def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    if weather:
        print(f"\nWeather in {weather['city']}:")
        print()
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
        print(f"Condition: {weather['description'].capitalize()}")
    else:
        print("Error: City not found or API issue!")

if __name__ == "__main__":
    main()
