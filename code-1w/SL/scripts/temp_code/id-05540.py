def calculate_final(exams, project):
    exam_avg = sum(exams) / len(exams)
    practical_score = project[0] * 0.6 + project[1] * 0.4
    adjustment = 5 if exam_avg >= 85 else 0
    final_score = exam_avg * 0.7 + practical_score * 0.3 + adjustment
    return final_score

# Student performance data
exam_set = {88, 92, 79, 94}
project_tuple = (85, 90)
bonus_factor = 1.05  # Not used in computation (distractor)
threshold = 80       # Irrelevant threshold value

final_score = calculate_final(exam_set, project_tuple)
print(f"Result: {final_score}")