import itertools

def compute_final_value():
    data_points = [2, 5, 8, 3, 7]
    threshold = 6
    intermediate_sum = 0
    filtered_values = []
    
    # Distractor computation that doesn't affect final result
    potential_offset = sum([x * 2 for x in data_points if x % 2 == 0])
    
    # Main logic - filter and process values
    for val in data_points:
        if val > threshold:
            filtered_values.append(val)
            intermediate_sum += val
    
    # Additional distractor operation
    temp_product = 1
    for i in range(len(filtered_values)):
        temp_product *= filtered_values[i] + 1
    
    # Core computation using itertools
    combinations = list(itertools.combinations(filtered_values, 2))
    pair_sums = [sum(pair) for pair in combinations]
    
    final_result = max(pair_sums) if pair_sums else 0
    
    # Unused variable that seems relevant
    average_filtered = sum(filtered_values) / len(filtered_values) if filtered_values else 0
    
    return final_result

final_solution = compute_final_value()
print(f"Result: {final_solution}")