def process_weather_data(data):
    # Extract temperatures from data
    temperatures = data[::2]  # Every other value is a temperature
    humidity = data[1::2]  # These are humidity values (not used in calculation)
    
    # Calculate some statistics
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    
    # Filter temperatures within 10 degrees of average
    filtered_temperatures = []
    for temp in temperatures:
        # Check if temperature is within range
        if abs(temp - avg_temp) <= 10:
            filtered_temperatures.append(temp)
        else:
            # Record outliers but don't use them
            outlier = temp
    
    # Calculate humidity metrics (not used in final result)
    humidity_threshold = 60
    high_humidity_days = [h for h in humidity if h > humidity_threshold]
    
    # Process the filtered temperatures
    temp_celsius = [round((t - 32) * 5/9, 1) for t in filtered_temperatures]
    temp_adjustment = 2.5
    adjusted_celsius = [t + temp_adjustment for t in temp_celsius]
    
    # Calculate the sum of filtered temperatures (in original Fahrenheit)
    filtered_sum = sum(filtered_temperatures)
    
    # Calculate other metrics that aren't used in the result
    range_value = max_temp - min_temp
    variance = sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)
    
    # Return the sum of filtered values
    return filtered_sum

# Weather data: [temp1, humidity1, temp2, humidity2, ...]
weather_data = [72, 65, 75, 55, 95, 80, 68, 70, 73, 62, 71, 58]
result = process_weather_data(weather_data)
print(f"Result: {result}")