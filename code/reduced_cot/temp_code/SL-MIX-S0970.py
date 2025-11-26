def analyze_temperature_data(temperatures):
    threshold = 25
    base_offset = 10
    temp_sum = sum(temperatures)
    avg_temp = temp_sum / len(temperatures)
    
    # Distractor calculations that don't affect final result
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    temp_range = max_temp - min_temp
    
    # Intermediate processing
    adjusted_temp = avg_temp + base_offset
    multiplier = 2 if adjusted_temp > 30 else 3
    
    # Conditional filtering
    high_temps = [temp for temp in temperatures if temp > threshold]
    result = len(high_temps) * multiplier
    
    # Final computation with conditional expression
    final_output = result * multiplier if result > threshold else result // multiplier
    
    print(f"Result: {final_output}")
    return final_output

# Sample temperature data for analysis
temp_readings = [18, 22, 27, 31, 19, 29, 33, 24]
analyze_temperature_data(temp_readings)