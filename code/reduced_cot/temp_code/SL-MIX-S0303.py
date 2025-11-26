def result_comparison(values):
    threshold_check = lambda x: x > 15
    filtered_count = len(list(filter(threshold_check, values)))
    
    # Some basic data processing
    total_points = len(values)
    ratio_calc = filtered_count / total_points if total_points > 0 else 0
    
    # Comparison operations
    meets_criteria = filtered_count >= 3
    base_score = 25 if meets_criteria else 10
    
    # Final adjustment
    adjustment = ratio_calc * 5
    final_score = base_score + adjustment
    
    return int(final_score)

data_points = [8, 22, 14, 19, 11, 25, 17]
final_value = result_comparison(data_points)
print(f"Target result: {final_value}")