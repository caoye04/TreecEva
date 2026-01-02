def calculate_final_score(scores, penalties):
    total_score = sum(scores)
    deduction = sum(penalties) if len(penalties) > 0 else 0
    adjusted = total_score - deduction
    result = adjusted * (1.0 + 0.1 * (len(scores) > 5))
    return result

# Simulate competition round scores
scores = [88, 92, 76, 94, 85, 90]
penalties = [5, 3]

# Irrelevant auxiliary data (minimal distraction)
temp_data = [x * 2 for x in scores if x < 80]
label_prefix = "ROUND_"

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")