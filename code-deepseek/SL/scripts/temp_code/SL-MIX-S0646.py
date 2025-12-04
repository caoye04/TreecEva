def process_set_data(data_items, threshold):
    # Distractor: misleading intermediate computation
    temp_sum = sum(range(10, 20)) + len(data_items) * 5
    
    # Relevant processing
    valid_items = {item for item in data_items if item > threshold}
    
    # More distractions
    unused_operation = temp_sum // 3 + 7
    secondary_set = {x * 2 for x in data_items if x % 3 == 0}
    
    # Dead code path that looks relevant
    if len(valid_items) > 5:
        redundant_calc = max(valid_items) - min(valid_items)
    else:
        redundant_calc = sum(valid_items) * 2
    
    # Key operation with set operations
    if len(valid_items) > 0:
        union_set = valid_items.union({threshold * 2, threshold + 1})
        intersection_set = union_set.intersection({x for x in range(15, 25)})
        result = sum(intersection_set) - len(union_set)
    else:
        result = threshold * 3 - 5
    
    return result

# Main execution with distractions
initial_data = [8, 12, 18, 22, 25, 30, 35]
filter_threshold = 15

# Irrelevant computations that look important
dummy_var = (len(initial_data) ** 2) + 10
intermediate_result = sum(initial_data[:3]) - min(initial_data)

# The critical execution point
final_output = process_set_data(initial_data, filter_threshold)

# More distractions after the answer is computed
post_computation = [x + 1 for x in initial_data if x < final_output]
final_check = len(set(post_computation)) - len(initial_data)

print(f"Target result: {final_output}")