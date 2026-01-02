def calculate_final_score(values, deductions):
    adjusted = list(map(lambda x: x * 1.1, values))
    total = sum(adjusted)
    penalty_sum = sum([d for d in deductions if d > 0])
    final_reduction = total * (penalty_sum / 100) if penalty_sum > 0 else 0
    return int(total - final_reduction)

# Irrelevant auxiliary data (minimal distraction)
user_data = {'id': 'USR921', 'version': '3.2'}
scores = [85, 92, 78, 88]
penalties = [5, -2, 3]

result = calculate_final_score(scores, penalties)
print(f'Result: {result}')