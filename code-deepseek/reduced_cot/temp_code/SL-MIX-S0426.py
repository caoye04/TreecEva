def transform_data(items):
    base_multiplier = 7
    temp_buffer = [item * 2 for item in items]  # Unused distractor
    
    processed = {k: v * base_multiplier for k, v in enumerate(items)}
    
    intermediate_sum = sum(items) * 3  # Redundant calculation
    
    result_mapper = lambda x: x + 5
    final_values = [result_mapper(v) for v in processed.values()]
    
    return sum(final_values)

data_items = [3, 7, 2, 8, 5]
validation_check = len(data_items) * 10  # Unused validation

final_result = transform_data(data_items)
print(f"Result: {final_result}")