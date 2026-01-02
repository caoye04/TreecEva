def analyze_weather_data():
    temperatures = [23.5, 19.0, 21.8, 18.2, 24.3, 22.1]
    humidity_levels = [45, 50, 52, 58, 47, 49]  # Irrelevant data for distraction
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    avg_temp = sum(temperatures) / len(temperatures)
    recent_temps = temperatures[1:4]
    
    if len(recent_temps) > 0:
        peak_temperature = max(recent_temps)
        if peak_temperature < avg_temp:
            peak_temperature += 1.5
    else:
        return -1

    # Additional unrelated computation
    total_humidity = sum(humidity_levels)
    
    print(f"Result: {peak_temperature}")

analyze_weather_data()