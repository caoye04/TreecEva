def validate_readings(data_points):
    irrelevant_var = [x * 2 for x in range(10)]
    misleading_sum = sum(range(15)) + 25
    return [x for x in data_points if x > 0]

def process_sensors(raw_data):
    temp_calc = lambda x: (x * 1.8) + 32
    converted = [temp_calc(val) for val in raw_data]
    dead_code_path = [val ** 2 for val in converted if val < 50]
    return converted

def aggregate_data(readings, threshold):
    validation_map = {'valid': lambda x: x > threshold, 'invalid': lambda x: x <= threshold}
    filtered_data = list(filter(validation_map['valid'], readings))
    
    irrelevant_dict = {'a': 42, 'b': 73, 'c': 19}
    misleading_avg = sum(irrelevant_dict.values()) / len(irrelevant_dict)
    
    if len(filtered_data) > 2:
        sorted_values = sorted(filtered_data)
        middle_index = len(sorted_values) // 2
        if len(sorted_values) % 2 == 0:
            result = (sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2
        else:
            result = sorted_values[middle_index]
    else:
        result = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    
    distractor_op = (result * 3.14) - 15.7
    return round(result, 2)

sensor_readings = [18.5, 22.3, 19.8, 25.1, 20.9, 24.7, 17.2]
threshold = 20.0
processed = process_sensors(sensor_readings)
validated = validate_readings(processed)
final_result = aggregate_data(sensor_readings, threshold)
print(f"Target result: {final_result}")