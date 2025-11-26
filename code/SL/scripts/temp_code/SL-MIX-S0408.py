student_scores = [85, 92, 78, 96, 88]
bonus_points = [3, 2, 5, 1, 4]

enumerate_scores = []
for idx, (score, bonus) in enumerate(zip(student_scores, bonus_points)):
    adjusted_score = score + bonus
    if adjusted_score > 90:
        enumerate_scores.append(adjusted_score)

final_score = sum(enumerate_scores)
print(f"Result: {final_score}")