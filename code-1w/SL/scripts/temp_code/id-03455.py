from collections import defaultdict

# Simulate student quiz data with multiple attempts
student_data = [
    {'name': 'Alice', 'quiz': 'Q1', 'score': 85},
    {'name': 'Bob', 'quiz': 'Q1', 'score': 78},
    {'name': 'Alice', 'quiz': 'Q2', 'score': 92},
    {'name': 'Charlie', 'quiz': 'Q1', 'score': 88},
    {'name': 'Bob', 'quiz': 'Q2', 'score': 81}
]

# Group scores by student using defaultdict
scores_by_student = defaultdict(list)
for record in student_data:
    scores_by_student[record['name']].append(record['score'])

# Define a lambda to compute average score per student
average_score = lambda scores: round(sum(scores) / len(scores), 2)

# Calculate final composite score from highest individual quiz score across students
max_individual_scores = []
for name, scores in scores_by_student.items():
    max_individual_scores.append(max(scores))

# Bonus rule: if any student has all even-numbered scores, add 5-point bonus
all_even_bonus = 5 if all(all(score % 2 == 0 for score in scores) for scores in scores_by_student.values()) else 0

def calculate_final_score(data):
    base = sum(max_individual_scores)
    return base + all_even_bonus

total_score = calculate_final_score(student_data)
print(f"Result: {total_score}")