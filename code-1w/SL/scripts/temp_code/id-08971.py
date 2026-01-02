def calculate_performance(data_map):
    base_offset = 17
    temp_result = 0
    final_score = 0
    
    # Irrelevant preprocessing: case conversion tracking
    case_tracker = {'upper': 0, 'lower': 0}
    for key in data_map.keys():
        if isinstance(key, str):
            if key.isupper():
                case_tracker['upper'] += 1
            elif key.islower():
                case_tracker['lower'] += 1

    # Distractor: unused transformation matrix
    transform_matrix = [[i * 2 + j for j in range(3)] for i in range(3)]
    dummy_accumulator = 0
    for row in transform_matrix:
        for val in row:
            dummy_accumulator += val % 4

    # Core logic: enumeration and conditional processing
    multiplier = len(data_map.get('config', [1, 1]))
    index_shift = data_map.get('shift', 5)

    values = data_map.get('sequence', [])
    for i, value in enumerate(values):
        if i % 2 == 0 and value > 0:
            temp_result += value * (i + 1)
        elif i % 2 == 1:
            temp_result -= (value // 2)

    # Secondary path: zipped analysis of metadata
    meta_a = data_map.get('factors', [1, 1, 1])
    meta_b = data_map.get('weights', [2, 2, 2])
    zip_correction = 0
    for a, b in zip(meta_a, meta_b):
        zip_correction += a * b

    # Final composition with offset and multiplier
    final_score = temp_result + base_offset
    final_score = (final_score * multiplier) - index_shift + zip_correction

    # Dead code branch: never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f"Debug: {case_tracker}, {dummy_accumulator}")

    return final_score

# Main execution
benchmark_data = {
    'sequence': [4, -6, 8, -2, 10],
    'config': [1, 2],
    'shift': 3,
    'factors': [3, 4],
    'weights': [2, 5],
    'threshold': 0.5,
    'mode': 'performant'
}

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")