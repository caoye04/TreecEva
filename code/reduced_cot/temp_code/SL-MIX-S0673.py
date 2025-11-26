student_scores = [85, 92, 78, 96, 88, 91]
bonus_points = 5
adjusted_scores = [score + bonus_points for score in student_scores]
final_grade = adjusted_scores[-3:] if len(adjusted_scores) >= 3 else adjusted_scores
print(f"Target result: {final_grade}")