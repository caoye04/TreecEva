from collections import defaultdict
from itertools import combinations

# Simulate employee task logs
task_logs = [
    {'employee': 'Alice', 'tasks': 15, 'errors': 2, 'overtime_hours': 3},
    {'employee': 'Bob', 'tasks': 12, 'errors': 5, 'overtime_hours': 6},
    {'employee': 'Charlie', 'tasks': 20, 'errors': 1, 'overtime_hours': 2},
    {'employee': 'Diana', 'tasks': 18, 'errors': 4, 'overtime_hours': 4}
]

# Irrelevant helper: counts character frequency in names (distractor)
def analyze_name_complexity(employees):
    char_count = defaultdict(int)
    for record in employees:
        name = record['employee']
        for char in name:
            char_count[char] += 1
    return char_count

# Misleading metric: computes unused 'effort_score'
def compute_effort_score(logs):
    effort = 0
    for log in logs:
        base_effort = log['tasks'] * 1.5
        overtime_bonus = log['overtime_hours'] * 2
        effort += base_effort + overtime_bonus
    return effort  # Never used in final logic

# Core logic: productivity ratio adjusted by error penalty
def calculate_productivity(tasks, errors):
    if tasks == 0:
        return 0.0
    base_productivity = tasks / (errors + 1)
    penalty = errors * 0.8
    return max(base_productivity - penalty, 0.5)  # Minimum floor

# Another distractor: generates all pairs of employees (unused)
def generate_peer_pairs(employees):
    names = [e['employee'] for e in employees]
    return list(combinations(names, 2))  # Computed but not used

# Real evaluation function
def evaluate_performance(productivity, errors):
    base = productivity * 10
    adjustment = 0
    if errors <= 2:
        adjustment = 5
    elif errors <= 4:
        adjustment = 2
    else:
        adjustment = -3
    return int(base + adjustment)

# Main processing
name_analysis = analyze_name_complexity(task_logs)  # Distractor call
peer_groups = generate_peer_pairs(task_logs)         # Unused computation
total_effort = compute_effort_score(task_logs)       # Dead-end calculation

# Process each employee's real metrics
results = []
for log in task_logs:
    p = calculate_productivity(log['tasks'], log['errors'])
    score = evaluate_performance(p, log['errors'])
    results.append({'employee': log['employee'], 'score': score})

# Focus on Charlie's final evaluation
charlie_log = task_logs[2]
productivity = calculate_productivity(charlie_log['tasks'], charlie_log['errors'])
errors = charlie_log['errors']
final_score = evaluate_performance(productivity, errors)

# Additional red herring: set operation with no impact
distinct_tasks = {log['tasks'] for log in task_logs}
distinct_tasks.add(99)  # Meaningless mutation

print(f"Result: {final_score}")