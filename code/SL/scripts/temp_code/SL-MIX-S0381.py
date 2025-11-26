def process_operations(data_stream):
    irrelevant_counter = 0
    misleading_sum = 0
    temp_storage = []
    
    # Distractor operations - misleading calculations
    for i, val in enumerate(data_stream):
        misleading_sum += val * 2  # Irrelevant multiplication
        irrelevant_counter += i // 3  # Dead code path
        temp_storage.append(val + 5)  # Unused storage
    
    # Actual processing with lambda and zip
    data_pairs = list(zip(data_stream, data_stream[1:]))
    operation = lambda x, y: (x & y) | (x ^ y)  # Bitwise operations
    
    # More distractors
    fake_metric = sum(temp_storage) - misleading_sum  # Never used
    dead_branch = misleading_sum % 7  # Unused calculation
    
    # Core logic with conditional branches
    processed_values = []
    for idx, (a, b) in enumerate(data_pairs):
        if idx % 2 == 0:
            result = operation(a, b)
            if result > 15:  # Nested condition
                processed_values.append(result - 8)
            else:
                processed_values.append(result + 3)
        else:
            # Misleading alternate path
            processed_values.append((a | b) + misleading_sum // 10)
    
    # Final accumulation
    final_result = sum(processed_values)
    
    # Final distractions
    unused_calculation = final_result * 2 - misleading_sum
    irrelevant_transform = [x ** 2 for x in temp_storage]
    
    return final_result

# Initialize data stream
data_stream = [12, 7, 25, 18, 9, 14, 21, 6]

# Execute main processing
final_metric = process_operations(data_stream)

# Print result
print(f"Result: {final_metric}")