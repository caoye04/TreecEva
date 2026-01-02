from collections import defaultdict, Counter
from functools import reduce

# Simulate student responses to a logic-based assessment
test_responses = [
    {'student': 'A', 'answers': [True, False, True, True, False], 'time_spent': 120},
    {'student': 'B', 'answers': [True, True, False, True, True], 'time_spent': 95},
    {'student': 'C', 'answers': [False, True, True, False, False], 'time_spent': 140},
    {'student': 'D', 'answers': [True, True, True, True, False], 'time_spent': 110}
]

# Correct answer key for the 5 questions
answer_key = [True, True, True, False, True]

# Track correct answers per question
question_correct_count = defaultdict(int)
student_scores = []
distractor_variable_ignored = set()

# Accumulate results and compute individual scores
for response in test_responses:
    score = 0
    correctness_list = []
    
    # Evaluate each answer
    for i, ans in enumerate(response['answers']):
        if ans == answer_key[i]:
            score += 1
            question_correct_count[i] += 1
            correctness_list.append(True)
        else:
            correctness_list.append(False)
    
    # Irrelevant complexity: track pattern streaks (not used later)
    streak = 0
    max_streak = 0
    for c in correctness_list:
        if c:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    
    # Weighted score based on time spent (efficiency bonus)
    efficiency_bonus = max(0, (120 - response['time_spent']) * 0.1)
    weighted_score = score + efficiency_bonus
    student_scores.append({'student': response['student'], 'raw': score, 'weighted': weighted_score})

# Misleading intermediate calculation (dead-end analysis)
if len(student_scores) > 3:
    avg_weighted = sum(s['weighted'] for s in student_scores) / len(student_scores)
    adjusted_threshold = avg_weighted - 0.5
    filtered_students = [s for s in student_scores if s['weighted'] >= adjusted_threshold]

# Another distraction: analyze answer patterns using sets
all_answer_tuples = [tuple(r['answers']) for r in test_responses]
counter_distribution = Counter(all_answer_tuples)
duplicate_pattern_count = sum(1 for cnt in counter_distribution.values() if cnt > 1)

# Real computation path begins here
raw_total = sum(item['raw'] for item in student_scores)
weight_total = sum(item['weighted'] for item in student_scores)

# Use lambda to compute dynamic adjustment factor
adjustment_fn = lambda x, y: 0.8 if x/y < 0.7 else 1.0
adjustment = adjustment_fn(raw_total, len(test_responses) * len(answer_key))

def calculate_final_score(base, adj):
    # Additional noise: unused helper logic
    def unused_normalization(data):
        total = sum(data)
        return [x / total for x in data]
    
    # Actual logic
    penalty = 0
    if duplicate_pattern_count >= 1:
        penalty = 1.5
    
    # Final formula
    return int(round((base * adj) - penalty))

# Key execution point
final_score = calculate_final_score(weight_total, adjustment)

# Dead code branch (never executed, adds interference)
if __debug__:
    validation_check = sum(question_correct_count.values()) > 10
    distractor_variable_ignored.add(validation_check)

print(f"Result: {final_score}")