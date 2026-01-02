def calculate_final_score(results):
    total_points = sum(results)
    bonus_awarded = len(results) >= 4 and all(score > 70 for score in results)
    adjustment = 10 if bonus_awarded else 0
    return total_points + adjustment

exam_results = [85, 78, 92, 76]
student_count = 1  # Irrelevant tracking variable (minimal interference)
base_threshold = 70  # Used in logic but not directly modified
final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")