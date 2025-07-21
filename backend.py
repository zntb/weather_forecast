from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={forecast_days}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if kind == "Temperature":
        return [d["main"]["temp"] for d in data["list"]]
    elif kind == "Sky":
        return [d["weather"][0]["main"] for d in data["list"]]
    
    return data

if __name__ == "__main__":
    print(get_data(place="New York", forecast_days=5, kind="Temperature"))