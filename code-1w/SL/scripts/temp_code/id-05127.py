def calculate_final_score(records):
    weights = {'quiz': 0.2, 'midterm': 0.3, 'final': 0.5}
    weighted_sum = sum(r['score'] * weights[r['type']] for r in records)
    return round(weighted_sum, 3)

# Irrelevant auxiliary data (minimal distraction)
student_id = "S78901"
enrollment_year = 2023

assessments = [
    {'type': 'quiz', 'score': 85},
    {'type': 'midterm', 'score': 78},
    {'type': 'final', 'score': 92}
]

# Main computation
adjustment_factor = 1.0
adjusted_assessments = [{**a, 'score': a['score'] * adjustment_factor} for a in assessments]

total_score = calculate_final_score(adjusted_assessments)
print(f"Result: {total_score}")