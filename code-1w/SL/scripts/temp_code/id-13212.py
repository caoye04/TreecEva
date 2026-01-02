from itertools import compress

def calculate_final_score(scores, importance_weights):
    normalized = [score / 100 for score in scores]
    weighted = [n * w for n, w in zip(normalized, importance_weights)]
    total_weight = sum(importance_weights)
    adjusted_total = sum(weighted) * (100 / total_weight)
    return round(adjusted_total)

# Irrelevant auxiliary variables (minimal distraction - intervention level 5)
student_id = "S123456"
enrollment_year = 2023
course_credits = [3, 4, 3, 2]

raw_scores = [88, 94, 76, 85]
weights = [0.2, 0.5, 0.2, 0.1]

# Key computation
final_score = calculate_final_score(raw_scores, weights)

# Output result as required
print(f"Result: {final_score}")