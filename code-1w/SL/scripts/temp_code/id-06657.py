from collections import defaultdict

# Simulate employee task tracking and performance evaluation
task_logs = [
    {'employee': 'Alice', 'tasks_completed': 8, 'errors': 1, 'overtime_hours': 5},
    {'employee': 'Bob', 'tasks_completed': 12, 'errors': 3, 'overtime_hours': 8},
    {'employee': 'Charlie', 'tasks_completed': 15, 'errors': 0, 'overtime_hours': 3},
    {'employee': 'Diana', 'tasks_completed': 6, 'errors': 2, 'overtime_hours': 10}
]

# Aggregate data by employee using defaultdict
employee_stats = defaultdict(lambda: {'tasks': 0, 'errors': 0, 'overtime': 0})
for log in task_logs:
    emp = log['employee']
    employee_stats[emp]['tasks'] += log['tasks_completed']
    employee_stats[emp]['errors'] += log['errors']
    employee_stats[emp]['overtime'] += log['overtime_hours']

# Compute productivity scores with some irrelevant intermediate metrics
total_tasks = sum(log['tasks_completed'] for log in task_logs)
total_errors = sum(log['errors'] for log in task_logs)
baseline_efficiency = total_tasks / (total_errors + 1) if total_errors > 0 else total_tasks

productivity = {}
waste_metrics = {}  # Distractor: not used later
for emp, stats in employee_stats.items():
    raw_productivity = stats['tasks'] * 10
    penalty = stats['errors'] * 15
    overtime_cost = stats['overtime'] * 2  # Semi-relevant but downweighted
    productivity[emp] = raw_productivity - penalty
    waste_metrics[emp] = overtime_cost + penalty  # Dead-end computation

# Compute team averages for distraction
avg_productivity = sum(productivity.values()) / len(productivity)
avg_waste = sum(waste_metrics.values()) / len(waste_metrics)  # Unused

# Risk assessment based on error rate and overtime
risk_factor = {}
for emp, stats in employee_stats.items():
    error_rate = stats['errors'] / stats['tasks'] if stats['tasks'] > 0 else 0
    overtime_ratio = stats['overtime'] / 40  # Normalize to workweek
    risk_factor[emp] = round(error_rate * 1.5 + overtime_ratio * 0.5, 4)

# Misleading secondary analysis: skill diversity index (not used)
skill_diversity = {}
for log in task_logs:
    diversity_score = (log['tasks_completed'] ** 0.5) / (log['errors'] + 1)
    skill_diversity[log['employee']] = diversity_score  # Never used

# Core evaluation function
def evaluate_performance(prod_dict, risk_dict):
    weighted_scores = []
    scaling_factor = 0.8  # Internal adjustment
    for emp in prod_dict:
        # Final score: scaled productivity adjusted by risk
        adj_score = prod_dict[emp] * (1 - risk_dict[emp]) * scaling_factor
        weighted_scores.append(adj_score)
    
    # Aggregate final score as sum of adjusted values
    aggregate = sum(weighted_scores)
    
    # Additional irrelevant normalization
    max_possible = max(weighted_scores) if weighted_scores else 0
    normalized_agg = aggregate / max_possible if max_possible != 0 else 0  # Not used
    
    return int(round(aggregate))

# Execute main logic
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")