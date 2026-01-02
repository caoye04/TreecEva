from collections import defaultdict

# Simulate employee task logs over a week
task_logs = [
    ('Alice', 'task1', 'complete'), ('Bob', 'task2', 'failed'),
    ('Alice', 'task3', 'complete'), ('Charlie', 'task4', 'complete'),
    ('Bob', 'task5', 'complete'), ('Alice', 'task6', 'failed'),
    ('Charlie', 'task7', 'failed'), ('Bob', 'task8', 'complete')
]

# Aggregate productivity and error counts
productivity = defaultdict(int)
errors = defaultdict(int)
wasteful_counter = defaultdict(lambda: 0)  # Distractor: not used in final logic

for name, task, status in task_logs:
    if status == 'complete':
        productivity[name] += 1
    else:
        errors[name] += 1

    # Irrelevant computation - increases cognitive load
    wasteful_counter[status] += 1

# Apply arbitrary weight adjustments (semi-relevant)
adjusted_productivity = {}
for name in productivity:
    bonus = 1 if productivity[name] >= 2 else 0  # Threshold bonus
    adjusted_productivity[name] = productivity[name] + bonus

# Misleading intermediate calculation
phantom_efficiency = {}
for name in productivity:
    total_tasks = productivity[name] + errors[name]
    if total_tasks > 0:
        phantom_efficiency[name] = (productivity[name] / total_tasks) * 100
    else:
        phantom_efficiency[name] = 0

# Core evaluation function
def evaluate_performance(prod, err):
    score = 0
    for name in prod:
        base = prod[name] * 10
        penalty = err.get(name, 0) * 15  # Higher penalty for errors
        individual_score = base - penalty

        # Additional logic to increase nesting depth
        if individual_score < 0:
            individual_score = 5  # Minimum floor score
        elif individual_score > 50:
            individual_score = 50  # Cap at 50

        score += individual_score

        # Dead code path - never executed due to prior constraints
        if individual_score > 100:
            score -= 10  # This line is unreachable

    return score

# Compute final score
final_score = evaluate_performance(adjusted_productivity, errors)

# Print result as required
print(f"Result: {final_score}")