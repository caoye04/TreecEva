score_ranges = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
student_scores = [85, 92, 78, 88, 95]
score_range = max(student_scores) // 10 * 10
grade_mapping = {90: 4.0, 80: 3.0, 70: 2.0, 60: 1.0}
final_grade = grade_mapping.get(score_range, 0)
print(f"Result: {final_grade}")