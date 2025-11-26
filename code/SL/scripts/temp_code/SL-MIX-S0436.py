student_grades = [85, 92, 78, 96, 88, 74, 91, 83, 79, 95]
threshold = 80
preliminary_count = len(student_grades)
filtered_scores = []
for grade in student_grades:
    if grade >= threshold:
        filtered_scores.append(grade)
intermediate_sum = sum(filtered_scores)
temp_calc = intermediate_sum * 0.1
processed_data = filtered_scores[2:7:2]
final_score = sum(processed_data) // len(processed_data) if processed_data else 0
redundant_check = len(student_grades) - len(filtered_scores)
print(f"Target result: {final_score}")