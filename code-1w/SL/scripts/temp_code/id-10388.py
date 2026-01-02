from itertools import compress

def calculate_performance_metric():
    # Sensor data replaced with employee performance metrics to avoid recent themes
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.25, 0.15, 0.3, 0.1]
    
    # Normalize weights to ensure they sum to 1.0
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Compute weighted score using zip and list comprehension
    weighted_scores = [score * weight for score, weight in zip(base_scores, normalized_weights)]
    avg_score = sum(weighted_scores)
    
    # Additional logic: bonus if all scores above threshold
    all_above_threshold = all(score >= 75 for score in base_scores)
    bonus = 5 if all_above_threshold else 0
    
    # Use enumerate to adjust score based on position (e.g., recent performance emphasis)
    for i, score in enumerate(base_scores):
        if i >= 3:  # Recent two evaluations get slight boost
            avg_score += score * 0.02
    
    final_score = avg_score + bonus
    return final_score

# Irrelevant utility function (minimal interference)
def unused_helper():
    return "This is not used"

# Main execution
result = calculate_performance_metric()
print(f"Result: {result}")