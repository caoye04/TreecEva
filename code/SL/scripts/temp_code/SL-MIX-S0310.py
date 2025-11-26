import collections

# Analyze student performance across multiple assessments
student_scores = [85, 92, 78, 96, 88, 74, 91, 89]
bonus_points = 3
temp_calculation = sum(student_scores) // len(student_scores)

# Calculate weighted scores with some distraction operations
score_counter = collections.Counter(student_scores)
common_scores = score_counter.most_common(2)

# Process scores with list comprehension and filtering
filtered_scores = [score + bonus_points for score in student_scores if score >= 80]
intermediate_sum = sum(filtered_scores)

# More distraction operations
unused_set = set(student_scores)
set_operations = len(unused_set.intersection({85, 90, 95}))

# Final processing with logical operations
processed_scores = [score * 0.8 + 20 if score > 85 else score * 0.9 + 10 for score in filtered_scores]
processed_scores.sort()

# Calculate final result
final_score = processed_scores[-1]
print(f"Result: {final_score}")