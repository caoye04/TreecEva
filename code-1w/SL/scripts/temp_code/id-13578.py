from itertools import compress

def calculate_final_score(scores, penalties):
    # Apply penalty mask: only penalize scores above threshold
    threshold = 75
    high_performers = [s > threshold for s in scores]
    
    # Use bitwise XOR to toggle penalty application every other high performer
    toggle_pattern = [i % 2 == 0 for i in range(len(high_performers))]
    effective_penalty = [p if h ^ t else 0 for h, t, p in zip(high_performers, toggle_pattern, penalties)]
    
    # Compute base total using list comprehension
    base_total = sum([s * 1.1 for s in scores])
    
    # Subtract cumulative effective penalties
    final_deduction = sum(effective_penalty)
    result = base_total - final_deduction
    
    # Irrelevant distraction: unused variable (minimal interference)
    debug_info = list(zip(scores, high_performers, effective_penalty))
    
    return result

# Input data
scores = [80, 92, 67, 90, 70]
penalties = [5, 3, 0, 2, 4]

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")