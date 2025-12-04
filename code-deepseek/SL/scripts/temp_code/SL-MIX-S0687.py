def analyze_temperature_data(temps):
    # Filter valid temperature readings
    valid_temps = [t for t in temps if -50 <= t <= 50]
    
    # Calculate some intermediate metrics (distractor)
    temp_range = max(valid_temps) - min(valid_temps) if valid_temps else 0
    avg_temp = sum(valid_temps) / len(valid_temps) if valid_temps else 0
    
    # Process temperatures with threshold adjustment
    threshold = 25
    processed_values = []
    adjustment_factor = 2  # Not used in final calculation
    
    for i, temp in enumerate(valid_temps):
        if temp > threshold:
            # Apply cooling adjustment
            adjusted = temp - 5
        else:
            # Apply heating adjustment
            adjusted = temp + 3
        processed_values.append(adjusted)
    
    # Calculate monthly averages (distractor)
    monthly_data = [sum(valid_temps[i:i+7])/7 for i in range(0, len(valid_temps), 7) if i+7 <= len(valid_temps)]
    
    # Final calculation - integer average of processed values
    final_tally = sum(processed_values) // len(processed_values)
    
    print(f"Target result: {final_tally}")

# Test data - temperature readings from environmental sensors
sensor_readings = [22, 28, 19, 31, 24, 27, 20, 29, 23, 26]
analyze_temperature_data(sensor_readings)