from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    data = response.json()
    
    # Check if the city was found
    if data.get("cod") != "200":
        raise Exception(data.get("message", "Unknown error occurred"))
    
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
  
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="New York", forecast_days=5))