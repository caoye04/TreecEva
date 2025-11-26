def filter_odd_values(data):
    irrelevant_set = {2, 4, 6, 8, 10}
    temp_cache = [x for x in data if x % 2 == 1]
    misleading_total = sum(irrelevant_set)  # Distractor: 30
    return temp_cache

def process_core_data(values):
    threshold = 7
    dead_code_result = len(values) * 3.14  # Unused calculation
    filtered = [v for v in values if v > threshold]
    sliced_data = filtered[1:-1]  # Remove first and last
    return sum(sliced_data)

def main():
    # Primary dataset
    sensor_readings = [5, 8, 12, 3, 15, 9, 6, 11, 7, 14]
    
    # Distractor operations
    calibration_set = {1, 2, 3, 4, 5}
    validation_offset = 25
    redundant_checksum = sum(range(10))  # 45
    
    # Core processing chain
    odd_readings = filter_odd_values(sensor_readings)
    core_sum = process_core_data(odd_readings)
    
    # More distractors
    backup_data = [x * 2 for x in sensor_readings[:3]]
    system_overhead = len(backup_data) * 10
    
    # Key assignment - this is the target
    final_filter_sum = core_sum + validation_offset
    processed_sum = final_filter_sum
    
    # Unused variables and operations
    diagnostic_flag = (len(sensor_readings) > 5)
    unused_buffer = bytearray(10)
    
    print(f"Result: {processed_sum}")

if __name__ == "__main__":
    main()