from itertools import combinations

# Simulate employee task completion data
task_difficulty = [3, 5, 2, 8, 7]
employee_efficiency = {'alice': 6, 'bob': 4, 'charlie': 7}
completed_tasks = {
    'alice': [True, False, True, True, False],
    'bob': [False, True, True, False, True],
    'charlie': [True, True, False, True, True]
}

# Auxiliary tracking variables (some are distractions)
total_evaluations = 0
redundant_sum = 0
intermediate_cache = []
useless_counter = 0

# Distractor: Precompute irrelevant efficiency scores
for name, eff in employee_efficiency.items():
    for i in range(len(task_difficulty)):
        if eff > task_difficulty[i]:
            redundant_sum += eff - task_difficulty[i]
        useless_counter += 1  # Dead use

# Real logic begins: compute weighted performance
base_scores = {}
for name, tasks in completed_tasks.items():
    score = 0
    for i, completed in enumerate(tasks):
        if completed:
            # Reward based on difficulty and individual efficiency
            bonus = 1 if employee_efficiency[name] >= task_difficulty[i] else 0
            score += task_difficulty[i] + bonus
    base_scores[name] = score

# Use slicing to analyze recent task trends (last 3 tasks)
recent_impact = {}
for name, tasks in completed_tasks.items():
    recent_tasks = tasks[-3:]  # Focus on last 3
    recent_difficulties = task_difficulty[-3:]
    recent_score = 0
    for i, completed in enumerate(recent_tasks):
        if completed:
            recent_score += recent_difficulties[i]
    recent_impact[name] = recent_score * 0.8  # Weighted recency factor

# Combine base and recent scores with conditional adjustment
adjustment_factor = 1.2
if base_scores['alice'] > base_scores['bob']:
    adjustment_factor *= 1.1

# Compute composite scores
composite_scores = {}
for name in employee_efficiency:
    raw = base_scores[name] + recent_impact[name]
    if name == 'charlie':
        raw *= adjustment_factor  # Extra motivation boost
    composite_scores[name] = raw

# Final evaluation using combinatorics: find optimal pair collaboration
best_pair_value = 0
for pair in combinations(composite_scores.keys(), 2):
    combined_eff = (composite_scores[pair[0]] + composite_scores[pair[1]]) / 2
    if combined_eff > best_pair_value:
        best_pair_value = combined_eff

# Critical statement
final_score = int(composite_scores['charlie'] - best_pair_value + 5)

# Tracking evaluations (distractor)
total_evaluations += 1
intermediate_cache.append(final_score)

print(f"Result: {final_score}")