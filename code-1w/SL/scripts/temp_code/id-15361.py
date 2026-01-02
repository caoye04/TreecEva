from collections import Counter

def calculate_final_score():
    scores = [85, 90, 78, 92, 88]
    weightage = [0.2, 0.2, 0.1, 0.3, 0.2]
    
    # Compute weighted average
    weighted_sum = sum(score * weight for score, weight in zip(scores, weightage))
    
    # Apply performance bonus if above threshold
    bonus = 5 if weighted_sum >= 85 else 0
    
    # Count frequency of score ranges
    grade_bins = Counter('A' if s >= 90 else 'B' if s >= 80 else 'C' for s in scores)
    
    # Final adjustment based on grade distribution
    adjustment = 2 if grade_bins['A'] > 2 else -1
    
    result = weighted_sum + bonus + adjustment
    return result

# Execute and print result
target_result = calculate_final_score()
print(f"Result: {target_result}")