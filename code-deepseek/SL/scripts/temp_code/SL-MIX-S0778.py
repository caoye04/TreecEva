from collections import Counter

def analyze_sensor_readings(readings):
    # Irrelevant sensor processing (distractor)
    temp_variance = sum([(r - sum(readings)/len(readings))**2 for r in readings]) / len(readings)
    max_reading = max(readings)
    min_reading = min(readings)
    return temp_variance + max_reading - min_reading  # Unused calculation

def process_data_point(data):
    # Main computation path with multiple steps
    processed_values = [x * 2 if x % 3 == 0 else x + 5 for x in data]
    
    # Misleading intermediate calculations
    irrelevant_sum = sum([x**2 for x in processed_values])  # Distractor
    filtered_data = [x for x in processed_values if x > 15]
    
    # Dead code path that's never executed
    if len(filtered_data) > 100:
        unused_result = irrelevant_sum / len(filtered_data)
    
    # Key computation with bitwise operations
    bitwise_result = (processed_values[0] & 0b1111) | (processed_values[1] << 2)
    
    # Final relevant calculation
    counter_data = Counter(filtered_data)
    final_value = sum([k * v for k, v in counter_data.items()]) + bitwise_result
    
    return final_value

# Main execution
sensor_data = [8, 12, 6, 18, 9, 21]

# Distractor function calls and variables
sensor_analysis = analyze_sensor_readings(sensor_data)
redundant_calc = sensor_analysis * 2 - 15  # Never used

# Critical data processing
processed_readings = [x + 3 if x % 2 == 0 else x - 2 for x in sensor_data]
analyzed_results = [x for x in processed_readings if x % 3 != 0]

# Final key statement
final_computation = process_data_point(analyzed_results)

print(f"Target result: {final_computation}")