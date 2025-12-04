def analyze_weather_data(readings, threshold=30):
    # Convert Celsius to Fahrenheit for analysis
    fahrenheit_readings = [c * 9/5 + 32 for c in readings]
    
    # Find anomalous readings (potential sensor errors)
    anomalous = {i for i, temp in enumerate(readings) if temp < -10 or temp > 45}
    
    # Calculate average temperature (not used in final result)
    avg_temp = sum(readings) / len(readings) if readings else 0
    
    # Track daily temperature fluctuations
    fluctuations = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    max_fluctuation = max(fluctuations) if fluctuations else 0
    
    # Apply quality filter based on threshold
    filtered_temperatures = []
    for i, temp in enumerate(readings):
        # Skip anomalous readings
        if i in anomalous:
            continue
        # Apply conditional data transformation
        adjusted_temp = temp - 0.5 if temp > threshold else temp + 0.5
        filtered_temperatures.append(adjusted_temp if i % 2 == 0 else temp)
    
    # Calculate result from filtered data
    result = sum(filtered_temperatures)
    
    # Secondary calculations (not affecting final answer)
    variance = sum((t - avg_temp) ** 2 for t in readings) / len(readings) if readings else 0
    trend_indicator = 1 if avg_temp > threshold else -1 if avg_temp < threshold else 0
    
    print(f"Result: {result}")
    return result

# Weather station readings (in Celsius)
temperature_readings = [22.5, 23.8, 25.1, 28.7, 26.4, 24.9, 47.2, 23.1]
analyze_weather_data(temperature_readings, 25)