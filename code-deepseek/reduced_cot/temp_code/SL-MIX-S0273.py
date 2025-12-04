def analyze_climate_data():
    temperature_readings = [22.5, 19.8, 25.3, 18.9, 23.7, 21.2]
    humidity_levels = [65, 72, 58, 75, 62, 68]
    
    # Main calculation - this determines the final result
    temperature_analysis = lambda readings: (max(readings) + min(readings)) / 2
    final_temperature = temperature_analysis(temperature_readings)
    
    # Distraction operations that don't affect final_temperature
    average_humidity = sum(humidity_levels) / len(humidity_levels)
    temperature_variance = max(temperature_readings) - min(temperature_readings)
    
    # More distraction - processing that's unused
    filtered_readings = [temp for temp in temperature_readings if temp > 20]
    reading_count = len(filtered_readings)
    
    print(f"Target result: {final_temperature}")

analyze_climate_data()