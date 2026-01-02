from collections import defaultdict

def calculate_final_score():
    # Simulate student quiz scores with retries
    scores = [85, 90, 78, 92]
    attempts = [1, 2, 1, 3]
    
    # Weighted score based on attempt number
    weighted_map = defaultdict(float)
    for i, score in enumerate(scores):
        penalty = 0.95 ** (attempts[i] - 1)
        weighted_map[i] = score * penalty
    
    # Boost if average improvement across attempts
    improvements = []
    temp_scores = [85, 78, 90, 78, 92]  # flattened timeline of submissions
    for j in range(1, len(temp_scores)):
        if temp_scores[j] > temp_scores[j-1]:
            improvements.append(True)
    
    base_avg = sum(weighted_map.values()) / len(weighted_map)
    bonus = 2.5 if len(improvements) > 3 else 0
    
    final_adjustment = base_avg + bonus
    result = int(round(final_adjustment))
    return result

# Execute and print result
target_variable = calculate_final_score()
print(f"Result: {target_variable}")