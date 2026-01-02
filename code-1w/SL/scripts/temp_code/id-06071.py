from collections import defaultdict

# Simulate student quiz scoring with penalty adjustments
def calculate_final_score(raw_scores, deductions):
    score_counter = defaultdict(int)
    for subject, score in raw_scores.items():
        score_counter[subject] += score
    
    total = sum(score_counter.values())
    adjustment = sum(deductions) if deductions else 0
    
    # Apply logical condition to cap adjustment impact
    cap_limit = 20
    effective_adjustment = adjustment if abs(adjustment) <= cap_limit else (cap_limit if adjustment > 0 else -cap_limit)
    
    final_multiplier = 1.1 if total > 250 else 1.0
    intermediate = total - effective_adjustment
    result = intermediate * final_multiplier
    
    # Irrelevant distraction: unused variable
    temp_debug_log = f'Final adjustment: {effective_adjustment}'
    
    return int(result)

# Input data
scores = {'math': 95, 'physics': 88, 'chemistry': 75, 'biology': 64}
penalties = [-5, -3, -2]

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")