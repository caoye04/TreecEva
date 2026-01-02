def calculate_final_score(grades, coefficients):
    weighted_sum = sum([g * c for g, c in zip(grades, coefficients)])
    max_grade = max(grades)
    normalized = [round(g / max_grade * 100, 2) for g in grades]
    avg_normalized = sum(normalized) / len(normalized)
    return int(weighted_sum + (avg_normalized * 0.1))

marks = [85, 90, 78, 92]
weights = [0.25, 0.3, 0.15, 0.3]
bonus_data = [1.1, 2.3, 3.5]  # irrelevant data
initial_avg = sum(marks) / len(marks)
final_score = calculate_final_score(marks, weights)
print(f"Target result: {final_score}")