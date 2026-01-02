def calculate_performance_rating():
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(base_scores)) / (max(base_scores) - min(base_scores)) * 100) for x in base_scores]
    adjusted_weights = [w + 0.01 for w in weights][:4]  # Unused adjustment
    
    weighted_sum = 0.0
    total_weight = 0.0
    
    for i, (score, weight) in enumerate(zip(base_scores, weights)):
        if score < 80:
            continue  # Skip low scores
        weighted_sum += score * weight
        total_weight += weight
    
    # Additional logic to increase cognitive load
    penalty_factor = 0.95 if len([s for s in base_scores if s >= 90]) >= 2 else 1.0
    raw_average = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Simulate bonus for consistency (not actually affecting final logic)
    consistency_bonus = 5 if all(abs(base_scores[i] - base_scores[i+1]) < 10 for i in range(len(base_scores)-1)) else 0
    
    # Final computation
    adjusted_average = raw_average * penalty_factor
    
    # Mapping to score scale
    final_score = int(round(adjusted_average + 0.5 * consistency_bonus))
    
    # Dead code path (never executed but adds distraction)
    if False:
        fallback = sum(base_scores) / len(base_scores)
        final_score = int(fallback)
    
    return final_score

# Main execution
result = calculate_performance_rating()
print(f"Result: {result}")