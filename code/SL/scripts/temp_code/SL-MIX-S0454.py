def process_data_points():
    data_sources = [(3, 7), (1, 9), (5, 2), (8, 4)]
    processed_values = []
    temp_buffer = []
    
    for idx, (x, y) in enumerate(data_sources):
        product = x * y
        processed_values.append(product)
        # Distractor computation that doesn't affect final result
        temp_buffer.append(idx + product % 3)
    
    # Distractor operation with zip that looks relevant but isn't used
    zipped_pairs = list(zip(processed_values, temp_buffer))
    
    # Another distractor - tuple operations that don't contribute to answer
    coordinate_tuples = [(val, idx) for idx, val in enumerate(processed_values)]
    
    enumerated_values = []
    for index, value in enumerate(processed_values):
        enumerated_values.append(value + index)
    
    # Distractor: calculate average but don't use it
    avg_value = sum(enumerated_values) / len(enumerated_values)
    
    # The key computation that determines the answer
    final_computation = max(enumerated_values) - min(enumerated_values)
    
    # Distractor: unused combination count
    unused_count = len(set(enumerated_values))
    
    print(f"Target result: {final_computation}")
    return final_computation

if __name__ == "__main__":
    result = process_data_points()