from collections import defaultdict

# Simulate student quiz scores with potential penalty applications
def calculate_final_score(raw_scores, deductions):
    score_map = defaultdict(int)
    for i, score in enumerate(raw_scores):
        score_map[f'student_{i}'] = score
    
    total = sum(raw_scores)
    penalty_sum = sum(d for d in deductions if d > 0)
    
    # Apply penalty only if total exceeds threshold
    if total > 200:
        total -= penalty_sum
    
    adjustment = len(raw_scores) - len(deductions)
    result = total + adjustment
    return result

scores = [78, 85, 92, 64]
penalties = [10, 5]

# Irrelevant auxiliary variable (minimal distraction)
unused_diagnostic = [x ** 2 for x in scores if x < 70]

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")