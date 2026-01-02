from collections import defaultdict

# Simulate employee task completion data
task_complexity = [3, 5, 2, 8, 7]
completion_times = [4, 6, 3, 9, 8]  # in hours
base_efficiency = 4.5

# Irrelevant metrics (distractors)
stress_levels = [60, 75, 50, 95, 80]  # arbitrary stress units
distraction_count = [12, 18, 8, 25, 20]
ambient_temperature = 22.5  # room temp, unused

# Data structure for aggregated performance
performance_log = defaultdict(lambda: 0)
efficiency_map = {i: (task_complexity[i] / completion_times[i]) for i in range(len(task_complexity))}

# Compute baseline adjusted efficiency
adjusted_efficiency = []
for i in range(len(efficiency_map)):
    adj_val = efficiency_map[i] * (base_efficiency / (i + 1)) if i > 0 else efficiency_map[i]
    adjusted_efficiency.append(round(adj_val, 3))

# Secondary processing with red herring calculations
phantom_score = 0
for temp in stress_levels:
    phantom_score += temp * 0.1  # unrelated computation

# More distraction: modeling nonexistent 'focus decay'
focus_decay = 0.0
for count in distraction_count:
    focus_decay += count * 0.05

# Real logic begins: normalize adjusted efficiency
normalized_scores = [score / sum(adjusted_efficiency) * 100 for score in adjusted_efficiency]

# Aggregate into performance log
for idx, score in enumerate(normalized_scores):
    performance_log[f'task_{idx}'] = score

# Apply conditional boost for high-complexity tasks
complexity_boost = 0.0
boost_applied = False
for i in range(len(task_complexity)):
    if task_complexity[i] >= 7 and normalized_scores[i] > 15:
        complexity_boost += normalized_scores[i] * 0.1
        boost_applied = True

if boost_applied:
    for i in range(len(normalized_scores)):
        normalized_scores[i] += complexity_boost / len(normalized_scores)

# Introduce lambda-based filtering (semi-relevant)
valid_performance = list(filter(lambda x: x > 10, normalized_scores))

# Final scoring logic
raw_total = sum(valid_performance)
penalty = len([x for x in completion_times if x > 7]) * 1.5  # penalty for slow tasks

# Distractor: unused bonus mechanism
potential_bonus = sum([1 for c in task_complexity if c <= 2]) * 2

# Actual final score calculation
def calculate_performance_rating():
    base = raw_total - penalty
    if len(valid_performance) >= 3:
        base *= 1.1  # consistency bonus
    return round(base, 2)

final_score = calculate_performance_rating()
print(f"Result: {final_score}")