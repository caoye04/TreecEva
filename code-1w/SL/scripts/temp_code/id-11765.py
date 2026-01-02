def calculate_performance(response_log, cutoffs):
    correct_count = 0
    bonus_active = False
    base_scores = []

    for entry in response_log:
        # Extract time and correctness
        elapsed_time = entry['time']
        is_correct = entry['correct']
        difficulty_level = entry['difficulty']

        # Core logic: correct answer within time threshold earns points
        if is_correct and elapsed_time <= cutoffs[difficulty_level]:
            correct_count += 1
            if elapsed_time < 2.0:
                bonus_active = True

        # Record base score regardless
        base_scores.append(1 if is_correct else 0)

    # Compute final score with optional bonus
    total_base = sum(base_scores)
    final_score = total_base * (1.5 if bonus_active else 1.0)
    
    return int(final_score)

# Simulated input data
thresholds = {'easy': 5.0, 'medium': 3.5, 'hard': 2.5}
answers = [
    {'time': 1.8, 'correct': True, 'difficulty': 'easy'},
    {'time': 4.2, 'correct': True, 'difficulty': 'medium'},
    {'time': 3.0, 'correct': False, 'difficulty': 'hard'},
    {'time': 2.1, 'correct': True, 'difficulty': 'hard'},
    {'time': 1.5, 'correct': True, 'difficulty': 'medium'}
]

# Irrelevant helper (minimal distraction)
def format_time(t):
    return f'{t:.2f}s'

unused_list = [format_time(a["time"]) for a in answers]  # Slight interference

final_score = calculate_performance(answers, thresholds)
print(f'Result: {final_score}')