def calculate_final_score(students):
    total_scores = []
    for idx, (name, score, active) in enumerate(students):
        if not active:
            continue
        adjusted_score = score * (1 + 0.1 * (idx > 2))
        total_scores.append(adjusted_score)
    
    bonus_applied = len(total_scores) > 3
    final_sum = sum(total_scores)
    final_score = final_sum + (5 if bonus_applied else 0)
    return final_score

# Irrelevant auxiliary data (minimal distraction)
student_ids = [101, 102, 103, 104, 105]
dropout_rates = [0.05, 0.03, 0.07, 0.06, 0.09]

students = [
    ('Alice', 80, True),
    ('Bob', 75, True),
    ('Charlie', 88, False),
    ('Diana', 90, True),
    ('Evan', 82, True)
]

final_score = calculate_final_score(students)
print(f"Result: {final_score}")