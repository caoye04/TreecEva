def transformation_func(data):
    process_lambda = lambda x: (x * 3) // 2
    processed = [process_lambda(val) for val in data]
    
    # Distractor operations
    temp_sum = sum(processed)
    avg_check = temp_sum // len(processed) if processed else 0
    
    # Intermediate unused computations
    unused_mult = [x * 2 for x in processed]
    verification_step = len(unused_mult) * 10
    
    # Key calculation
    result = sum(processed) % 17
    return result

initial_data = [8, 15, 23, 42, 11]

# Processing chain with some irrelevant steps
filtered_values = [x for x in initial_data if x > 10]
intermediate_check = len(filtered_values) * 5
placeholder_map = {x: x % 7 for x in filtered_values}

# Semi-relevant but unused calculation
backup_calc = (intermediate_check + 3) ^ 5

final_output = transformation_func(filtered_values)
print(f"Target result: {final_output}")