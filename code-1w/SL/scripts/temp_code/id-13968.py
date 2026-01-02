from itertools import combinations

# Simulated benchmark data for code reasoning tasks
task_difficulties = [2, 3, 5, 7, 11, 13]
scores = [85, 90, 78, 92, 88, 76]
execution_times = [1.2, 0.9, 1.5, 0.8, 1.1, 1.3]

# Irrelevant distraction variables
dummy_weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
temp_results = []
for i in range(len(dummy_weights)):
    temp_results.append(scores[i] * dummy_weights[i])

# Hidden relationship: performance depends on prime-aligned high performers
prime_high_performers = []
for i in range(len(task_difficulties)):
    if task_difficulties[i] in {2, 3, 5, 7, 11, 13} and scores[i] >= 85:
        prime_high_performers.append(i)

# Distractor: unused function
def unused_aggregator(data):
    return sum(x * 0.1 for x in data if x > 50)

# Real logic begins: find all pairs of top performers on prime tasks
candidate_pairs = list(combinations(prime_high_performers, 2))
bonus_awarded = 0
for pair in candidate_pairs:
    idx1, idx2 = pair
    time_diff = abs(execution_times[idx1] - execution_times[idx2])
    if time_diff < 0.5:
        bonus_awarded += 5

# Secondary computation path with partial relevance
efficiency_ratings = []
for i in range(len(execution_times)):
    rating = scores[i] / execution_times[i]
    efficiency_ratings.append(round(rating, 2))

# Misleading average calculation (not used directly)
avg_efficiency = sum(efficiency_ratings) / len(efficiency_ratings)
adjusted_base = sum(score for i, score in enumerate(scores) if i in prime_high_performers)

# Core formula obscured by intermediate steps
penalty = 0
for i in prime_high_performers:
    if execution_times[i] > 1.0:
        penalty += 2

base_performance = adjusted_base + bonus_awarded - penalty

# Final adjustment using lambda transformation (only some values contribute)
contribution_filter = lambda x: x >= 85
relevant_scores = list(filter(contribution_filter, scores))
final_multiplier = 1.1 if len(relevant_scores) > 4 else 1.0

# Critical statement
final_score = calculate_performance(benchmark_data)

# Helper function defined after use (adds cognitive load)
def calculate_performance(data):
    return int((base_performance * final_multiplier) + 0.5)  # Rounded integer result

# Data structure to satisfy forward reference
benchmark_data = {
    'tasks': task_difficulties,
    'scores': scores,
    'times': execution_times
}

# Print result for evaluation
Result: {final_score}