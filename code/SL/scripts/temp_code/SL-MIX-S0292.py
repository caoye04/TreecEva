def process_data(items):
    temp_storage = {}
    preliminary_sum = 0
    processed_values = []
    
    for idx, value in enumerate(items):
        if value % 2 == 0:
            processed_values.append(value * 2)
            temp_storage[f'key_{idx}'] = value + 10
        else:
            processed_values.append(value // 2)
            preliminary_sum += value
    
    intermediate_calc = sum(processed_values) + len(temp_storage)
    
    # Distractor operations that don't affect final result
    dummy_operation = preliminary_sum * 3
    unused_mapping = {k: v * 2 for k, v in temp_storage.items()}
    
    final_count = intermediate_calc % 17
    return final_count

data_items = [8, 3, 12, 5, 9, 14]
result = process_data(data_items)
print(f"Result: {result}")