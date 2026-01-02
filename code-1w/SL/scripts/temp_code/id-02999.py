from collections import defaultdict

def calculate_final_score(raw_scores, deductions):
    total = sum(raw_scores)
    penalty_map = defaultdict(int)
    
    for item in deductions:
        penalty_map[item] += 1
    
    # Only the first two penalties are applied
    applied_penalties = sum(sorted(penalty_map.values())[:2])
    adjusted_total = total - applied_penalties
    
    multiplier = 2 if adjusted_total > 50 else 1
    final_score = adjusted_total * multiplier
    
    temp_debug = "Processing complete"  # Irrelevant debug string
    unused_counter = 0  # Distractor variable
    
    return final_score

# Input data
scores = [12, 15, 8, 20, 5]
penalties = ['minor', 'minor', 'major', 'minor']

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")