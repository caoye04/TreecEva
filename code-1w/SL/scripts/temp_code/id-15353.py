from itertools import compress

def calculate_final_score():
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.2, 0.1, 0.3, 0.2]
    
    # Apply modular arithmetic to normalize scores above 80
    adjusted_scores = [(score % 100) + 1 for score in base_scores]
    
    # Use conditional expression to boost low performers
    boosted_scores = [s + 5 if s < 85 else s for s in adjusted_scores]
    
    # Compute weighted sum using element-wise multiplication
    weighted_sum = sum(w * s for w, s in zip(weights, boosted_scores))
    
    # Final adjustment based on pass threshold
    result = weighted_sum if weighted_sum >= 90 else weighted_sum - 5
    
    return result

# Irrelevant utility variable (minor distraction)
dummy_flag = True

result = calculate_final_score()
print(f"Result: {result}")