from collections import Counter

def analyze_grades(grades):
    # Calculate some statistics that won't be used
    grade_counts = Counter(grades)
    most_common = grade_counts.most_common(1)[0][0]
    
    # Process that will be used
    total = sum(grades)
    average = total / len(grades)
    return average

def calculate_bonus(attendance):
    # Some operations that won't affect the result
    perfect_record = all(day > 0 for day in attendance)
    late_days = sum(1 for day in attendance if day == 1)
    
    # The actual calculation that matters
    attendance_rate = sum(attendance) / (len(attendance) * 2)
    bonus = 10 * attendance_rate if attendance_rate > 0.8 else 0
    return bonus

def calculate_weighted_score(student_data):
    # Extract relevant data
    quiz_scores = student_data['quiz_scores']
    exam_scores = student_data['exam_scores']
    attendance = student_data['attendance']
    
    # Some operations that won't be used in final calculation
    max_quiz = max(quiz_scores)
    min_exam = min(exam_scores)
    score_difference = max_quiz - min_exam
    
    # Relevant calculations
    quiz_weight = 0.3
    exam_weight = 0.6
    attendance_weight = 0.1
    
    # Slice operations for processing
    relevant_quizzes = quiz_scores[1:-1]  # Remove highest and lowest quiz
    quiz_average = sum(relevant_quizzes) / len(relevant_quizzes)
    
    # Lambda for calculating exam score with bonus points
    calculate_exam_score = lambda scores: sum(scores) / len(scores) + (5 if max(scores) > 90 else 0)
    exam_score = calculate_exam_score(exam_scores)
    
    # Calculate attendance bonus
    attendance_bonus = calculate_bonus(attendance)
    
    # Bitwise operations for some additional processing (that won't affect result)
    bit_flag = 0b1010 & 0b1100  # equals 8 (0b1000)
    
    # Final weighted calculation
    weighted_sum = (quiz_average * quiz_weight) + \
                  (exam_score * exam_weight) + \
                  (attendance_bonus * attendance_weight)
    
    # Round to 2 decimal places
    return round(weighted_sum, 2)

# Student data
student_data = {
    'name': 'Alex Johnson',
    'id': 'AJ2023',
    'quiz_scores': [75, 82, 78, 90, 65],
    'exam_scores': [88, 92, 85],
    'attendance': [2, 2, 1, 2, 0, 2, 1, 2, 2, 2]  # 2=present, 1=late, 0=absent
}

# Calculate the final score
final_score = calculate_weighted_score(student_data)
print(f"Result: {final_score}")
