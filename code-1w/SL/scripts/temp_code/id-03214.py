from collections import defaultdict

# Simulate student quiz responses and correct answers
correct_answers = ['A', 'B', 'C', 'D', 'A', 'B']
student_responses = ['A', 'C', 'C', 'D', 'B', 'B']

# Track response frequency using defaultdict
response_count = defaultdict(int)
for response in student_responses:
    response_count[response] += 1

# Calculate base score based on number of correct answers
correct_count = sum(1 for i in range(len(correct_answers)) if student_responses[i] == correct_answers[i])
base_score = correct_count * 10  # 10 points per correct answer

# Apply logic penalty for inconsistent patterns
has_inconsistency = False
for i in range(len(student_responses) - 1):
    if student_responses[i] == 'C' and student_responses[i+1] == 'D':
        has_inconsistency = True

penalty = 5 if has_inconsistency and response_count['B'] > 1 else 0

# Bonus for frequent use of most common answer choice
most_common_response = max(response_count, key=response_count.get)
bonus = 7 if response_count[most_common_response] >= 2 else 0

# Final performance score calculation
final_score = base_score - penalty + bonus

print(f"Result: {final_score}")