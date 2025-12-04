def process_data_points():
    raw_data = [42, 18, 73, 56, 29, 91, 34, 67]
    
    # Pre-processing step (distractor)
    processed_data = [x * 2 for x in raw_data if x % 2 == 0]
    temp_sum = sum(processed_data)
    
    # Main processing with list comprehension
    adjusted_values = [x % 25 for x in raw_data]
    sorted_values = sorted(adjusted_values, reverse=True)
    
    # Additional computation (semi-relevant but not used)
    average_val = sum(adjusted_values) / len(adjusted_values)
    variance = sum((x - average_val) ** 2 for x in adjusted_values)
    
    # Final result calculation
    final_score = sorted_values[0] + sorted_values[-1]
    print(f"Result: {final_score}")

process_data_points()