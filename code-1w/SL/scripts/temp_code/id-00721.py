def process_scores(scores, weights):
    weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
    total_weight = sum(weights)
    normalized = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Irrelevant distraction: unused calculation
    avg_score = sum(scores) / len(scores) if scores else 0
    
    # Key computation
    bonus = 5 if normalized > 80 else 2
    result = normalized + bonus
    return result

# Input data
scores = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.1, 0.4]

# Execute
result = process_scores(scores, weights)
print(f"Target result: {result}")