from collections import defaultdict
from itertools import combinations

# Simulate employee task completion data
task_difficulty = [3, 5, 2, 8, 7]
employee_tasks = {
    'alice': [True, False, True, True, False],
    'bob': [True, True, False, False, True],
    'charlie': [False, True, True, True, True]
}

# Irrelevant distraction: unused function
def unused_helper(x):
    return x ** 2 + 3 * x - 1

# Misleading intermediate calculation (not used in final result)
total_possible_points = sum(task_difficulty) * len(employee_tasks)
avg_completion_rate = 0.0  # Placeholder for distraction

# State tracker for performance
performance_log = defaultdict(float)
penalty_counter = 0

for emp, completions in employee_tasks.items():
    raw_score = 0
    bonus_applied = False

    for i, completed in enumerate(completions):
        if completed:
            raw_score += task_difficulty[i]
            # Apply bonus if difficult task (>6) is completed early (index < 3)
            if task_difficulty[i] > 6 and i < 3 and not bonus_applied:
                raw_score += 5
                bonus_applied = True

    # Deduct penalty for incomplete high-priority tasks (difficulty >= 7)
    for i, completed in enumerate(completions):
        if not completed and task_difficulty[i] >= 7:
            raw_score -= 3
            penalty_counter += 1  # Tracked but not used directly

    performance_log[emp] = raw_score

# Secondary processing with combinatorics distraction
pair_ranks = []
for pair in combinations(performance_log.keys(), 2):
    diff = abs(performance_log[pair[0]] - performance_log[pair[1]])
    pair_ranks.append((pair, diff))

# Actual computation path
base_total = sum(performance_log.values())
adjustment_factor = len([d for d in task_difficulty if d >= 5])

# Final performance rating with conditional logic
if base_total > 30:
    final_score = base_total - adjustment_factor
else:
    final_score = base_total + adjustment_factor

Result: {final_score}