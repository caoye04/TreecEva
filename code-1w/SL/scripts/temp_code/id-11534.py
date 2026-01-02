def calculate_final_score(values, deductions):
    total = sum(values)
    adjusted = total // len(values)  # Integer division
    
    # Apply penalty reductions using slicing on first half
    relevant_deductions = deductions[:len(deductions)//2]
    penalty_cut = sum(relevant_deductions) * 0.1
    
    # Use enumerate to find high-value indices and adjust
    bonus = 0
    for i, val in enumerate(values):
        if val > 80 and i % 2 == 0:
            bonus += 5
    
    final_score = adjusted - int(penalty_cut) + bonus
    return final_score

# Input data
scores = [75, 82, 90, 65, 88, 92]
penalties = [10, 20, 30, 40]

# Calculation
result = calculate_final_score(scores, penalties)
print(f"Result: {result}")