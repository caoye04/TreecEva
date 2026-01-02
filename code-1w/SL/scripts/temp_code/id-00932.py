from collections import defaultdict

# Simulate employee task logs with timestamps and completion status
task_logs = [
    {'employee': 'Alice', 'task': 'T1', 'duration': 120, 'completed': True},
    {'employee': 'Bob', 'task': 'T2', 'duration': 95, 'completed': False},
    {'employee': 'Alice', 'task': 'T3', 'duration': 150, 'completed': True},
    {'employee': 'Charlie', 'task': 'T4', 'duration': 80, 'completed': True},
    {'employee': 'Bob', 'task': 'T5', 'duration': 200, 'completed': True},
    {'employee': 'Charlie', 'task': 'T6', 'duration': 110, 'completed': False}
]

# Track productivity metrics per employee
productivity = defaultdict(lambda: {'tasks_completed': 0, 'total_time': 0, 'penalty_points': 0})

for log in task_logs:
    emp = log['employee']
    if log['completed']:
        productivity[emp]['tasks_completed'] += 1
        productivity[emp]['total_time'] += log['duration']
    else:
        productivity[emp]['penalty_points'] += 1

# Calculate average time per completed task for each employee
avg_times = {}
for emp, data in productivity.items():
    if data['tasks_completed'] > 0:
        avg_times[emp] = data['total_time'] / data['tasks_completed']
    else:
        avg_times[emp] = float('inf')

# Misleading distraction: compute unused efficiency ratio
efficiency_ratio = lambda x, y: (x / (y + 1)) if y != float('inf') else 0
unused_ratios = {e: efficiency_ratio(productivity[e]['tasks_completed'], avg_times[e]) for e in productivity}

# Risk factor based on penalty points and inconsistency
risk_factor = 0
for data in productivity.values():
    risk_factor += data['penalty_points'] * 2
    if data['tasks_completed'] == 0:
        risk_factor += 5

# Real evaluation logic
completion_weight = sum(p['tasks_completed'] for p in productivity.values())
time_penalty = sum(max(0, p['total_time'] - 100) for p in productivity.values()) // 10

baseline = completion_weight * 10
time_adjustment = max(0, 50 - time_penalty)

# Distractor: unused complex calculation involving string hashing
hash_distractor = sum(len(name)**2 for name in productivity.keys()) % 7

# Final performance score
final_score = baseline + time_adjustment - risk_factor

# Irrelevant logging
log_entries = [f'{k}: {v}' for k, v in productivity.items()]
dummy_sum = sum(len(entry) for entry in log_entries) % 13  # Dead computation

Result: final_score