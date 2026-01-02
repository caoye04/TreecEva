def analyze_performance(metrics):
    base_score = 0
    penalty = 0
    temp_offset = 0

    for metric in metrics:
        if metric['value'] > 80:
            base_score += 10
        elif metric['value'] > 60:
            base_score += 5
        else:
            penalty += 2

        # Distractor: irrelevant computation
        temp_offset += len(metric['name']) % 3

    # Dead code path (never executed due to logic)
    if temp_offset > 100:
        base_score -= temp_offset // 10

    return base_score - penalty


def calculate_efficiency_ratio(data):
    total_ops = sum(d['ops'] for d in data)
    total_time = sum(d['time'] for d in data)
    return total_ops / total_time if total_time > 0 else 0

# Simulated input data
rank_data = [
    {'rank': 1, 'score': 95, 'active': True},
    {'rank': 2, 'score': 88, 'active': True},
    {'rank': 3, 'score': 76, 'active': False},
    {'rank': 4, 'score': 65, 'active': True}
]

bonus_multiplier = 1.5
baseline_adjustment = 0.85  # Unused in final logic
aux_counter = 0

# Irrelevant tracking variables
metric_log = []
for entry in rank_data:
    if entry['score'] >= 70:
        metric_log.append(f"High-{entry['rank']}")
    aux_counter += 1  # Incremented but not used

# Core logic with conditional expression
base_points = sum(10 if r['score'] >= 90 else 7 if r['score'] >= 80 else 5 for r in rank_data if r['active'])
score_boost = 20 if base_points > 25 else 10

# Secondary distraction: unused efficiency calculation
system_metrics = [
    {'ops': 120, 'time': 4},
    {'ops': 180, 'time': 6}
]
efficiency = calculate_efficiency_ratio(system_metrics)
scaling_factor = efficiency * 0.1  # Computed but irrelevant

# Final score depends only on base_points and bonus_multiplier
final_score = int((base_points * bonus_multiplier) + (score_boost if len([r for r in rank_data if r['active']]) >= 3 else 0))

# Print result as required
print(f"Result: {final_score}")