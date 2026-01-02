from collections import defaultdict
from itertools import combinations

# Simulate employee task logs over a workday
task_logs = [
    ('login', 9), ('data_entry', 54), ('meeting', 60), ('coding', 120),
    ('break', 15), ('review', 45), ('logout', 10)
]

# Process raw time-on-task data
daily_minutes = defaultdict(int)
for task, duration in task_logs:
    daily_minutes[task] += duration

# Compute total active work time (exclude breaks and login/logout)
active_tasks = {k: v for k, v in daily_minutes.items() if k not in ['break', 'login', 'logout']}
total_work_time = sum(active_tasks.values())

# Calculate productivity score with diminishing returns after 200 minutes
time_bonus = min(total_work_time, 200) * 1.2
overtime_penalty = max(0, total_work_time - 240) * 0.8
productivity = time_bonus - overtime_penalty

# Assess risk factor based on task diversity
task_diversity = len(active_tasks)
risk_factor = 0
if task_diversity == 1:
    risk_factor = 50
elif task_diversity <= 2:
    risk_factor = 20
else:
    risk_factor = 5

# Distractor: Analyze break patterns (not used in final score)
break_count = sum(1 for t, _ in task_logs if t == 'break')
avg_break_length = daily_minutes['break'] / break_count if break_count else 0
alertness_metric = 100 - (avg_break_length * 2)

# Distractor: Generate all possible task pairs (unused)
all_task_pairs = list(combinations(active_tasks.keys(), 2))
pair_complexity = len(all_task_pairs) * 1.5 if len(all_task_pairs) > 3 else 0

# Core evaluation logic
def evaluate_performance(prod, risk):
    base_score = prod * 0.9
    adjusted = base_score - risk * 2.5
    # Apply floor to prevent negative scores
    return max(adjusted, 10)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Additional distractor variables
theoretical_max = evaluate_performance(200 * 1.2, 5)
efficiency_ratio = final_score / theoretical_max if theoretical_max else 0

print(f"Result: {final_score}")