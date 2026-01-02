def calculate_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * log2(prob)
    return entropy

# Simulate performance metrics across different departments
dept_a = [88, 92, 75, 85, 90]
dept_b = [70, 80, 85, 78, 82]
dept_c = [95, 90, 93, 88, 91]

# Irrelevant intermediate calculations (distractors)
avg_a = sum(dept_a) / len(dept_a)
avg_b = sum(dept_b) / len(dept_b)
avg_c = sum(dept_c) / len(dept_c)

combined_performance = dept_a + dept_b + dept_c
performance_variance = sum((x - sum(combined_performance)/len(combined_performance))**2 for x in combined_performance) / len(combined_performance)

# Entropy-based weight adjustment (not used in final path but looks relevant)
entropy_weights = {
    'A': calculate_entropy(dept_a),
    'B': calculate_entropy(dept_b),
    'C': calculate_entropy(dept_c)
}

# Key data structure with rankings and efficiency ratios
rank_data = {
    'team_x': {'rank': 3, 'efficiency': 0.88, 'base_points': 85},
    'team_y': {'rank': 1, 'efficiency': 0.94, 'base_points': 92},
    'team_z': {'rank': 2, 'efficiency': 0.90, 'base_points': 89}
}

# Bonus logic with red herring computations
base_bonus_pool = 150
utilized_pool = 0
bonus_per_rank = {}
for team, data in rank_data.items():
    # Complex but unused bonus allocation attempt
    bonus_per_rank[team] = base_bonus_pool * (1 / data['rank'])
    utilized_pool += bonus_per_rank[team] / 10

scaling_factor = 1.05
adjustment_log = []  # Dead variable - never used again

# Real computation begins: weighted score based on rank and efficiency
effective_scores = {}
for team, data in rank_data.items():
    raw_score = data['base_points'] * data['efficiency']
    rank_penalty = (data['rank'] - 1) * 2.5
    adjusted_score = raw_score - rank_penalty
    effective_scores[team] = max(adjusted_score, 0)

# Determine bonus multiplier from highest performer
best_base = max(data['base_points'] for data in rank_data.values())
bonus_multiplier = 1 + (best_base - 85) * 0.01

# Secondary adjustment using dictionary operations
multiplier_map = {1: 1.2, 2: 1.1, 3: 1.05}
rank_boost = multiplier_map.get(min(data['rank'] for data in rank_data.values()), 1.0)

# Final aggregation with unnecessary complexity
total_effective = sum(effective_scores.values())
score_mean = total_effective / len(effective_scores)
deviation_penalty = 0
for score in effective_scores.values():
    if score < score_mean:
        deviation_penalty += (score_mean - score) * 0.1

# Core answer computation
final_score = 0
for team, score in effective_scores.items():
    contribution = score * bonus_multiplier
    if rank_data[team]['rank'] == 1:
        contribution *= rank_boost  # Extra boost for rank 1
    final_score += contribution

# Normalize by number of teams to avoid inflation
final_score /= len(effective_scores)

# Output result as required
print(f"Result: {final_score}")