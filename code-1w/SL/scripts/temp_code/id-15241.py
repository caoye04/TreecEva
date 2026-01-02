def analyze_trend(values):
    trend = 0
    for v in values:
        if v > 0:
            trend += 1
        elif v < 0:
            trend -= 1
    return trend

# Simulate system health metrics over time
cpu_loads = [0.78, 0.82, 0.91, 0.88, 0.95]
memory_usage = [0.65, 0.70, 0.76, 0.72, 0.79]
disk_iops = [120, 135, 142, 138, 145]

# Normalize and create performance score array
normalized_scores = []
for i in range(len(cpu_loads)):
    score = (cpu_loads[i] * 0.5 + memory_usage[i] * 0.3) * 100
    normalized_scores.append(round(score, 2))

# Misleading auxiliary computation (distractor)
avg_response_time_ms = 245.6
latency_penalty = 0
if avg_response_time_ms > 200:
    latency_penalty = 10

# Another red herring: network jitter simulation
jitter_samples = [12.4, 15.1, 10.8, 18.3, 14.2]
jitter_avg = sum(jitter_samples) / len(jitter_samples)
jitter_impact = int(jitter_avg // 5)  # Unused downstream

# Extract directional trends as boolean flags
load_trend = analyze_trend([cpu_loads[i] - cpu_loads[i-1] for i in range(1, len(cpu_loads))])
memory_trend = analyze_trend([memory_usage[i] - memory_usage[i-1] for i in range(1, len(memory_usage))])

increasing_pressure = load_trend > 0 and memory_trend > 0
trend_multiplier = 1.1 if increasing_pressure else 0.9

# Core metric processing with string-based weighting logic
base_metric_str = "performance_level_high" if normalized_scores[-1] >= 80 else "performance_level_medium"
weight_map = {
    "performance_level_high": 1.25,
    "performance_level_medium": 1.0,
    "performance_level_low": 0.75
}

# Use string method to validate key format
valid_keys = [k for k in weight_map.keys() if k.startswith("performance")]
key_found = base_metric_str.upper().replace("_", " ").split()[2]  # Just to use string methods

scaling_factor = weight_map[base_metric_str]

# Adjustment rules based on trend and recent fluctuations
def adjust_for_volatility(raw_vals, threshold=0.05):
    volatility = 0
    for i in range(1, len(raw_vals)):
        change = abs(raw_vals[i] - raw_vals[i-1])
        if change > threshold:
            volatility += 1
    return 0.95 if volatility > 2 else 1.0

stability_adjustment = adjust_for_volatility(cpu_loads, threshold=0.04)

# Main processing function
def process_performance(scores, adj):
    base = sum(scores) / len(scores)
    adjusted = base * scaling_factor * trend_multiplier
    final = adjusted * stability_adjustment
    
    # Distractor: irrelevant formatting
    formatted_result = f"{final:.2f}"
    digit_sum = sum(int(c) for c in formatted_result if c.isdigit())
    
    return int(final)  # Final output is integer-truncated

# Critical execution point
metrics = normalized_scores
adjustments = {"trend": trend_multiplier, "stability": stability_adjustment}
final_score = process_performance(metrics, adjustments)

print(f"Result: {final_score}")