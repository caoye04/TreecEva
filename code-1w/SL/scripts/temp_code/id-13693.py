from collections import defaultdict, Counter

# Simulate user interaction logs for a productivity app
task_log = [
    ('task1', 'start', 10), ('task2', 'start', 15), ('task1', 'pause', 20),
    ('task3', 'start', 25), ('task2', 'stop', 30), ('task3', 'pause', 35),
    ('task1', 'resume', 40), ('task1', 'stop', 50), ('task4', 'start', 55),
    ('task4', 'stop', 60)
]

status_tracker = defaultdict(list)
duration_map = {}
for task_id, action, timestamp in task_log:
    status_tracker[task_id].append((action, timestamp))

# Calculate task durations
for task, events in status_tracker.items():
    start_time = None
    total_duration = 0
    for action, time in events:
        if action == 'start':
            start_time = time
        elif action == 'stop' and start_time is not None:
            total_duration += time - start_time
            start_time = None
        elif action == 'pause' and start_time is not None:
            total_duration += time - start_time
            start_time = None
        elif action == 'resume':
            start_time = time
    duration_map[task] = total_duration

# Irrelevant aggregation: count transitions (not used later)
transition_counter = Counter(action for _, action, _ in task_log)
unused_sum = sum(transition_counter.values()) // 2  # Distractor

# Focus on tasks that took longer than 15 units
filtered_tasks = {k: v for k, v in duration_map.items() if v > 15}

# Another distractor: tuple unpacking with zip
ranks = sorted(filtered_tasks.keys())
sorted_durations = [filtered_tasks[k] for k in ranks]
indexed_pairs = list(enumerate(zip(ranks, sorted_durations)))
offset_correction = len(indexed_pairs) * 2  # Not directly impactful

# Base metrics
base_value = sum(filtered_tasks.values())  # 35 + 5 = 40

# Bonus logic based on task diversity
unique_actions = set(action for _, action, _ in task_log)
bonus_multiplier = 1 if len(unique_actions) > 4 else 0.5
bonus_points = len(filtered_tasks) * 7 * bonus_multiplier  # 2 * 7 * 1 = 14

# Penalty system
penalty_count = 0
for actions in status_tracker.values():
    pauses = [act for act, _ in actions if act == 'pause']
    if len(pauses) > 1:
        penalty_count += 1  # Only task1 has multiple pauses

adjustment_factor = 3

# Key statement
final_score = base_value + bonus_points - penalty_count * adjustment_factor

# Print result
print(f"Result: {final_score}")