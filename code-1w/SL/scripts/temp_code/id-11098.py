from itertools import combinations

# Simulate employee task logs with metadata
task_logs = [
    {'id': 101, 'status': 'completed', 'priority': 'high', 'duration': 45, 'errors': 0},
    {'id': 102, 'status': 'failed', 'priority': 'medium', 'duration': 30, 'errors': 3},
    {'id': 103, 'status': 'completed', 'priority': 'low', 'duration': 60, 'errors': 1},
    {'id': 104, 'status': 'completed', 'priority': 'high', 'duration': 40, 'errors': 0},
    {'id': 105, 'status': 'pending', 'priority': 'high', 'duration': 0, 'errors': 0},
]

# Irrelevant utility: converts duration to formatted string
def format_duration(d):
    hours, mins = divmod(d, 60)
    return f'{hours:02d}:{mins:02d}'

# Dead function: never called but looks important
def analyze_trends(logs):
    total_tasks = len(logs)
    completion_rate = sum(1 for t in logs if t['status'] == 'completed') / total_tasks
    return {'total': total_tasks, 'rate': completion_rate}

# Distractor: complex but unused combinatorics on task IDs
task_pairs = list(combinations([t['id'] for t in task_logs], 2))
high_priority_ids = [t['id'] for t in task_logs if t['priority'] == 'high']
co_occurrence_matrix = [[0]*len(task_logs) for _ in range(len(task_logs))]

# Unused transformation: string-based encoding of statuses
status_map = {'completed': 'C', 'failed': 'F', 'pending': 'P'}
encoded_statuses = ''.join(status_map[t['status']] for t in task_logs)
reversed_encoded = encoded_statuses[::-1]

# Another red herring: bit manipulation on error counts (not used in final logic)
event_bits = 0
for t in task_logs:
    event_bits ^= (t['errors'] << 2)
    event_bits += t['duration'] % 5

# Core logic disguised among noise
BASE_WEIGHT = 10
PRIORITY_MULTIPLIERS = {'low': 1, 'medium': 2, 'high': 3}
STATUS_BONUS = {'completed': 5, 'failed': -2, 'pending': 0}

def calculate_task_value(task):
    base = BASE_WEIGHT * PRIORITY_MULTIPLIERS[task['priority']]
    bonus = STATUS_BONUS[task['status']]
    penalty = task['errors'] * 3
    time_efficiency = (60 - task['duration']) / 10 if task['duration'] > 0 else 0
    return base + bonus - penalty + time_efficiency

# Secondary distraction: sorting by irrelevant metric
sorted_by_error_potential = sorted(
    task_logs,
    key=lambda x: x['errors'] * PRIORITY_MULTIPLIERS[x['priority']],
    reverse=True
)

# Real computation hidden in middle of noise
raw_values = [calculate_task_value(t) for t in task_logs]
filtered_values = [v for v in raw_values if v > 10]  # Only high-impact tasks count

# Decoy aggregation
mean_with_extremes = sum(raw_values) / len(raw_values)
trimmed_mean = sum(filtered_values) / len(filtered_values) if filtered_values else 0

# Critical operation buried after distractions
final_score = int(sum(
    v for i, v in enumerate(filtered_values)
    if i % 2 == 0  # Only even-indexed high-impact tasks
))

# More misdirection: fake normalization
if final_score > 50:
    normalized = final_score / 1.5
    rounded_norm = round(normalized, 2)
else:
    normalized = final_score * 1.1

# Actual output
print(f"Result: {final_score}")