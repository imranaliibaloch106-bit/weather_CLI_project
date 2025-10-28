# Import required libraries
import requests
from config import API_KEY
import datetime

# Function to fetch weather data
def get_weather(city="Badin"):
    """
    Fetch current weather data for Badin from OpenWeatherMap API.
    
    Args:
        city (str): City name (default: Badin)
    
    Returns:
        None
    """
    # Base URL for OpenWeatherMap API
    base_url = "https://home.openweathermap.org/api_keys"
    
    # Parameters for API request
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        # Send GET request to API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Print weather report
        print("\n🌦 Live Weather Report")
        print(f"📍 City: {data['name']}, {data['sys']['country']}")
        print(f"🕒 Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"🤔 Feels Like: {data['main']['feels_like']}°C")
        print(f"🌤 Weather: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"\n❌ HTTP Error occurred: {http_err}")
    except Exception as e:
        print("⚠ Error occurred:", e)

# Main function
def main():
    print("=== 🌦 Weather CLI App (Badin City) ===")
    city = input("Enter city name (default: Badin): ") or "Badin"
    get_weather(city)

# Run main function
if __name__ == "_main_":
    main()
