def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def process_student_grades(quizzes, assignments):
    quiz_avg = calculate_average(quizzes)
    assignment_avg = calculate_average(assignments)
    final_grade = (quiz_avg * 0.3) + (assignment_avg * 0.7)
    return round(final_grade, 2)

quiz_scores = [85, 92, 78, 90]
assignment_grades = [88, 95, 82, 91, 87]
student_name = "Alex Johnson"
course_code = "CS101"

final_score = process_student_grades(quiz_scores, assignment_grades)
print(f"Result: {final_score}")