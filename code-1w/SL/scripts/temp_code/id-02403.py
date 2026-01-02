from collections import defaultdict

# Simulate student quiz responses and scoring
questions = ['q1', 'q2', 'q3', 'q4']
correct_answers = {'q1': 'A', 'q2': 'B', 'q3': 'C', 'q4': 'D'}
student_responses = [
    {'q1': 'A', 'q2': 'B', 'q3': 'C', 'q4': 'D'},
    {'q1': 'A', 'q2': 'B', 'q3': 'D', 'q4': 'D'},
    {'q1': 'B', 'q2': 'B', 'q3': 'C', 'q4': 'A'}
]

# Count correct answers per question
question_correct_count = defaultdict(int)
for response in student_responses:
    for q, ans in response.items():
        if ans == correct_answers[q]:
            question_correct_count[q] += 1

# Calculate average correctness across questions
total_questions = len(questions)
sum_correct_ratio = sum(question_correct_count[q] / len(student_responses) for q in questions)
avg_correct_ratio = sum_correct_ratio / total_questions

# Bonus logic based on consistency
consistency_bonus = 1.0 if question_correct_count['q2'] == question_correct_count['q4'] else 0.5

# Difficulty adjustment: q3 was hardest, so weight it inversely
difficulty_factor = 1.2 if question_correct_count['q3'] < 2 else 1.0

# Final score calculation
base_score = avg_correct_ratio * 100
adjusted_score = base_score * difficulty_factor
final_score = int(adjusted_score + consistency_bonus)

Result: final_score