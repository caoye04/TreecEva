def calculate_performance(scores):
    processed_data = {}
    total_sum = sum(scores)
    score_count = len(scores)
    
    # Distractor calculations that don't affect final result
    bonus_points = score_count * 2
    penalty = total_sum % 10
    intermediate = bonus_points - penalty
    
    # Relevant operations for final result
    processed_data['average'] = total_sum / score_count
    processed_data['range'] = max(scores) - min(scores)
    
    # More distractor operations
    temp_adjustment = processed_data['range'] * 0.1
    adjusted_avg = processed_data['average'] + temp_adjustment
    
    # Core calculation
    aggregate_factor = (total_sum // score_count) + (score_count % 5)
    processed_data['aggregate'] = aggregate_factor * 3
    
    # Final assignment
    final_score = processed_data['aggregate']
    
    # Print result
    print(f"Result: {final_score}")
    return final_score

# Test data
performance_scores = [85, 92, 78, 96, 88]
calculate_performance(performance_scores)