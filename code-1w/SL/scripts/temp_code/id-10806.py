from collections import defaultdict, Counter

# Simulate employee task completion data
task_logs = [
    {'employee': 'alice', 'task': 'data_cleaning', 'status': 'completed', 'priority': 3},
    {'employee': 'bob', 'task': 'bug_fix', 'status': 'failed', 'priority': 2},
    {'employee': 'alice', 'task': 'report_generation', 'status': 'completed', 'priority': 1},
    {'employee': 'carol', 'task': 'server_maintenance', 'status': 'completed', 'priority': 4},
    {'employee': 'bob', 'task': 'security_patch', 'status': 'completed', 'priority': 5},
    {'employee': 'carol', 'task': 'backup', 'status': 'failed', 'priority': 2},
    {'employee': 'alice', 'task': 'api_deployment', 'status': 'completed', 'priority': 4}
]

# Track stats per employee
completion_count = defaultdict(int)
failure_count = defaultdict(int)
priority_weighted_score = defaultdict(float)
bonus_awarded = defaultdict(bool)

# Distractor: unused structure for time tracking
timing_analysis = defaultdict(list)
baseline_times = [12.5, 14.2, 11.8, 15.1, 13.7]

for log in task_logs:
    emp = log['employee']
    status = log['status']
    priority = log['priority']

    if status == 'completed':
        completion_count[emp] += 1
        priority_weighted_score[emp] += 1.5 * priority
        
        # Bonus logic (semi-relevant)
        if priority >= 4 and completion_count[emp] > 1:
            bonus_awarded[emp] = True
    else:
        failure_count[emp] += 1
        priority_weighted_score[emp] -= 0.5 * priority  # penalty

# Distractor: dead code path (never executed due to data)
phantom_employee = 'dave'
if phantom_employee in completion_count and len(bonus_awarded) > 10:
    priority_weighted_score[phantom_employee] = 999

# Compute efficiency ratios (some used, some not)
efficiency_ratio = {}
for emp in completion_count:
    total_tasks = completion_count[emp] + failure_count[emp]
    efficiency_ratio[emp] = completion_count[emp] / total_tasks if total_tasks > 0 else 0

# Unused distractor calculation
idle_time_estimate = sum([x * 0.7 for x in range(1, len(task_logs))])

# Aggregate final performance score
base_performance = sum(priority_weighted_score.values())
extra_bonus = 10 if any(bonus_awarded.values()) else 0
penalty_factor = len([f for f in failure_count.values() if f >= 2]) * 3

# Final score computation with conditional expression
intermediate_total = base_performance + extra_bonus - penalty_factor
final_score = intermediate_total if intermediate_total > 0 else 0

# Semi-relevant list comprehension: get high-priority completed tasks
high_priority_done = [t for t in task_logs if t['priority'] > 3 and t['status'] == 'completed']
productivity_index = len(high_priority_done) * efficiency_ratio.get('alice', 0)

# Output result as required
print(f"Result: {final_score}")