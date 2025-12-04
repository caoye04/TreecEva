def analyze_sensor_readings(sensor_data):
    # Initial processing with irrelevant calculations
    temp_sum = sum([x * 2 for x in sensor_data if x > 5])
    processed_readings = [abs(x - 10) for x in sensor_data]
    
    # Misleading intermediate variables
    calibration_factor = 3.14159
    sensor_offset = 7.5
    dummy_calc = (temp_sum * calibration_factor) / sensor_offset
    
    # Dead code path that's never used
    if dummy_calc > 1000:
        unused_result = dummy_calc // 2
    else:
        unused_result = dummy_calc * 2
    
    # Main processing logic
    valid_readings = [x for x in processed_readings if x < 8]
    return sum(valid_readings) + len(valid_readings)

def process_results(data_points, cutoff):
    # Irrelevant set operations
    temp_set = set(data_points)
    redundant_union = temp_set | {15, 20, 25}
    
    # Distractor calculations
    base_value = max(data_points) - min(data_points)
    scale_factor = len([x for x in data_points if x % 2 == 0])
    
    # Core logic with nested conditions
    if base_value > cutoff:
        adjusted_data = [x + scale_factor for x in data_points]
        if len(adjusted_data) > 3:
            result = sum(adjusted_data[:4]) // 2
        else:
            result = sum(adjusted_data) * 3
    else:
        filtered_values = [x for x in data_points if x > cutoff // 2]
        if len(filtered_values) > 0:
            result = (sum(filtered_values) * len(data_points)) % 17
        else:
            result = cutoff + len(data_points)
    
    # Unused intermediate result
    misleading_total = result + base_value + scale_factor
    return result

# Main execution
sensor_readings = [12, 8, 15, 3, 9, 11, 6, 14]
threshold = 7

# Irrelevant processing path
intermediate_data = analyze_sensor_readings(sensor_readings)
redundant_calc = intermediate_data * 2 - 5

# Filter data with string operations (distractor)
status_message = "Sensor Status: Active"
if status_message.startswith("Sensor"):
    filtered_data = [x for x in sensor_readings if x > 8]
else:
    filtered_data = sensor_readings

# Key statement with complex reasoning
final_metric = process_results(filtered_data, threshold)

print(f"Target result: {final_metric}")