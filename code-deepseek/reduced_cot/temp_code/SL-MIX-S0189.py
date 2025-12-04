def process_data(data_list):
    # Misleading variable - never actually used
    initial_offset = 37
    processing_factor = lambda x: (x * 3 - 7) if x % 2 == 0 else (x * 2 + 5)
    
    # Dead code path - never called
    unused_function = lambda y: y ** 2 + y * 3 - 10
    
    temp_results = []
    for item in data_list:
        # Irrelevant intermediate calculation
        intermediate = item + initial_offset - 15
        
        if item > 0:
            processed = processing_factor(item)
            temp_results.append(processed)
        else:
            # This branch is never taken in actual execution
            negative_result = item * 2 - 8
            temp_results.append(negative_result)
    
    # Misleading calculation that gets discarded
    distraction_sum = sum(temp_results) + 42
    
    # Actual relevant processing
    filtered_data = [x for x in temp_results if x > 10]
    result_value = sum(filtered_data) if filtered_data else 0
    
    return result_value

# Main execution with distractions
data_collection = [4, 7, 2, 9, 5]

# Irrelevant variable that creates confusion
processing_threshold = 15

# Dead assignment that never affects the result
setup_config = {'mode': 'advanced', 'limit': 100}

# Key execution point
items_to_process = [x for x in data_collection if x < 8]
result = process_data(items_to_process)

# More distractions
secondary_processing = lambda a, b: a * b - 25
redundant_check = secondary_processing(10, 3)

# Final answer variable
final_output = result + 3

print(f"Target result: {final_output}")