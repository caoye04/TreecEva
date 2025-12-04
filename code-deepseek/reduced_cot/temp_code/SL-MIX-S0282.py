def calculate_performance_metrics():
    # Student assessment data
    raw_scores = [85, 92, 78, 96, 88, 74, 91, 83, 95, 79]
    
    # Filter scores above threshold
    threshold = 80
    filtered_scores = [score for score in raw_scores if score >= threshold]
    
    # Calculate statistics (distractor operations)
    temp_max = max(filtered_scores)
    temp_min = min(filtered_scores)
    temp_range = temp_max - temp_min
    
    # Sort and select relevant subset
    sorted_scores = sorted(filtered_scores)
    critical_index = len(sorted_scores) // 2 - 1
    
    # Adjustment calculations
    base_adjustment = 5
    score_variance = temp_range // 4
    adjustment_factor = base_adjustment - score_variance
    
    # Unused intermediate calculation
    hypothetical_bonus = (temp_max + temp_min) // 10
    
    # Final score determination
    final_score = sorted_scores[critical_index] + adjustment_factor
    
    print(f"Target result: {final_score}")

calculate_performance_metrics()