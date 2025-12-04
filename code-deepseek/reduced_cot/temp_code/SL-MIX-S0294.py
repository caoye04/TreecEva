def process_temperature_data(temps):
    seasonal_temps = [temp for temp in temps if 20 <= temp <= 35]
    temp_range = max(temps) - min(temps)
    adjusted_range = temp_range * 1.5
    
    # Distractor calculations that don't affect final result
    avg_temp = sum(temps) / len(temps)
    temp_variance = sum((t - avg_temp) ** 2 for t in temps) / len(temps)
    
    valid_count = len(seasonal_temps)
    mid_point = len(seasonal_temps) // 2
    selected_temps = seasonal_temps[mid_point-1:mid_point+2] if len(seasonal_temps) >= 3 else seasonal_temps
    
    # Another distractor operation
    scaled_temps = [t * 0.8 for t in selected_temps]
    
    result = sum(selected_temps) + valid_count
    return result

# Main execution
temperature_readings = [18, 25, 32, 19, 28, 35, 21, 29, 33, 16, 27, 31]
result = process_temperature_data(temperature_readings)
final_summary = result + 10
print(f"Target result: {final_summary}")