def calculate_offset(base_value, multiplier):
    offset = base_value * multiplier - 15
    temp_offset = offset + 7
    return temp_offset

def process_data_set(data_points, threshold):
    valid_points = {}
    processed_count = 0
    for key, value in data_points.items():
        if value > threshold:
            valid_points[key] = value * 2
            processed_count += 1
        else:
            valid_points[key] = value // 3
    dummy_counter = len(data_points) * 2
    unused_value = dummy_counter - processed_count
    return valid_points, processed_count

def update_results(primary, secondary, adjustment):
    primary_processed, primary_count = process_data_set(primary, 20)
    secondary_processed, secondary_count = process_data_set(secondary, 15)
    
    offset_calc = calculate_offset(primary_count, 3)
    misleading_temp = offset_calc + secondary_count * 2
    
    combined_values = []
    for key in primary_processed:
        if key in secondary_processed:
            combined_values.append(primary_processed[key] + secondary_processed[key])
    
    if len(combined_values) > 0:
        final_adjustment = sum(combined_values) * adjustment
        result = final_adjustment - offset_calc
    else:
        result = adjustment * 100
    
    return result

primary_data = {'A': 25, 'B': 18, 'C': 32, 'D': 12}
secondary_data = {'A': 8, 'B': 22, 'E': 45}
adjustment_factor = 2

final_result = update_results(primary_data, secondary_data, adjustment_factor)
print(f"Result: {final_result}")