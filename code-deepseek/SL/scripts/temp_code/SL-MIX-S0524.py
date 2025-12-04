def compute_final_score(performance_data, bonus_threshold):
    # Process performance metrics
    base_scores = [entry['score'] for entry in performance_data]
    max_score = max(base_scores)
    min_score = min(base_scores)
    
    # Calculate weighted average with bonus consideration
    weighted_sum = sum(score * (index + 1) for index, score in enumerate(base_scores))
    total_weight = sum(range(1, len(base_scores) + 1))
    weighted_avg = weighted_sum / total_weight
    
    # Apply bonus multiplier (distractor - not used in final result)
    bonus_multiplier = 1.5 if weighted_avg > bonus_threshold else 1.0
    
    # Calculate score range and final adjustment
    score_range = max_score - min_score
    range_adjustment = score_range * 0.1  # Distractor calculation
    
    # Final result calculation (ignores bonus and range adjustment)
    performance_ratio = weighted_avg / max_score
    final_score = int(performance_ratio * 100)
    
    return final_score

# Input data
performance_data = [
    {'score': 85, 'category': 'technical'},
    {'score': 92, 'category': 'analytical'},
    {'score': 78, 'category': 'creative'},
    {'score': 88, 'category': 'collaborative'}
]

bonus_threshold = 85

# Main execution
final_result = compute_final_score(performance_data, bonus_threshold)
print(f"Result: {final_result}")