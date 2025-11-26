def analyze_performance(data_points):
    baseline = 42
    processed_data = []
    
    for value in data_points:
        if value % 2 == 0:
            processed_value = value * 3 - 5
        else:
            processed_value = value + 7
        processed_data.append(processed_value)
    
    # Distractor operations that don't affect final result
    temp_sum = sum(processed_data[:2])
    average_temp = temp_sum / 2
    
    adjustment_factor = len(processed_data) // 2
    
    # More distractor calculations
    max_val = max(processed_data)
    min_val = min(processed_data)
    range_val = max_val - min_val
    
    final_score = processed_data[2] * adjustment_factor
    
    # Final verification (distractor)
    verification_check = final_score > 50
    
    print(f"Result: {final_score}")
    return final_score

# Main execution
performance_data = [12, 8, 15, 6, 9]
result = analyze_performance(performance_data)