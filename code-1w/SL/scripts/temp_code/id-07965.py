def analyze_temperature_readings():
    raw_readings = [23.5, 19.0, 25.8, 17.2, 30.1, 22.0, 27.3, 18.9, 24.4, 26.7]
    threshold = 20.0
    
    # Convert to integer approximations for quick analysis
    int_approximations = [int(temp) for temp in raw_readings]
    
    # Identify readings above threshold using lambda
    high_temp_filter = lambda x: x > threshold
    filtered_values = list(filter(high_temp_filter, raw_readings))
    
    # Apply correction factor to all values (irrelevant to final result)
    corrected_readings = [round(temp * 0.98, 2) for temp in raw_readings]
    
    # Calculate sum of filtered original values
    filtered_sum = sum(filtered_values)
    
    # Dummy string operation (distractor)
    status_msg = "Analysis Complete".lower().replace(" ", "_")
    
    return filtered_sum

result = analyze_temperature_readings()
print(f"Result: {result}")