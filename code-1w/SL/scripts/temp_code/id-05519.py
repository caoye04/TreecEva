from collections import defaultdict
import math

# Simulate employee task logs with redundant metadata
task_logs = [
    {'employee': 'Alice', 'tasks': 8, 'errors': 1, 'overtime_hours': 5},
    {'employee': 'Bob', 'tasks': 12, 'errors': 3, 'overtime_hours': 8},
    {'employee': 'Charlie', 'tasks': 15, 'errors': 0, 'overtime_hours': 3},
    {'employee': 'Diana', 'tasks': 6, 'errors': 2, 'overtime_hours': 10}
]

# Irrelevant aggregation: total hours worked (not used in final score)
hourly_data = defaultdict(int)
for log in task_logs:
    hourly_data[log['employee']] += log['tasks'] * 1.5 + log['overtime_hours']

# Compute productivity ratio: tasks per error (with special case for zero errors)
def compute_productivity(tasks, errors):
    if errors == 0:
        return tasks + 10  # Bonus for no errors
    return tasks / errors

# Misleading risk assessment based on overtime (partially relevant)
def assess_risk(overtime_hours, tasks):
    stress_index = overtime_hours / (tasks + 1)
    risk_lookup = {0: 0.1, 1: 0.3, 2: 0.5, 3: 0.7, 4: 0.9}
    base_risk = risk_lookup.get(int(stress_index), 1.0)
    return base_risk * 1.2

# Auxiliary function to filter high performers (used indirectly)
is_high_performer = lambda tasks, errors: tasks >= 10 and errors <= 1

# List comprehension to extract performance tuples
performance_data = [
    (log['tasks'], log['errors'], log['overtime_hours']) 
    for log in task_logs 
    if is_high_performer(log['tasks'], log['errors'])
]

# Compute average productivity for qualified employees
productivity_list = [
    compute_productivity(p[0], p[1]) 
    for p in performance_data
]
avg_productivity = sum(productivity_list) / len(productivity_list) if productivity_list else 0

# Compute composite risk factor from all logs (some irrelevant entries)
risk_accumulator = 0
for log in task_logs:
    individual_risk = assess_risk(log['overtime_hours'], log['tasks'])
    risk_accumulator += individual_risk * 0.25
risk_factor = max(risk_accumulator, 0.5)

# Dead code: unused efficiency metric
efficiency_scores = [p[0] / (p[2] + 1) for p in performance_data]  # Not used

# Core evaluation logic
productivity = avg_productivity

# Final scoring with non-linear transformation
def evaluate_performance(prod, risk):
    adjusted = prod * (1.5 - risk)
    penalty = math.log(1 + risk * 2)
    return round(adjusted - penalty, 4)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Output result
print(f"Result: {final_score}")