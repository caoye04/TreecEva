from collections import defaultdict

def calculate_final_score(data):
    base_score = data['exam'] * 0.6
    quiz_avg = sum(data['quizzes']) / len(data['quizzes']) * 0.3
    participation = 10 if data['participation_days'] > 15 else 5
    
    # Irrelevant distraction: counting feedback length
    feedback_length = len(data['feedback'].split())
    bonus = 5 if feedback_length > 20 and data['exam'] > 75 else 0
    
    total = base_score + quiz_avg + participation + bonus
    return round(total, 2)

# Student data input
student_data = {
    'exam': 88,
    'quizzes': [85, 90, 78],
    'participation_days': 18,
    'feedback': 'Excellent effort throughout the term with consistent improvement and strong engagement in class discussions'
}

final_score = calculate_final_score(student_data)
print(f"Result: {final_score}")