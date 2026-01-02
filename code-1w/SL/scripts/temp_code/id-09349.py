def calculate_performance(effort, persistence):
    base = effort * 2.5
    bonus = 10 if persistence > 7 else 5
    return base + bonus

# Simulate learning session metrics
task_duration = 45
engagement = task_duration * 1.2
retention = 8

# Irrelevant distraction: logging session info
session_log = f'Duration: {task_duration}min'.upper()
dummy_set = {1, 2, 3}
dummy_set.add(4)  # No effect on logic

# Key computation chain
initial_estimate = engagement + 5
adjusted_retention = max(retention, 6)
final_score = calculate_performance(engagement, retention)

print(f'Result: {final_score}')