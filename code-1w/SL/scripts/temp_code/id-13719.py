def calculate_final_score(scores, penalties):
    total_score = sum(scores)
    penalty_deduction = 0
    
    # Apply penalties using integer division and rounding logic
    for i, penalty in enumerate(penalties):
        if i % 2 == 0:
            penalty_deduction += penalty // 2
        else:
            penalty_deduction += round(penalty * 0.75)
    
    # Use slicing to only consider top 4 scores
    top_scores = sorted(scores, reverse=True)[:4]
    base_value = sum(top_scores)
    
    # Combine base value with penalty adjustment
    final_adjustment = base_value - penalty_deduction
    result = final_adjustment + (len(scores) > len(penalties))
    return result

# Input data
scores = [88, 92, 76, 94, 85]
penalties = [10, 8, 12]

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")