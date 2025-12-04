def analyze_temperature_data(temps, threshold=25):
    # Extract temperature readings from different sensors
    valid_indices = []
    invalid_readings = []
    
    # Process temperature data
    for i in range(len(temps)):
        # Check for sensor errors (negative values)
        if temps[i] < 0:
            invalid_readings.append(temps[i])
            # Skip this reading
            continue
            
        # Flag readings above threshold for further analysis
        if temps[i] > threshold:
            # Reverse index calculation for monitoring purposes
            reverse_idx = len(temps) - i - 1
            debug_value = temps[i] * 2 - reverse_idx
        
        # Track valid indices for later processing
        valid_indices.append(i)
    
    # Calculate statistics on invalid readings
    invalid_count = len(invalid_readings)
    invalid_avg = sum(invalid_readings) / invalid_count if invalid_count > 0 else 0
    
    # Process the middle section of the data for trend analysis
    mid_start = len(temps) // 3
    mid_end = 2 * len(temps) // 3
    mid_section = temps[mid_start:mid_end]
    
    # Calculate various metrics
    daily_trend = sum(mid_section) / len(mid_section) if mid_section else 0
    temp_range = max(temps) - min(temps) if temps else 0
    
    # Get the sum of valid temperature readings
    filtered_sum = sum([temps[i] for i in valid_indices])
    
    # Normalize by number of readings
    normalized_sum = filtered_sum / len(valid_indices) if valid_indices else 0
    
    return filtered_sum

# Temperature readings from 10 sensors
temperature_data = [23.5, -2.1, 26.8, 24.3, -1.5, 28.7, 22.9, 25.6, 27.2, 23.1]

# Analyze the data
result = analyze_temperature_data(temperature_data)
print(f"Result: {result}")