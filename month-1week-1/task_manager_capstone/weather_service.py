"""
Weather Service Module
Day 14 Capstone: Demonstrates API integration
"""

import requests


class WeatherService:
    """
    Service for fetching weather data.
    
    API CONCEPTS:
    - HTTP requests
    - JSON parsing
    - Error handling
    """
    
    def __init__(self):
        self.base_url = "https://wttr.in"
    
    def get_weather(self, city):
        """
        Get current weather for a city.
        
        Returns:
            dict with weather info or None if failed
        """
        try:
            url = f"{self.base_url}/{city}?format=j1"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                current = data['current_condition'][0]
                
                return {
                    'temp_f': current['temp_F'],
                    'temp_c': current['temp_C'],
                    'condition': current['weatherDesc'][0]['value'],
                    'humidity': current['humidity']
                }
            else:
                return None
                
        except Exception as e:
            print(f"Weather fetch error: {e}")
            return None
    
    def get_weather_advice(self, city):
        """
        Get weather-based task advice.
        
        DEMONSTRATES:
        - Using API data for decision making
        - String generation based on conditions
        """
        weather = self.get_weather(city)
        
        if not weather:
            return "Unable to fetch weather data."
        
        temp_f = int(weather['temp_f'])
        condition = weather['condition'].lower()
        
        advice = []
        
        # Temperature-based advice
        if temp_f > 85:
            advice.append("🌡️ It's hot! Schedule outdoor tasks for morning/evening.")
        elif temp_f < 32:
            advice.append("❄️ It's freezing! Indoor tasks recommended.")
        elif temp_f < 50:
            advice.append("🧥 It's cold! Bundle up for outdoor tasks.")
        
        # Condition-based advice
        if 'rain' in condition or 'drizzle' in condition:
            advice.append("🌧️ Rain expected! Postpone outdoor tasks.")
        elif 'snow' in condition:
            advice.append("🌨️ Snow! Drive carefully for errands.")
        elif 'clear' in condition or 'sunny' in condition:
            advice.append("☀️ Great weather for outdoor tasks!")
        
        if not advice:
            advice.append("🌤️ Weather is moderate - good for any tasks!")
        
        return "\n".join(advice)


if __name__ == "__main__":
    # Test weather service
    service = WeatherService()
    
    print("Testing Weather Service...")
    print("="*60)
    
    city = "New York"
    weather = service.get_weather(city)
    
    if weather:
        print(f"\nWeather in {city}:")
        print(f"  Temperature: {weather['temp_f']}°F ({weather['temp_c']}°C)")
        print(f"  Conditions: {weather['condition']}")
        print(f"  Humidity: {weather['humidity']}%")
        
        print(f"\nTask Advice:")
        print(service.get_weather_advice(city))
    else:
        print("Failed to fetch weather")