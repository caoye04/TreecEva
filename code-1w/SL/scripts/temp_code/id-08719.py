def calculate_final(scores, present_days):
    avg_score = sum(scores) / len(scores)
    bonus = 5 if present_days >= 20 else 0
    weighted_exam = avg_score * 0.8
    attendance_points = min(present_days * 0.25, 10)
    final_result = weighted_exam + attendance_points + bonus
    return round(final_result, 2)

# Irrelevant auxiliary variable (minimal distraction)
initial_threshold = 75

exam_scores = [88, 92, 76, 85, 90]
attendance = 22
difficulty_factor = 1.05  # Unused parameter, slight interference

final_score = calculate_final(exam_scores, attendance)
print(f"Target result: {final_score}")