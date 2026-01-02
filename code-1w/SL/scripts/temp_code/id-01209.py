from itertools import compress

def evaluate_response(time_taken, threshold=2.5):
    return 1 if time_taken <= threshold else 0

def calculate_performance(times, accuracy_flags):
    weighted = [t * a for t, a in zip(times, accuracy_flags)]
    avg_weighted = sum(weighted) / len(weighted) if weighted else 0
    bonus = 10 if sum(accuracy_flags) >= 3 else 0
    return int(50 * avg_weighted + bonus)

task_durations = [1.8, 3.2, 2.1, 4.0]
response_accuracy = [True, False, True, True]

# Evaluate each response under time constraint
evaluation_flags = [evaluate_response(t) for t in task_durations]

# Compute performance score using weighted logic and bonus rules
final_score = calculate_performance(task_durations, evaluation_flags)

# Additional unrelated tracking (minimal distraction)
count_completed = len(task_durations)
completion_rate = count_completed / 4

Result: final_score