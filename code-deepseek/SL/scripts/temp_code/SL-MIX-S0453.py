def analyze_temperature_trends():
    raw_readings = [25, 32, 18, 29, 34, 22, 31, 27]
    filtered_data = [temp for temp in raw_readings if temp > 20]
    
    # Intermediate calculations (distractor)
    max_temp = max(raw_readings)
    min_temp = min(raw_readings)
    temp_range = max_temp - min_temp
    
    # Process data
    adjusted_data = [temp + 5 if temp < 25 else temp - 3 for temp in filtered_data]
    
    # More intermediate variables (distractor)
    total_adjusted = sum(adjusted_data)
    average_temp = total_adjusted / len(adjusted_data)
    
    # Key calculation
    scaling_factor = 4 if len(adjusted_data) > 5 else 2
    final_metric = adjusted_data[-1] // scaling_factor
    
    # Unused calculation (distractor)
    normalized_metric = final_metric * 1.5
    
    print(f"Result: {final_metric}")

analyze_temperature_trends()