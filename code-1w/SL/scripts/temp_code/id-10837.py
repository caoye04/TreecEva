def process_weather_data():
    raw_readings = {'New York': '72.5F', 'Los Angeles': '79.1F', 'Chicago': '65.3F'}
    conversion_factor = 5.0 / 9.0
    offset = 32
    city = 'Chicago'
    
    # Extract numeric part from string readings and convert to Celsius
    cleaned_readings = {}
    for location, temp_str in raw_readings.items():
        if temp_str.endswith('F'):
            fahrenheit_value = float(temp_str[:-1])
            celsius_value = (fahrenheit_value - offset) * conversion_factor
            cleaned_readings[location] = round(celsius_value, 2)
    
    # Apply calibration adjustment based on sensor type
    sensor_types = {'New York': 'A', 'Los Angeles': 'B', 'Chicago': 'A'}
    adjusted_readings = {}
    for loc, temp_c in cleaned_readings.items():
        if sensor_types[loc] == 'A':
            adjusted_readings[loc] = temp_c + 1.2  # calibration offset
        else:
            adjusted_readings[loc] = temp_c + 0.8
    
    final_temperature = adjusted_readings[city]
    print(f"Result: {final_temperature}")

process_weather_data()