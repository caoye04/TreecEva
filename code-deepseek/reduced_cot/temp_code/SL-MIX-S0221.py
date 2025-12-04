student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
best_student = max(student_grades, key=student_grades.get)
multiplier = 1.5
bonus_points = 10
final_score = student_grades[best_student] * multiplier
print(f"Result: {final_score}")