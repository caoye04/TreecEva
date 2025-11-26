from collections import Counter

student_grades = [85, 92, 78, 96, 88, 91, 74, 89]
# Distractor operations that don't affect the result
grade_frequencies = Counter(student_grades)
most_common_grade = grade_frequencies.most_common(1)[0][0]

def calculate_weighted_sum(grades):
    return sum(map(lambda x: x * 1.1, grades))

weighted_sum = calculate_weighted_sum(student_grades)
avg_grade = sum(student_grades) / len(student_grades)

# Relevant computations for final score
base_sum = sum(student_grades[:5])
adjustment_factor = 1.05
adjusted_sum = int(base_sum * adjustment_factor)

# More distractor calculations
temp_calc = (max(student_grades) - min(student_grades)) * 0.5
threshold_check = len([g for g in student_grades if g > 85])

penalty_points = 12
bonus_credit = 25
final_score = adjusted_sum - penalty_points + bonus_credit

print(f"Result: {final_score}")