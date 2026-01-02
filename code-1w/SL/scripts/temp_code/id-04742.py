from collections import defaultdict

# Simulate employee task logs with productivity metrics
task_logs = [
    {'employee': 'Alice', 'tasks_completed': 8, 'errors': 1, 'overtime_hours': 2},
    {'employee': 'Bob', 'tasks_completed': 5, 'errors': 3, 'overtime_hours': 5},
    {'employee': 'Charlie', 'tasks_completed': 10, 'errors': 0, 'overtime_hours': 1},
    {'employee': 'Diana', 'tasks_completed': 7, 'errors': 2, 'overtime_hours': 3}
]

# Track department-wise stats (semi-relevant for distraction)
department_stats = defaultdict(lambda: {'tasks': 0, 'errors': 0})
for log in task_logs:
    dept = 'Engineering' if log['employee'] in ['Alice', 'Charlie'] else 'Support'
    department_stats[dept]['tasks'] += log['tasks_completed']
    department_stats[dept]['errors'] += log['errors']

# Compute individual productivity scores
productivity_scores = {}
for log in task_logs:
    base_productivity = log['tasks_completed'] * 10
    penalty = log['errors'] * 15
    overtime_bonus = min(log['overtime_hours'] * 5, 20)  # Diminishing returns
    score = base_productivity - penalty + overtime_bonus
    productivity_scores[log['employee']] = max(score, 0)

# Misleading intermediate calculation (distraction)
avg_overtime = sum(log['overtime_hours'] for log in task_logs) / len(task_logs)
phantom_risk = avg_overtime * 0.5  # Not actually used later

# Determine risk factor based on error rate (relevant)
total_tasks = sum(log['tasks_completed'] for log in task_logs)
total_errors = sum(log['errors'] for log in task_logs)
error_rate = total_errors / total_tasks if total_tasks > 0 else 0
risk_factor = int(error_rate * 100)

# Apply conditional adjustment to risk (relevant)
if risk_factor < 5:
    risk_factor = risk_factor * 0.8
else:
    risk_factor = risk_factor * 1.2

# Aggregate productivity for top performers (relevant)
top_threshold = 80
high_performers = [score for score in productivity_scores.values() if score >= top_threshold]
productivity = sum(high_performers) if high_performers else 0

# Dead code path (distractor)
if phantom_risk > 100:
    productivity *= 0.9  # Never executed

# Core evaluation function
def evaluate_performance(prod, risk):
    if prod == 0:
        return 0
    efficiency_ratio = prod / (1 + risk)
    stability_modifier = 1.0
    if risk < 10:
        stability_modifier = 1.1
    elif risk > 20:
        stability_modifier = 0.9
    final = efficiency_ratio * stability_modifier
    return round(final, 2)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result for inspection
print(f"Result: {final_score}")