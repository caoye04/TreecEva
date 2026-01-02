from collections import defaultdict

# Simulate employee task completion and performance scoring
task_difficulty = {'data_cleaning': 2, 'model_training': 5, 'report_generation': 3}
completed_tasks = ['data_cleaning', 'model_training', 'data_cleaning']

# Count how many times each task was completed
task_count = defaultdict(int)
for task in completed_tasks:
    task_count[task] += 1

# Base score calculation based on task repetitions and difficulty
base_score = 0
for task, count in task_count.items():
    base_score += count * task_difficulty.get(task, 1)

# Bonus logic based on conditional expression
bonus_awarded = 1.5 if len(completed_tasks) > 2 and task_count['data_cleaning'] >= 2 else 1.0

# Final performance score computation
def calculate_performance(multiplier):
    return int(base_score * multiplier) + (10 if multiplier > 1.2 else 0)

final_score = calculate_performance(bonus_awarded)
print(f"Target result: {final_score}")