def calculate_final_score(results, attendance):
    base_score = sum(results.values())
    bonus_points = len(attendance.difference({'absent', 'late'})) * 2
    penalty = 0
    if 'cheating' in results.keys():
        penalty = 50
    adjusted_score = base_score + bonus_points - penalty
    return max(adjusted_score, 0)

# Exam results for student
exam_results = {
    'math': 85,
    'physics': 90,
    'chemistry': 88
}

# Attendance record set
attendance_record = {'present', 'on_time', 'early'}

# Irrelevant variable (minor distraction)
temp_log = [1, 2, 3]

final_score = calculate_final_score(exam_results, attendance_record)
print(f"Result: {final_score}")