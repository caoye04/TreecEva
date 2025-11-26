student_scores = [85, 92, 78, 96, 88]
temp_buffer = [x + 2 for x in student_scores]
score_list = temp_buffer[1:4]
enumerate_values = [index * value for index, value in enumerate(score_list)]
performance_score = sum(enumerate_values) / len(score_list)
print(f"Result: {performance_score}")