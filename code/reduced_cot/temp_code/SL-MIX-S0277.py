student_records = [('Alice', 85), ('Bob', 72), ('Charlie', 91), ('Diana', 78), ('Evan', 95)]
score_threshold = 80
preliminary_scores = [score for name, score in student_records]
above_threshold = [score for score in preliminary_scores if score > score_threshold]
filtered_scores = sorted(above_threshold)
temp_sum = sum(preliminary_scores)
count_distractor = len([x for x in preliminary_scores if x % 2 == 0])
adjustment_factor = max(filtered_scores) - min(filtered_scores) - 5
intermediate_calc = (temp_sum + count_distractor) // 10
final_result = filtered_scores[-1] + adjustment_factor
print(f"Result: {final_result}")