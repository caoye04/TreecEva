def calculate_performance():
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    weighted_scores = [base_scores[i] * weights[i] for i in range(len(base_scores))]
    
    # Apply bonus if average exceeds threshold
    avg_score = sum(weighted_scores) / len(weighted_scores)
    bonus = 5 if avg_score >= 85 else 0
    
    adjusted_scores = [score + bonus for score in weighted_scores]
    final_score = max(adjusted_scores)
    
    # Irrelevant tracking variable (minimal interference)
    total_processed = len(base_scores)
    
    print(f"Result: {final_score}")
    
    return final_score

result = calculate_performance()