def calculate_final_score(scores, penalties):
    total_score = sum(scores)
    penalty_deduction = sum(penalties) % 7
    
    # Apply modular arithmetic to cap penalty impact
    adjusted_total = total_score - penalty_deduction
    
    # Use list comprehension to identify high scores
    high_performers = [s for s in scores if s >= 80]
    bonus = len(high_performers) * 2
    
    final_multiplier = 1.1 if len(high_performers) > 2 else 1.0
    result = (adjusted_total + bonus) * final_multiplier
    return int(result)

# Input data
scores = [85, 92, 78, 96, 88]
penalties = [3, 5, 2, 8]

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")