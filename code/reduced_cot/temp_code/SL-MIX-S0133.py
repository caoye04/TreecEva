def analyze_weather_data():
    # Simulated weather station readings (temperature in Celsius)
    temperature_readings = [8, 12, 15, 9, 18, 22, 7, 14, 20, 11]
    
    # Create mapping of days to temperatures
    weather_data = {f'Day_{i+1}': temp for i, temp in enumerate(temperature_readings)}
    
    # Intermediate calculations that don't affect final result
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    max_temp = max(temperature_readings)
    
    # This intermediate variable is used for distraction
    temp_variance = sum((t - avg_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
    
    # Extract relevant data subset (distractor operation)
    data_slice = {k: v for k, v in weather_data.items() if v >= 10}
    
    # Key statement: Process only temperatures above 5°C
    result_dict = {key: val * 2 for key, val in data_slice.items() if val > 5}
    
    # Final calculation (answer is here)
    processed_result = sum(result_dict.values()) // len(result_dict)
    
    print(f"Target result: {processed_result}")
    return processed_result

# Execute the analysis
analyze_weather_data()