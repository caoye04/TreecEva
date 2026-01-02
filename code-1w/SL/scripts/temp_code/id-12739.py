from collections import defaultdict

# Simulate employee task completion data
task_data = [
    {'employee': 'Alice', 'tasks_completed': 8, 'errors': 1},
    {'employee': 'Bob', 'tasks_completed': 6, 'errors': 0},
    {'employee': 'Charlie', 'tasks_completed': 10, 'errors': 3}
]

# Irrelevant distraction: unused variable
temp_result = sum([t['tasks_completed'] for t in task_data])

# Compute performance baseline
base_scores = defaultdict(int)
for entry in task_data:
    name = entry['employee']
    base_scores[name] = entry['tasks_completed'] * 10 - entry['errors'] * 5

# Bonus logic based on error rate
get_bonus_factor = lambda errors, tasks: 1.5 if tasks > 0 and errors / tasks < 0.2 else 1.0

bonus_multiplier = get_bonus_factor(1, 8)  # Alice's error rate

# Final performance calculation
def calculate_performance(multiplier):
    total_base = sum(base_scores.values())
    adjusted = total_base * multiplier
    if adjusted > 200:
        return int(adjusted * 0.9)  # Apply efficiency discount
    return int(adjusted)

final_score = calculate_performance(bonus_multiplier)
print(f"Result: {final_score}")