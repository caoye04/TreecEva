from itertools import compress

def calculate_final_score(marks, weights):
    # Normalize weights to sum to 1.0
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Determine which marks are above passing threshold
    passing_threshold = 50
    passed = [mark >= passing_threshold for mark in marks]
    
    # Use only marks from passed subjects for weighted average
    valid_marks = list(compress(marks, passed))
    valid_weights = list(compress(normalized_weights, passed))
    
    # If no subject is passed, return 0
    if not valid_marks:
        return 0
    
    # Compute weighted score
    weighted_score = sum(m * w for m, w in zip(valid_marks, valid_weights))
    
    # Apply bonus if all subjects passed
    perfect_pass = all(passed)
    bonus = 5.0 if perfect_pass else 0.0
    
    final_score = weighted_score + bonus
    return final_score

# Input data
marks = [78, 85, 45, 90]
weights = [0.2, 0.3, 0.1, 0.4]

# Execution point
final_score = calculate_final_score(marks, weights)
print(f"Result: {final_score}")