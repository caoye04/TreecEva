def analyze_efficiency(data, threshold=0.75):
    normalized = {k: v / sum(data.values()) for k, v in data.items()}
    filtered = {k: v for k, v in normalized.items() if v > threshold}
    return len(filtered) if filtered else 1

system_load = {'node_a': 24, 'node_b': 18, 'node_c': 32, 'node_d': 11}

# Irrelevant transformation chain
temp_data = [x * 2 for x in system_load.values()]
temp_data = [t - 5 for t in temp_data if t > 30]
adjusted_load = sum(temp_data) // 2 if temp_data else 0

scaling_factor = 1.3
buffer_pool = set()
for val in system_load.values():
    buffer_pool.add(val % 7)

benchmark_refs = set(range(1, 6))
overlap_count = len(buffer_pool & benchmark_refs)

auxiliary_metric = overlap_count * scaling_factor

# Core logic disguised among distractors
metrics = {
    'throughput': 89,
    'latency': 42,
    'jitter': 5,
    'bandwidth': 76
}

baseline_caps = [70, 50, 10, 65]

# Distractor: complex but unused structure
detailed_analysis = {
    name: {
        'raw': val,
        'deviation': abs(val - ref),
        'efficiency': val >= ref * 0.95
    }
    for name, val, ref in zip(metrics.keys(), metrics.values(), baseline_caps)
}

status_flags = [1 if m >= b else 0 for m, b in zip(metrics.values(), baseline_caps)]
activation_level = sum(status_flags)

benchmarks = {
    'critical': 85,
    'high': 70,
    'medium': 50,
    'low': 30
}

# Real computation buried in distractions
def evaluate_performance(perf, tiers):
    score = 0
    tier_vals = sorted(tiers.values(), reverse=True)
    
    # Misleading intermediate calculation
    phantom_score = 0
    for i, (k, v) in enumerate(perf.items()):
        phantom_score += v * (i + 1)  # Not used later
    
    # Actual scoring logic
    for key, value in perf.items():
        if value >= tiers['critical']:
            score += 10
        elif value >= tiers['high']:
            score += 7
        elif value >= tiers['medium']:
            score += 4
        else:
            score += 1
    
    # Secondary adjustment using set operation
    metric_set = set(perf.values())
    threshold_set = set(range(70, 101))
    bonus_multiplier = len(metric_set & threshold_set)  # intersection
    
    if bonus_multiplier > 0:
        score *= (1 + bonus_multiplier * 0.1)
    
    return int(score)

interim_result = analyze_efficiency(system_load)

# Unused but plausible-looking diagnostic block
if adjusted_load > 20:
    diagnostics = "STABLE"
elif adjusted_load > 10:
    diagnostics = "MONITORING"
else:
    diagnostics = "WARNING"

final_score = evaluate_performance(metrics, benchmarks)
Result: final_score