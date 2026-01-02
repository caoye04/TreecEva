def compute_backup_grade(scores):
    return sum(scores) / len(scores)

# Student grading scenario
student_scores = [85, 90, 78, 92]
extra_credits = [5, 3]  # Not used in main logic

# Compute weighted average
weighted_score = (student_scores[0] * 0.2) + (student_scores[1] * 0.3) + (student_scores[2] * 0.2) + (student_scores[3] * 0.3)

# Determine final score using conditional expression
passing_threshold = 80.0
final_scores = [weighted_score, 87, 76]
result = final_score if final_score > passing_threshold else compute_backup_grade(final_scores)

# Intermediate variable that doesn't affect result
unused_diagnostic = max(student_scores) - min(student_scores)

print(f"Result: {result}")