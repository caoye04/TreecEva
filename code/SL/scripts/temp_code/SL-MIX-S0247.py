def process_data_points(data_stream):
    filtered_values = [x for x in data_stream if x > 15]
    
    temp_sum = 0
    for idx, value in enumerate(filtered_values):
        if idx % 2 == 0:
            temp_sum += value * 2
        else:
            temp_sum += value
    
    result = temp_sum // len(filtered_values) if filtered_values else 0
    
    adjustment = 7
    final_output = result + adjustment
    
    print(f"Target result: {final_output}")

# Test data
sensor_readings = [12, 18, 25, 9, 32, 21, 14, 29]
process_data_points(sensor_readings)