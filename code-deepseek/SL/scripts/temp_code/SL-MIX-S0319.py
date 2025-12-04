student_scores = [85, 92, 78, 96, 88]
bonus_points = [5, 3, 7, 2, 6]
threshold = 90
total_score = 0

for idx, (score, bonus) in enumerate(zip(student_scores, bonus_points)):
    adjusted_score = score + bonus
    if adjusted_score >= threshold:
        total_score += adjusted_score

print(f"Result: {total_score}")