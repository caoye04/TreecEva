def calculate_final_score(exams, attendance):
    base_score = sum(exams) / len(exams)
    attendance_bonus = 5 if all(att >= 0.8 for att in attendance) else 0
    curve_factor = 1.1 if base_score < 75 else 1.0
    
    # Irrelevant variable (minor distraction)
    max_possible = 100 * len(exams)
    
    adjusted_score = base_score * curve_factor + attendance_bonus
    return round(adjusted_score)

# Input data
exam_results = [82, 76, 91, 69]
attendance_records = [0.85, 0.92, 0.88]

# Compute final score
defined_before = True
final_score = calculate_final_score(exam_results, attendance_records)
print(f"Target result: {final_score}")