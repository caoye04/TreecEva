def calculate_performance_metric():
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.2, 0.15, 0.25, 0.2]
    
    # Irrelevant distraction: unused variable
    max_possible = max(base_scores)
    
    # Weighted score computation using list comprehension
    weighted_scores = [score * weight for score, weight in zip(base_scores, weights)]
    
    # Compute average as performance metric
    average_score = sum(weighted_scores)
    
    # Conditional adjustment based on threshold
    bonus = 5 if average_score >= 85 else 0
    
    # Final performance score with bonus
    final_score = average_score + bonus
    
    return final_score

# Entry point
target_result = calculate_performance_metric()
print(f"Result: {target_result}")