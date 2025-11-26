student_grades = {101: 85, 102: 92, 103: 78, 104: 88, 105: 95}
attendance_scores = [90, 85, 95, 80, 92]
bonus_points = 5

# Calculate adjusted grades with attendance bonus
adjusted_grades = {}
for i, (student_id, grade) in enumerate(student_grades.items()):
    adjusted_grades[student_id] = grade + (attendance_scores[i] // 10) + bonus_points

# Find student with maximum grade
max_student_id = max(student_grades, key=student_grades.get)

# Distractor calculations
average_grade = sum(student_grades.values()) / len(student_grades)
temp_scores = [x * 2 for x in attendance_scores]
unused_calculation = sum(temp_scores) - 100

# Key statement
final_score = adjusted_grades[max_student_id]
print(f"Result: {final_score}")