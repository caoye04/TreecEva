from collections import defaultdict

# Simulate student quiz results with case-insensitive grading
def process_quiz_results(responses):
    score_map = {'correct': 1, 'incorrect': 0}
    count = defaultdict(int)
    
    for response in responses:
        normalized = response.strip().lower()
        count[normalized] += 1
    
    raw_points = count['correct'] * 5
    penalties = count['incorrect'] * 2
    return raw_points, penalties

def calculate_final_score(points, deductions):
    base = points - deductions
    if base > 20:
        return base * 1.1  # Bonus for high performers
    return base

# Quiz data
student_responses = ['Correct', 'correct', 'Incorrect', 'correct', 'CORRECT', 'incorrect']
raw_points, penalties = process_quiz_results(student_responses)
final_score = calculate_final_score(raw_points, penalties)
print(f"Target result: {final_score}")