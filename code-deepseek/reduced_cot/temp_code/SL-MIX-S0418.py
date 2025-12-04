student_scores = [85, 92, 78, 96, 88]
assignment_weights = [0.15, 0.20, 0.10, 0.25, 0.30]
weighted_total = 0
for i in range(len(student_scores)):
    weighted_total += student_scores[i] * assignment_weights[i]
bonus_points = 5 if weighted_total > 85 else 0
final_score = weighted_total + bonus_points
print(f"Result: {final_score}")