# Weather data analysis for tourism recommendation system
weather_data = {
    "Paris": {"temp": 28, "humidity": 55, "forecast": "Sunny"},
    "London": {"temp": 22, "humidity": 70, "forecast": "Cloudy"},
    "Rome": {"temp": 32, "humidity": 45, "forecast": "Clear"},
    "Berlin": {"temp": 24, "humidity": 50, "forecast": "Partly Cloudy"},
    "Madrid": {"temp": 30, "humidity": 35, "forecast": "Sunny"},
    "Amsterdam": {"temp": 26, "humidity": 65, "forecast": "Rainy"}
}

temp_threshold = 25
humidity_max = 60
total_cities = len(weather_data)

# Find cities with ideal weather conditions for tourism
eligible_count = sum(1 for city, stats in weather_data.items() if stats["temp"] > 25 and stats["humidity"] < 60)

print(f"Result: {eligible_count}")