def analyze_data_scores(raw_data):
    # Process raw data scores
    cleaned_data = [score for score in raw_data if score > 0]
    
    # Calculate some intermediate metrics (distractor operations)
    data_sum = sum(cleaned_data)
    data_avg = data_sum / len(cleaned_data) if cleaned_data else 0
    
    # Apply slicing operations to focus on specific segments
    middle_segment = cleaned_data[1:-1] if len(cleaned_data) > 2 else cleaned_data
    
    # Calculate processing metrics
    max_val = max(middle_segment) if middle_segment else 0
    min_val = min(middle_segment) if middle_segment else 0
    
    # Range calculation (distractor - not used in final result)
    data_range = max_val - min_val
    
    # Process values with transformation
    processed_values = [val * 2 + 5 for val in middle_segment]
    
    # Calculate adjustment factor based on data properties
    adjustment_factor = (len(processed_values) % 4) + 1
    
    # Final computation using the last processed value
    final_score = processed_values[-1] * adjustment_factor
    
    print(f"Result: {final_score}")
    return final_score

# Test data
performance_scores = [15, 8, 22, 17, 9, 25, 11]
result = analyze_data_scores(performance_scores)