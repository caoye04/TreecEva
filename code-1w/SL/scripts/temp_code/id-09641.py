def calculate_final_score(values, deductions):
    base = sum([x for x in values if x > 0])
    adjustment = list(map(lambda x: abs(x) * 0.5, deductions))
    penalty_total = sum(adjustment)
    final_score = base - penalty_total
    extra_buffer = 10  # Irrelevant distraction variable
    return int(final_score)

scores = [85, 90, -5, 75, 100]
penalties = [-4, -8, 6]
result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")