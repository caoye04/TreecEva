def analyze_data(values, threshold):
    # Calculate statistics
    total_sum = sum(values)
    max_val = max(values)
    min_val = min(values)
    
    # Filter values above threshold
    filtered = [x for x in values if x > threshold]
    filtered_count = len(filtered)
    
    # Calculate weighted score (distractor - not used in final result)
    weight_factor = max_val - min_val
    weighted_score = total_sum * weight_factor
    
    # Set operations to find unique patterns
    unique_values = set(values)
    pattern_count = len(unique_values)
    
    # Final calculation (this is the actual logic)
    if filtered_count > 0:
        avg_filtered = sum(filtered) / filtered_count
        final_score = avg_filtered * pattern_count
    else:
        final_score = pattern_count * 2.5
    
    # Distractor operation that doesn't affect result
    temp_adjustment = final_score + weight_factor
    
    return final_score

data_values = [15, 30, 45, 20, 35, 25, 40]
result = analyze_data(data_values, threshold=25)
final_score = result
print(f"Result: {final_score}")