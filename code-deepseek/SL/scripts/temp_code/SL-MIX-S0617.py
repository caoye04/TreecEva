def calculate_performance_metrics(scores):
    base_total = sum(scores)
    average_score = base_total / len(scores)
    
    # Distractor: calculate median but don't use it
    sorted_scores = sorted(scores)
    mid = len(sorted_scores) // 2
    median_score = (sorted_scores[mid] + sorted_scores[~mid]) / 2
    
    # Distractor: complex operation that gets discarded
    weighted_sum = sum(score * (i + 1) for i, score in enumerate(scores))
    
    # Relevant operations
    performance_map = {score: idx for idx, score in enumerate(sorted_scores)}
    primary_metric = performance_map.get(max(scores), 0)
    
    # More distractors
    adjustment_factor = len([s for s in scores if s > 50])
    unused_calc = (base_total ^ adjustment_factor) & 0xFF
    
    # Final relevant calculations
    weight_factor = 3
    bonus_adjustment = 15
    final_score = primary_metric * weight_factor + bonus_adjustment
    
    print(f"Result: {final_score}")
    return final_score

# Test data
student_scores = [78, 92, 85, 67, 94, 88]
calculate_performance_metrics(student_scores)