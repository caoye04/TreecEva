from itertools import compress

def calculate_final_score(raw_scores, deductions):
    # Filter scores above threshold using slicing and boolean mask
    passing_scores = raw_scores[2:]
    valid_mask = [score >= 50 for score in passing_scores]
    filtered_scores = list(compress(passing_scores, valid_mask))
    
    # Apply modular arithmetic to wrap penalty values
    total_deduction = sum(d % 7 for d in deductions)
    base_score = sum(filtered_scores)
    
    # Final adjustment based on number of valid scores
    if len(filtered_scores) > 2:
        base_score -= total_deduction
    else:
        base_score += 10
        
    result = base_score % 1000
    return result

# Input data
scores = [45, 52, 67, 89, 41, 73]
penalties = [12, 25, 8, 19]

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")