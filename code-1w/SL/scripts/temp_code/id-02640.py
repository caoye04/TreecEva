from collections import defaultdict, Counter

# Simulate student responses to a multi-part assessment
def analyze_responses():
    raw_answers = ['A', 'B', 'C', 'A', 'D', 'B', 'A', 'C', 'A']
    correct_key = {'q1': 'A', 'q2': 'B', 'q3': 'C', 'q4': 'A', 'q5': 'D'}
    
    # Distractor: unused scoring weights
    scoring_weights = {'easy': 1, 'medium': 2, 'hard': 3}
    difficulty_map = {'q1': 'easy', 'q2': 'medium', 'q3': 'hard', 'q4': 'easy', 'q5': 'hard'}

    # Track answer frequencies (semi-relevant)
    frequency_stats = Counter(raw_answers)
    total_A = frequency_stats['A']
    total_B = frequency_stats['B']
    total_C = frequency_stats['C']
    total_D = frequency_stats['D']

    # Compute per-question correctness
    results = defaultdict(bool)
    for i, q in enumerate(['q1', 'q2', 'q3', 'q4', 'q5'], 0):
        if i < len(raw_answers):
            results[q] = (raw_answers[i] == correct_key[q])
        else:
            results[q] = False  # Unanswered = incorrect

    # Intermediate score calculation
    correct_count = sum(1 for val in results.values() if val)
    attempted_count = min(len(raw_answers), 5)
    accuracy_rate = correct_count / attempted_count if attempted_count > 0 else 0

    # Bonus logic for streaks (distraction)
    max_streak = 0
    current_streak = 0
    for ans in raw_answers[:5]:
        idx = raw_answers.index(ans)
        q = ['q1','q2','q3','q4','q5'][idx]
        if results[q]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    # Irrelevant transformation
    normalized_A = round(total_A / len(raw_answers), 3) if len(raw_answers) > 0 else 0

    # Core computation: aggregate score with penalty for over-attempts
    base_score = correct_count * 10
    penalty = max(0, len(raw_answers) - 5) * 2  # Penalty for extra answers
    bonus = 5 if max_streak >= 3 else 0

    final_score = base_score - penalty + bonus

    # Dead code: never executed but looks important
    if False:
        final_score = int(final_score * 1.1) if accuracy_rate > 0.8 else int(final_score * 0.9)

    return final_score

# Execute and print result
target_result = analyze_responses()
print(f"Target result: {target_result}")