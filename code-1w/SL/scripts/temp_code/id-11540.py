from collections import Counter

# Simulate student quiz responses and scoring
def evaluate_answers(correct_key, student_responses):
    return [1 if resp == key else 0 for resp, key in zip(student_responses, correct_key)]

# Apply scoring rubric with bonus for consecutive correct answers
def calculate_bonus(scores):
    bonus = 0
    consecutive = 0
    for score in scores:
        if score == 1:
            consecutive += 1
            if consecutive == 3:
                bonus += 2  # Bonus for triple consecutive
                consecutive = 0  # Reset to avoid overlapping bonuses
        else:
            consecutive = 0
    return bonus

# Final score calculation combining base and bonus
def calculate_final_score(result_list):
    base = sum(result_list)
    extra = calculate_bonus(result_list)
    return base + extra

# Quiz setup
correct_answer_key = ['A', 'B', 'C', 'A', 'B']
student_answers = ['A', 'B', 'C', 'A', 'B']  # All correct

# Evaluate individual responses
raw_scores = evaluate_answers(correct_answer_key, student_answers)

# Count response distribution (irrelevant but plausible)
distribution = Counter(student_answers)

# Compute final score with bonus logic
total_score = calculate_final_score(raw_scores)

print(f"Result: {total_score}")