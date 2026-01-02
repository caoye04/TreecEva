def analyze_performance(metrics):
    # Irrelevant transformation (distractor)
    normalized = {k: v * 1.1 for k, v in metrics.items() if v < 50}
    adjusted = {}
    for key, val in metrics.items():
        if val >= 30:
            adjusted[key] = val * 0.95
        else:
            adjusted[key] = val * 1.05

    # Semi-relevant aggregation
    avg_metric = sum(metrics.values()) / len(metrics)
    bonus = 0
    if avg_metric > 40:
        bonus = 10

    return adjusted, bonus


def track_efficiency(logs):
    counts = {}
    for entry in logs:
        category = entry.get('type', 'unknown')
        counts[category] = counts.get(category, 0) + 1
    # Dead code path - never used later (distractor)
    if 'error' in counts and counts['error'] > 5:
        return -1
    return len(logs)

# Main data
stats_dict = {
    'response_time': 45,
    'throughput': 52,
    'error_rate': 28,
    'availability': 99,
    'latency': 37
}

# Auxiliary data (partially irrelevant)
log_entries = [
    {'type': 'info', 'code': 200},
    {'type': 'warning', 'code': 404},
    {'type': 'info', 'code': 200},
    {'type': 'error', 'code': 500},
    {'type': 'info', 'code': 200}
]

# Intermediate processing with distraction
adjusted_metrics, performance_bonus = analyze_performance(stats_dict)
log_size = track_efficiency(log_entries)

# Misleading calculation (not part of final result)
counterfeit_score = 0
for k, v in stats_dict.items():
    if 'time' in k or 'rate' in k:
        counterfeit_score += v // 2

# Core logic chain begins
base_score = 0
penalty = 0
for key, value in stats_dict.items():
    if key == 'availability':
        base_score += value * 0.5
    elif 'time' in key or 'latency' in key:
        base_score += 100 - value
    elif 'throughput' in key:
        base_score += value * 0.8
    else:
        base_score += value * 0.3

    # Additional penalty branch
    if value < 30:
        penalty += 5

net_base = base_score - penalty

# Secondary adjustment using dictionary operations
multipliers = {'response_time': 1.1, 'throughput': 1.2, 'latency': 0.9}
total_multiplier_effect = 0
for k in stats_dict:
    if k in multipliers:
        total_multiplier_effect += multipliers[k]

# Final computation
final_score = int(net_base + performance_bonus - total_multiplier_effect * 2)

print(f"Result: {final_score}")