from collections import Counter

student_grades = [85, 92, 78, 96, 88, 91, 74, 89, 95, 82]

# Calculate grade statistics
grade_counter = Counter(student_grades)
most_common_grade = grade_counter.most_common(1)[0][0]
average_grade = sum(student_grades) / len(student_grades)

# Process grades with adjustments
processed_data = []
for grade in student_grades:
    temp_adjustment = grade * 0.1  # Not used in final calculation
    adjusted_grade = grade + 2 if grade < 90 else grade - 1
    processed_data.append(adjusted_grade)

# Calculate adjustment factor based on grade distribution
high_grades = [g for g in student_grades if g >= 90]
low_grades = [g for g in student_grades if g < 80]
adjustment_factor = len(high_grades) - len(low_grades)

# Redundant calculation that doesn't affect final result
bonus_points = sum(g % 10 for g in student_grades)

# Final computation
final_score = processed_data[-1] + adjustment_factor
print(f"Result: {final_score}")