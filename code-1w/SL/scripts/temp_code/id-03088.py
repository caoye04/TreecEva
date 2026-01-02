from collections import defaultdict

# Simulate a work session with task logging and performance metrics
task_log = [
    ('write', 45, True),
    ('review', 30, False),
    ('debug', 60, True),
    ('meeting', 40, False),
    ('refactor', 55, True)
]

# Irrelevant aggregation: count task types (distractor)
task_counter = defaultdict(int)
for task_type, duration, is_productive in task_log:
    task_counter[task_type] += 1

# Track various metrics
idle_time = 0
setup_time = 15
breaks = [10, 5, 7]
gross_minutes = sum(duration for _, duration, _ in task_log) + setup_time + sum(breaks)

# Core data for computation
productive_tasks = []
total_output = 0
active_minutes = 0
penalty_factor = 0.0

# Secondary loop with conditional expressions and enumeration (moderate nesting)
for i, (task_type, duration, is_productive) in enumerate(task_log):
    adjusted_duration = duration * (0.8 if task_type == 'review' else 1.0)
    
    # Only productive tasks contribute to output
    if is_productive:
        contribution = (duration ** 0.5) * (i + 1)  # Non-linear output based on order and duration
        total_output += contribution
        active_minutes += duration
        productive_tasks.append((task_type, duration, contribution))
    else:
        idle_time += duration
        # Red herring: modify unused variable
        penalty_factor += 0.1

# Distractor: complex but unused calculation using zip and enumerate
overlap_index = 0
for idx, (a, b) in enumerate(zip(breaks, breaks[1:])):
    overlap_index += (a + b) * (idx + 1)

# Unused helper function (dead code path)
def calculate_stress_level(minutes, tasks):
    return len(tasks) * minutes // 10

# Final efficiency metric — this is where the answer comes from
efficiency_score = total_output / active_minutes if active_minutes > 0 else 0

# Print result as required
print(f"Result: {efficiency_score}")