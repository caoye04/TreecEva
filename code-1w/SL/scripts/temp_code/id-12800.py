from collections import defaultdict

# Simulate employee task logs with redundant data
task_logs = [
    ('Alice', 'task1', 'complete'), ('Bob', 'task2', 'failed'),
    ('Alice', 'task3', 'complete'), ('Charlie', 'task4', 'complete'),
    ('Bob', 'task5', 'complete'), ('Alice', 'task6', 'failed'),
    ('Charlie', 'task7', 'failed'), ('Bob', 'task8', 'complete')
]

# Irrelevant frequency counter for task statuses (distractor)
status_count = defaultdict(int)
for _, _, status in task_logs:
    status_count[status] += 1

# Extract productivity per employee (relevant)
productivity = defaultdict(int)
errors = defaultdict(int)
for name, _, status in task_logs:
    if status == 'complete':
        productivity[name] += 1
    else:
        errors[name] += 1

# Misleading normalization attempt (not used later)
normalized_productivity = {}
total_tasks = len(task_logs)
for name in productivity:
    normalized_productivity[name] = productivity[name] / total_tasks

# Compute raw totals (some are unused)
employee_totals = {name: productivity[name] + errors[name] for name in set(n for n, _, _ in task_logs)}

# Introduce unrelated string processing (distractor)
names_upper = [name.upper() for name in productivity.keys()]
name_initals = [name[0] + '.' for name in names_upper]

# Create a red herring set operation (irrelevant)
unique_statuses = set(status for _, _, status in task_logs)
completion_set = {'complete'}
dropped_set = unique_statuses - completion_set

# Compute error rate per employee (relevant)
error_rate = {}
for name in productivity:
    total = productivity[name] + errors[name]
    error_rate[name] = errors[name] / total if total > 0 else 0.0

# Another distraction: simulate workload distribution (unused)
workload = defaultdict(float)
for name, _, status in task_logs:
    workload[name] += 1.5 if status == 'failed' else 1.0

# Key function combining arithmetic and logic
def evaluate_performance(prod_dict, err_dict):
    scores = []
    scaling_factor = 10
    penalty_weight = 0.4
    
    # Loop through each employee (nested logic)
    for emp in prod_dict:
        base_score = prod_dict[emp] * scaling_factor
        penalty = int(err_dict[emp] * 100) * penalty_weight
        adjusted = base_score - penalty
        
        # Conditional bonus for high productivity (additional logic step)
        if prod_dict[emp] >= 2:
            adjusted += 5
        
        # Artificial cap (distractor, but doesn't trigger)
        if adjusted > 50:
            adjusted = 50  # This path not taken
            
        scores.append(adjusted)
    
    # Final aggregation using sum and rounding (critical step)
    aggregate = sum(scores)
    return round(aggregate, 2)

# Execute key statement
target_employee = 'Alice'
partial_result = evaluate_performance({'Alice': 2}, {'Alice': 1})
final_score = evaluate_performance(productivity, error_rate)

print(f"Result: {final_score}")