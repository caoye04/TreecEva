from collections import defaultdict

# Simulate student quiz scores with potential penalty applications
def calculate_final_score(raw_scores, deductions):
    score_counter = defaultdict(int)
    for subject, score in raw_scores.items():
        score_counter[subject] += score
    
    total = sum(score_counter.values())
    penalty_sum = sum(deductions)
    
    # Apply conditional adjustment based on performance threshold
    adjustment = -5 if total < 60 else 10
    
    result = total - penalty_sum + adjustment
    return result

# Input data
scores = {'math': 25, 'physics': 30, 'chemistry': 20}
penalties = [5, 3, 2]

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")