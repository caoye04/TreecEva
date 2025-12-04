# Temperature readings analysis function
def analyze_readings(data):
    # Filter out invalid temperature readings (below -50°C)
    valid_readings = [temp for temp in data if temp > -50]
    
    # Some metadata about the readings
    num_readings = len(data)
    max_temp = max(valid_readings) if valid_readings else 0
    min_temp = min(valid_readings) if valid_readings else 0
    
    # Filter readings between 20-30°C (comfortable temperature range)
    comfortable_range = [temp for temp in valid_readings if 20 <= temp <= 30]
    comfortable_count = len(comfortable_range)
    
    # Get readings that are divisible by 3 (for sensor calibration check)
    filtered_data = [temp for temp in valid_readings if temp % 3 == 0]
    
    # Count unique temperature values for reporting
    unique_elements = len(set(filtered_data))
    
    print(f"Result: {unique_elements}")
    return unique_elements

# Temperature readings from various sensors (in Celsius)
temperature_data = [21, 24, 18, 27, 24, 21, 30, 15, 18, 27, 33, 24, 21, 18, 15]
result = analyze_readings(temperature_data)