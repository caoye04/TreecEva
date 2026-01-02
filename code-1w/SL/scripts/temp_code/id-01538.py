def analyze_efficiency(values):
    sorted_vals = sorted(values)
    median = sorted_vals[len(sorted_vals) // 2]
    normalized = [v / (median + 1e-5) for v in values]
    efficiency = sum(normalized)
    return efficiency


def track_progress(metrics):
    cumulative = 0
    progression = []
    for m in metrics:
        cumulative += m * 0.85
        progression.append(cumulative)
    smoothed = [p * 0.9 for p in progression]
    return smoothed[-1] if smoothed else 0

# Simulate daily productivity metrics over a work cycle
daily_output = [12, 15, 10, 18, 22, 14, 19, 24, 16, 13]
overhead_costs = [2.1, 1.8, 2.5, 1.7, 1.9, 2.3, 2.0, 1.6, 2.4, 2.2]
adjusted_productivity = []

for i in range(len(daily_output)):
    adj_val = (daily_output[i] - overhead_costs[i]) * 1.1
    adjusted_productivity.append(max(adj_val, 0))

# Compute efficiency index
efficiency_index = analyze_efficiency(adjusted_productivity)

# Track trend progression
trend_score = track_progress(adjusted_productivity)

# Define risk thresholds and safe zones
risk_levels = {1: 'low', 2: 'medium', 3: 'high'}
critical_thresholds = [10, 15, 20]
risk_set = set()
for val in adjusted_productivity:
    if val < critical_thresholds[0]:
        risk_set.add('minimal')
    elif val > critical_thresholds[2]:
        risk_set.add('extreme')
    if val > critical_thresholds[1]:
        risk_set.add('elevated')

# Misleading distraction: unused health metrics
temporal_weights = [0.95**i for i in range(len(adjusted_productivity))]
weighted_sum = sum(adjusted_productivity[i] * temporal_weights[i] for i in range(len(adjusted_productivity)))
average_decay = weighted_sum / len(temporal_weights)
phantom_buffer = [x * 0.1 for x in adjusted_productivity if x > 18]

# Core evaluation logic
productivity = efficiency_index + trend_score

# Secondary distraction: redundant list processing
duplicate_check = [x for x in adjusted_productivity if adjusted_productivity.count(x) > 1]
unique_count = len(set(adjusted_productivity))

# Final performance model
def evaluate_performance(p, risks):
    base = p * 0.75
    penalty = 0
    if 'extreme' in risks:
        penalty += 12
    if 'elevated' in risks:
        penalty += 5
    if len(risks) >= 2:
        penalty += 3
    return base - penalty

final_score = evaluate_performance(productivity, risk_set)

# Distraction: unused auxiliary calculation
projected_growth = final_score * 1.08
buffer_reserve = sum(overhead_costs) * 0.5

print(f"Result: {final_score}")