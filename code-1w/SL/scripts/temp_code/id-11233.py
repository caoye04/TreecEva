def calculate_final_score(scores, penalties):
    total_score = sum(scores)
    adjustment = 0
    
    # Apply penalty only if score exceeds threshold
    if total_score > 50:
        for i, penalty in enumerate(penalties):
            adjustment += penalty * (i + 1)
    
    # Irrelevant distraction: unused variable
    temp_debug = [x * 2 for x in scores]
    
    final_multiplier = 1.1 if total_score > 60 else 1.0
    raw_result = (total_score - adjustment) * final_multiplier
    result = int(raw_result)
    
    return result

# Input data
scores = [10, 15, 12, 8, 9]
penalties = [3, 1, 4]

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")