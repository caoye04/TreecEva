def calculate_final_score(raw_data, limit):
    # Preprocessing: filter and transform data
    valid_entries = [x for x in raw_data if isinstance(x, int) and x > 0]
    squared_values = [x**2 for x in valid_entries]
    
    # Irrelevant intermediate computation (distractor)
    average_value = sum(valid_entries) / len(valid_entries) if valid_entries else 0
    temp_result = [y for y in squared_values if y < 1000]  # Not used later
    
    # Core logic with conditional filtering and aggregation
    filtered_set = {z for z in squared_values if z > limit}
    if len(filtered_set) == 0:
        return 0
    
    max_val = max(filtered_set)
    min_val = min(filtered_set)
    range_val = max_val - min_val
    
    # Secondary distractor: unused statistical calculation
    mean_sqr = sum(squared_values) / len(squared_values) if squared_values else 0
    deviation_sum = sum((v - mean_sqr)**2 for v in squared_values)  # Dead-end path
    
    # Final score computation based on range and size
    size_factor = len(filtered_set)
    final_score = range_val + size_factor * 2
    
    # Early return alternative not taken
    if limit < 0:
        return -1
    
    return final_score

# Main execution
raw_dataset = [3, -2, 5, 0, 'x', 4, 6, 8]
threshold = 20

# Extraneous variable assignments (distractors)
processed_copy = [i*2 for i in raw_dataset if type(i) == int]
duplicate_filter = set(processed_copy)
useless_total = sum(x for x in processed_copy if x < 10)

final_score = calculate_final_score(raw_dataset, threshold)
print(f"Target result: {final_score}")