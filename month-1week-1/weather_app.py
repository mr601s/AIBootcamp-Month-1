"""
Weather Application - Real-time weather data from the internet
Day 13: Practical API usage
"""

import requests
from datetime import datetime

def get_weather(city):
    """
    Get current weather for a city
    Using OpenWeatherMap API
    """

    # Free weather API endpoint
    base_url = 'https://wttr.in'

    # Request weather in JSON format
    url = f'{base_url}/{city}?format=j1'

    print(f'\nFetching weather for: {city}')
    print('Connecting to weather service...')

    try: 
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            # Extract current conditions
            current = data['current_condition'][0]

            # Temperature data
            temp_f = current['temp_F']
            temp_c = current['temp_C']
            feels_like_f = current['FeelsLikeF']
            feels_like_c = current['FeelsLikeC']

            # Weather description
            description = current['weatherDesc'][0]['value']

            # Additional data 
            humidity = current['humidity']
            wind_speed = current['windspeedMiles']
            wind_dir = current['winddir16Point']

            # Display weather report
            print("\n" + "="*60)
            print(f"WEATHER REPORT - {city.upper()}")
            print("="*60)
            print(f"Conditions:     {description}")
            print(f"Temperature:    {temp_f}°F ({temp_c}°C)")
            print(f"Feels Like:     {feels_like_f}°F ({feels_like_c}°C)")
            print(f"Humidity:       {humidity}%")
            print(f"Wind:           {wind_speed} mph {wind_dir}")
            print("="*60)
            
            return True
        
        else:
            print(f"❌ Error: Unable to fetch weather data (Status Code: {response.status_code})")
            return False
        
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out")
        return False
    except Exception as e:
        print(f"❌ Error: An unexpected error occurred: {e}")
        return False
    
def main():
    """Main weather app"""

    print("\n" + "="*60)
    print("        REAL-TIME WEATHER APPLICATION")
    print("      Fetch Current Weather Data from Internet")
    print("="*60)

    city = input("\nEnter city name (e.g., London, New York): ").strip()

    if city:
        get_weather(city)
    else:
        print("❌ Error: City name cannot be empty")

if __name__ == '__main__':
    main()