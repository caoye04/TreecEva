def analyze_performance(feedback_stream):
    base_weights = [0.1, 0.2, 0.3, 0.4]
    raw_scores = [max(1, min(10, x)) for x in feedback_stream if isinstance(x, int)]
    valid_count = len(raw_scores)
    
    if valid_count < 3:
        return 0
    
    filtered_ratings = [score for score in raw_scores if score >= 5]
    adjustment_factor = 1.5 if len(filtered_ratings) > 4 else 1.0
    adaptive_weights = [w * adjustment_factor for w in base_weights[:len(filtered_ratings)]]
    
    # Normalize weights if they exist
    total_weight = sum(adaptive_weights)
    if total_weight > 0:
        adaptive_weights = [w / total_weight for w in adaptive_weights]
    
    threshold_score = filtered_ratings and sum(rating * weight for rating, weight in zip(filtered_ratings, adaptive_weights)) / len(filtered_ratings)
    
    extra_buffer = [0] * (valid_count - len(filtered_ratings))
    cleanup_flag = False
    
    return threshold_score

result = analyze_performance([7, 8, 4, 9, 6, 5, 10, 3])
print(f"Result: {result}")