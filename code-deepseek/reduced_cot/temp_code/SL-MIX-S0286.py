def analyze_data_patterns(input_data, target_range):
    # Irrelevant analysis that doesn't affect final result
    temp_sum = sum(x * 2 for x in input_data if x > 5)
    filtered_data = [x for x in input_data if x % 2 == 0]
    
    # Misleading computation path
    dummy_calc = len(input_data) * 3.14159
    
    # Actual relevant logic
    valid_entries = [x for x in input_data if target_range[0] <= x <= target_range[1]]
    weighted_sum = sum(idx * val for idx, val in enumerate(valid_entries))
    
    # More distractions
    unused_result = max(input_data) - min(input_data)
    
    return weighted_sum

def compute_final_score(data_sequence, threshold):
    # Setup initial parameters
    base_score = 42
    multiplier = 3
    
    # Distractor operations
    fake_calculation = (base_score * 2) // 7
    misleading_value = threshold * fake_calculation
    
    # Core logic with zip and enumerate
    processed_data = []
    for idx, (a, b) in enumerate(zip(data_sequence[:-1], data_sequence[1:])):
        if a + b > threshold:
            processed_data.append((idx, a - b))
    
    # More irrelevant computations
    dead_code_path = sum(x for x in range(10) if x % 3 == 0)
    
    # Actual result computation
    if processed_data:
        final_value = sum(val * idx for idx, val in processed_data)
        result = final_value + base_score
    else:
        result = base_score * multiplier
    
    # Final distraction
    unused_metric = len(data_sequence) * threshold
    
    return result

# Main execution
input_values = [8, 12, 5, 18, 3, 15, 7, 20]
range_boundaries = (10, 25)
threshold_value = 20

# Call the main function
final_result = compute_final_score(input_values, threshold_value)

# Print the result
print(f"Result: {final_result}")