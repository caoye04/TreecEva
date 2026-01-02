def analyze_performance(metrics):
    # Irrelevant transformation of metrics (distractor)
    normalized = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]
    adjusted = [n + 5 for n in normalized if n < 85]
    return sum(adjusted) // len(adjusted) if adjusted else 0

# Simulated input data from evaluation rounds
evaluation_data = [88, 72, 94, 63, 77, 81]
rankings = sorted(set([abs(100 - x) for x in evaluation_data]))  # Invert scores for ranking

# Bonus system based on performance tiers
bonus_tiers = {'excellent': 8, 'good': 5, 'average': 3}
bonus_weights = []
for rank in rankings:
    if rank <= 10:
        bonus_weights.append(bonus_tiers['excellent'])
    elif rank <= 20:
        bonus_weights.append(bonus_tiers['good'])
    else:
        bonus_weights.append(bonus_tiers['average'])

# Secondary analysis (mostly irrelevant to final result)
outlier_count = 0
for i in range(len(evaluation_data)):
    if abs(evaluation_data[i] - sum(evaluation_data) / len(evaluation_data)) > 15:
        outlier_count += 1

# Auxiliary function that computes secondary metric (unused)
def compute_efficiency(data):
    peak = max(data)
    avg = sum(data) / len(data)
    return round((avg / peak) * 100, 2)

# Core scoring logic
prev_ranks = [rankings[i] - rankings[i-1] for i in range(1, len(rankings))] if len(rankings) > 1 else [0]
trend_modifier = sum(prev_ranks) * 2 if sum(prev_ranks) > 10 else 5

# Final score calculation based on weighted bonuses and trend
base_points = sum(bonus_weights)
penalty_set = {x for x in rankings if x > 25}  # Set comprehension (required feature)
penalty = len(penalty_set) * 4

# Additional distractor: unused tuple unpacking
summary_stats = (min(rankings), max(rankings), len(rankings))
min_rank, max_rank, total_entries = summary_stats

# Actual answer computation
final_score = base_points + trend_modifier - penalty

# Print result as required
print(f"Result: {final_score}")