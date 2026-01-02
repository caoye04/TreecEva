def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = sum(1 for entry in logs if 'success' in entry)
    failure_count = total_entries - valid_count
    efficiency_ratio = valid_count / total_entries if total_entries else 0
    return efficiency_ratio

# Simulated system logs with mixed outcomes
task_logs = [
    'task_01_success', 'task_02_fail', 'task_03_success', 'task_04_success',
    'task_05_fail', 'task_06_success', 'task_07_success', 'task_08_fail'
]

# Irrelevant distraction: character frequency analysis
char_freq = {}
for log in task_logs:
    for char in log:
        char_freq[char] = char_freq.get(char, 0) + 1
rare_chars = [c for c, freq in char_freq.items() if freq < 2]

# Secondary metric with partial relevance
streak_counter = 0
longest_streak = 0
for log in task_logs:
    if 'success' in log:
        streak_counter += 1
        longest_streak = max(longest_streak, streak_counter)
    else:
        streak_counter = 0

# Core productivity signal
productivity = sum(1 for log in task_logs if log.endswith('_success'))
errors = len([log for log in task_logs if '_fail' in log])

# Misleading intermediate calculation (not used in final result)
avg_task_length = sum(len(log) for log in task_logs) / len(task_logs)
complexity_heuristic = avg_task_length * 0.75

# Lambda-based dynamic weight (used)
weight_fn = lambda x, y: 1.5 if x / (x + y) > 0.6 else 1.0

# Core evaluation logic
def evaluate_performance(completed, failed):
    if failed == 0:
        return completed * 10
    performance_rate = completed / (completed + failed)
    bonus_factor = weight_fn(completed, failed)
    base_score = completed * 5
    penalty = failed * 3
    return int((base_score - penalty) * bonus_factor + (performance_rate * 10))

# Final computation step
final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")