def calculate_temperature_stats(temp_readings):
    # Misleading intermediate calculation
    fake_average = sum(temp_readings) / max(len(temp_readings), 1)
    temp_variance = sum([(x - fake_average) ** 2 for x in temp_readings]) / len(temp_readings)
    
    # Actual target calculation
    valid_readings = [x for x in temp_readings if 15 <= x <= 35]
    if not valid_readings:
        return 0
    
    # Distractor operations
    unused_temp_range = max(temp_readings) - min(temp_readings) if temp_readings else 0
    misleading_median = sorted(temp_readings)[len(temp_readings)//2] if temp_readings else 0
    
    # Core logic with bitwise operations
    processed_data = [(x * 2) | 1 for x in valid_readings]
    target_value = sum(processed_data) // len(processed_data)
    return target_value

def filter_sensor_data(raw_data):
    # Irrelevant string manipulation
    data_string = ','.join(map(str, raw_data))
    split_data = data_string.split(',')
    
    # Main filtering with lambda
    filtered = list(filter(lambda x: x % 3 != 0 and x % 7 != 0, raw_data))
    
    # Dead code path
    if len(filtered) > 10:
        oversized_list = [x * 2 for x in filtered]
    
    return filtered

def process_final_data(input_list):
    # Multiple irrelevant computations
    fake_sum = sum(input_list) * 1.5
    misleading_product = 1
    for num in input_list[:3]:
        misleading_product *= num
    
    # Key transformation with tuple operations
    data_pairs = [(x, x ^ 0xFF) for x in input_list]
    processed_values = [a + b for a, b in data_pairs]
    
    # Final calculation with bit masking
    final_result = sum(processed_values) & 0x3F
    return final_result

# Main execution
sensor_readings = [18, 22, 25, 29, 32, 14, 36, 21, 28, 31, 16, 24, 27, 33, 19]
filtered_results = filter_sensor_data(sensor_readings)
processed_stats = calculate_temperature_stats(filtered_results)

# Irrelevant intermediate variable
intermediate_calc = (processed_stats * 3) // 2

# Target execution point
final_output = process_final_data(filtered_results)

# Misleading print statements
print(f"Intermediate: {intermediate_calc}")
print(f"Filtered count: {len(filtered_results)}")
print(f"Target result: {final_output}")