from itertools import combinations

# Simulate employee task performance evaluation
base_points = 85
task_completion_times = [12.5, 14.3, 9.8, 15.1, 11.7]
error_rates = [0.02, 0.05, 0.01, 0.07, 0.03]
bonus_multiplier = 1.1
penalty_factor = 0.9

# Irrelevant metrics (distractors)
idle_time_records = [3.2, 4.1, 2.8, 5.0, 3.6]
coffee_breaks_taken = 4
team_size = 5
hypothetical_bonus = 15

# Compute adjusted scores per task
adjusted_scores = []
for i in range(len(task_completion_times)):
    time_score = max(0, 100 - task_completion_times[i])
    error_penalty = error_rates[i] * 50
    raw_score = time_score - error_penalty
    adjusted_scores.append(max(raw_score, 0))

# Determine rank based on top-2 average using combinations
best_pair_avg = 0
for pair in combinations(adjusted_scores, 2):
    avg_pair = sum(pair) / 2
    if avg_pair > best_pair_avg:
        best_pair_avg = avg_pair

rank = 1 if best_pair_avg >= 80 else 2 if best_pair_avg >= 70 else 3

# Additional irrelevant computation (dead path)
dummy_aggregates = []
for window in range(1, 4):
    for start in range(len(adjusted_scores) - window + 1):
        segment = adjusted_scores[start:start+window]
        dummy_aggregates.append(sum(segment) / len(segment))

# Unused state tracking
state_log = []
counter = 0
for score in adjusted_scores:
    if score > 75:
        state_log.append((counter, 'high'))
    elif score > 60:
        state_log.append((counter, 'medium'))
    else:
        state_log.append((counter, 'low'))
    counter += 1

# Core logic: evaluate performance based on rank and base points
def evaluate_performance(rank, base):
    modifiers = {1: 1.2, 2: 1.0, 3: 0.8}
    return int(base * modifiers[rank])

# Critical statement
final_score = evaluate_performance(rank, base_points)

# Print result
print(f"Result: {final_score}")