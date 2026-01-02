from collections import defaultdict

# Simulate student quiz responses and correct answers
correct_answers = ['A', 'B', 'C', 'D', 'A', 'B']
student_responses = {
    'Alice': ['A', 'B', 'C', 'D', 'A', 'B'],
    'Bob': ['A', 'C', 'C', 'D', 'A', 'D'],
    'Charlie': ['A', 'B', 'B', 'D', 'B', 'B']
}

# Irrelevant distractor: unused function
def unused_helper():
    return sum([i * i for i in range(3)])

# Count correct responses per student
correct_counts = defaultdict(int)
for student, answers in student_responses.items():
    for i, answer in enumerate(answers):
        if answer == correct_answers[i]:
            correct_counts[student] += 1

# Calculate total points with bonus for perfect sections
section_bonus = 0
if correct_counts['Alice'] >= 5:
    section_bonus += 2
if correct_counts['Bob'] >= 5:
    section_bonus += 2
if correct_counts['Charlie'] >= 5:
    section_bonus += 2

total_base_score = sum(correct_counts.values())

# Apply multiplier based on number of students exceeding threshold
performance_multiplier = 1.5 if sum(1 for count in correct_counts.values() if count >= 5) >= 2 else 1.0

# Final score computation
def calculate_final_score():
    base = total_base_score
    bonus = section_bonus
    multiplier = performance_multiplier
    return int((base + bonus) * multiplier)

final_score = calculate_final_score()
print(f"Result: {final_score}")