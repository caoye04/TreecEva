def calculate_temperature_stats(measurements):
    temp_sum = sum(measurements)
    temp_count = len(measurements)
    temp_avg = temp_sum / temp_count
    
    # Distractor calculations that don't affect final result
    temp_range = max(measurements) - min(measurements)
    temp_squared = [x**2 for x in measurements]
    temp_variance = sum(temp_squared) / temp_count - temp_avg**2
    
    # Main logic chain
    adjusted_temps = [temp + 5 for temp in measurements]
    filtered_temps = [temp for temp in adjusted_temps if temp > 20]
    
    # More distractors
    temp_product = 1
    for temp in measurements:
        temp_product *= temp
    
    # Key calculation path
    if filtered_temps:
        final_temp = sum(filtered_temps) / len(filtered_temps)
    else:
        final_temp = temp_avg
    
    # Build metrics dictionary
    metrics = {
        'average': temp_avg,
        'range': temp_range,
        'temperature': final_temp,
        'variance': temp_variance,
        'product': temp_product
    }
    
    # Final metrics with some unused operations
    final_metrics = {}
    for key, value in metrics.items():
        if key in ['average', 'temperature', 'variance']:
            final_metrics[key] = round(value, 2)
    
    target_value = final_metrics['temperature']
    print(f"Target result: {target_value}")

# Execute with sample data
sensor_readings = [15, 22, 18, 25, 20, 17]
calculate_temperature_stats(sensor_readings)