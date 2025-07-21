from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    
    dates = []
    temperatures = []
    sky_conditions = []
    
    for data_point in filtered_data:
        dates.append(data_point["dt_txt"])
        temperatures.append(data_point["main"]["temp"])
        sky_conditions.append(data_point["weather"][0]["main"])
    
    if kind == "Temperature":
        return dates, temperatures
    elif kind == "Sky":
        return dates, sky_conditions

if __name__ == "__main__":
    print(get_data(place="New York", forecast_days=5, kind="Temperature"))