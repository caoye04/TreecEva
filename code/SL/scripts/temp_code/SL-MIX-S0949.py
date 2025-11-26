from collections import Counter

def analyze_sensor_data(sensor_readings):
    # Initial sensor processing (distractor)
    reading_sum = sum(sensor_readings)
    average_reading = reading_sum / len(sensor_readings)
    
    # Relevant processing with Counter
    reading_counter = Counter(sensor_readings)
    most_common_value = reading_counter.most_common(1)[0][0]
    
    # Misleading intermediate calculations
    temp_variance = max(sensor_readings) - min(sensor_readings)
    normalized_readings = [x / reading_sum for x in sensor_readings]
    
    # Dead code path (never used)
    unused_metric = temp_variance * 2.5
    
    # Core logic chain
    filtered_values = [x for x in sensor_readings if x > most_common_value]
    if len(filtered_values) > 0:
        processed_values = [x * 1.25 for x in filtered_values]
        delta_adjustment = len(filtered_values) * 3.5
    else:
        processed_values = [most_common_value * 0.8]
        delta_adjustment = -2.0
    
    # Additional distractor operations
    redundant_calc = sum(normalized_readings) * 100
    placeholder_var = redundant_calc - temp_variance
    
    # Final computation
    final_output = processed_values[2] + delta_adjustment
    print(f"Result: {final_output}")
    return final_output

# Main execution
sensor_data = [45, 67, 45, 89, 67, 23, 67, 91, 45]
analyze_sensor_data(sensor_data)