def aggregate_performance(weights, scores):
    # Normalize weights using lambda and sum
    total_weight = sum(map(lambda x: x ** 0.5, weights))
    normalized = [w**0.5 / total_weight for w in weights]
    
    # Apply weight to each score
    weighted_scores = [score * norm for score, norm in zip(scores, normalized)]
    
    # Misleading intermediate: entropy calculation (not used)
    import math
    entropy = -sum(p * math.log(p) for p in normalized if p > 0)
    avg_score = sum(weighted_scores) / len(weighted_scores)
    
    # Simulate feedback adjustment with string-based flags
    adjustment_flags = ['boost', 'neutral', 'penalize']
    flag_effects = {'boost': 1.2, 'neutral': 1.0, 'penalize': 0.8}
    performance_flag = 'neutral'
    
    # Extra distraction: tuple unpacking and irrelevant grouping
    categories = ['A', 'B', 'C']
    grouped_data = [(cat, sc) for cat, sc in zip(categories, scores)]
    unpacked = [item for pair in grouped_data for item in pair]
    
    # Bitwise masking on score indices (distractor)
    masked_indices = [i ^ 3 for i in range(len(scores))]
    
    # Real computation path
    base_result = sum(weighted_scores)
    if performance_flag in flag_effects:
        adjusted_result = base_result * flag_effects[performance_flag]
    else:
        adjusted_result = base_result
    
    # Final nonlinear transformation
    final_result = int(round(adjusted_result ** 1.1))
    
    return final_result

# Input data
feedback_weights = [8, 2, 5]
raw_scores = [75, 88, 92]

# Dead code path - never executed but looks relevant
if False:
    raw_scores = sorted(raw_scores, reverse=True)
    feedback_weights = [w + 1 for w in feedback_weights]

# Core execution
final_score = aggregate_performance(feedback_weights, raw_scores)
print(f"Result: {final_score}")