def calculate_final_score(values, deductions):
    adjusted = [v * 0.9 for v in values]
    total = sum(adjusted)
    penalty_sum = sum(d for d in deductions if d > 0)
    final_deduction = penalty_sum * 1.5 if penalty_sum > 10 else penalty_sum
    result = total - final_deduction
    return result

scores = [85, 90, 78, 92]
penalties = [5, 0, 12]
extra_noise_variable = "irrelevant string"
temp_calc = [x**2 for x in range(3)]  # distractor list comprehension
result = calculate_final_score(scores, penalties)
print(f"Result: {result}")