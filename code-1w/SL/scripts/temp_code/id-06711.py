from collections import defaultdict, Counter

# Simulate employee task logs with redundant metadata
task_logs = [
    {'employee': 'Alice', 'task': 'debug', 'duration': 45, 'errors': 2, 'priority': 'high'},
    {'employee': 'Bob', 'task': 'deploy', 'duration': 30, 'errors': 0, 'priority': 'medium'},
    {'employee': 'Alice', 'task': 'review', 'duration': 25, 'errors': 1, 'priority': 'low'},
    {'employee': 'Charlie', 'task': 'debug', 'duration': 60, 'errors': 5, 'priority': 'high'},
    {'employee': 'Bob', 'task': 'debug', 'duration': 50, 'errors': 3, 'priority': 'high'},
    {'employee': 'Charlie', 'task': 'review', 'duration': 20, 'errors': 0, 'priority': 'low'}
]

# Irrelevant aggregation: count tasks by priority (not used in final score)
priority_count = defaultdict(int)
for log in task_logs:
    priority_count[log['priority']] += 1

# Track total work time per employee (semi-relevant)
work_time = defaultdict(int)
error_count = defaultdict(int)
task_count = Counter()

for log in task_logs:
    emp = log['employee']
    work_time[emp] += log['duration']
    error_count[emp] += log['errors']
    task_count[emp] += 1

# Distractor computation: efficiency ratio (never used)
efficiency = {}
for emp in work_time:
    raw_ratio = (work_time[emp] / (error_count[emp] + 1))
    efficiency[emp] = round(raw_ratio, 2) if raw_ratio > 10 else 0

# Real logic: compute performance penalty based on error density and debug involvement
def evaluate_performance(employee: str) -> float:
    total_time = work_time[employee]
    total_errors = error_count[employee]
    debug_tasks = len([t for t in task_logs if t['employee'] == employee and t['task'] == 'debug'])

    # Base score from time spent
    base_score = total_time * 0.8

    # Penalty for high error density
    error_density = total_errors / len(task_logs)  # normalized across all logs
    penalty = total_errors * 12 * error_density

    # Bonus for handling debug tasks
    bonus = debug_tasks * 15 if debug_tasks >= 1 else 0

    # Conditional adjustment: extra credit if worked more than average
    avg_time = sum(work_time.values()) / len(work_time)
    extra_credit = 20 if total_time > avg_time else 0

    return base_score - penalty + bonus + extra_credit

# Misleading intermediate calculation (dead-end)
total_penalty_pool = sum(e * 12 for e in error_count.values())
adjusted_pool = total_penalty_pool * 0.75 if total_penalty_pool > 100 else total_penalty_pool

# Key statement
final_score = evaluate_performance('Alice')

# Output result as required
print(f"Result: {final_score}")