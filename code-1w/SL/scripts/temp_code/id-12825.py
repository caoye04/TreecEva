def calculate_final_score(scores, penalties):
    base_score = sum(scores)
    penalty_deduction = sum(penalties) * 0.5
    adjusted_score = base_score - penalty_deduction
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_log = [f'Entry_{i}' for i in range(len(scores))]
    
    # Apply bonus if performance is high using conditional expression
    bonus = 10 if adjusted_score > 75 else 0
    final_multiplier = (lambda x: 1.1 if x > 90 else 1.0)(base_score)
    
    result = adjusted_score + bonus
    result *= final_multiplier
    return round(result, 2)

# Input data
scores = [85, 78, 92]
penalties = [4, 6]

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")