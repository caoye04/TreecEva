def calculate_final_score(values, deductions):
    adjustment_factor = 0.9
    weighted_scores = list(map(lambda x: x * adjustment_factor, values))
    total_score = sum(weighted_scores)
    penalty_sum = sum(d for d in deductions if d > 5)  # Only significant penalties applied
    total_score -= penalty_sum
    return int(total_score)

# Simulate student assessment scores and penalties
scores = [88, 92, 76, 94, 85]
penalties = [3, 7, 2, 10]
metadata = {'version': '1.2', 'active': True}  # Irrelevant data (intervention level 5)
temp_buffer = [x ** 2 for x in range(3)]  # Unused computation (minor distraction)

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")