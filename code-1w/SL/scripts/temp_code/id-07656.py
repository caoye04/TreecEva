from collections import defaultdict
import math

# Irrelevant utility function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Decoy function that looks important but isn't called
def compute_rankings(entries):
    rankings = defaultdict(int)
    for e in entries:
        rankings[e] += 1
    return sorted(rankings.values(), reverse=True)

# Misleading intermediate calculation with decoy variables
temp_offset = 42
scaling_factor = 1.618
normalization_constant = math.log(10 + scaling_factor)

# Simulated system metrics with red herring fields
metrics = {
    'latency_ms': [120, 85, 95, 110, 130],
    'throughput_ops': [480, 520, 490, 510, 505],
    'error_rate': [0.01, 0.005, 0.02, 0.003, 0.012],
    'memory_usage_mb': [750, 800, 720, 780, 810],
    'cpu_load': [0.65, 0.72, 0.68, 0.74, 0.70],
    'timestamp': [1712050000, 1712050060, 1712050120, 1712050180, 1712050240]
}

# Benchmark configuration with irrelevant parameters
benchmark = {
    'target_latency': 100,
    'min_throughput': 500,
    'max_error_threshold': 0.015,
    'weighting': {'latency': 0.3, 'throughput': 0.4, 'errors': 0.3},
    'calibration_data': [0.1 * i for i in range(10)],
    'deprecated_mode': True,
    'legacy_flag': 'OFF'
}

# Unused transformation pipeline
preprocessors = [
    lambda x: x + 10 if x < 100 else x - 5,
    lambda x: round(x * 1.05, 2),
    lambda x: max(0, x - temp_offset)
]

# Real logic begins here — hidden among distractions
def analyze_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs) if diffs else 0

# Core evaluation logic buried in abstraction
def evaluate_component(data, target, weight):
    avg = sum(data) / len(data)
    deviation = abs(avg - target) / target
    score = max(0, 1 - deviation)
    return score * weight

# Secondary metric with plausible but unused alternative
def alternative_scorer(vals, func=lambda v: v ** 0.5):
    return sum(func(v) for v in vals) / len(vals)

# Main evaluation function — only one that matters
def evaluate_performance(m, b):
    # Extract relevant series
    latencies = m['latency_ms']
    throughput = m['throughput_ops']
    errors = m['error_rate']

    # Compute individual component scores
    latency_score = evaluate_component(latencies, b['target_latency'], b['weighting']['latency'])
    throughput_score = evaluate_component(throughput, b['min_throughput'], b['weighting']['throughput'])
    
    # Error rate uses inverse logic (lower is better)
    error_avg = sum(errors) / len(errors)
    error_penalty = error_avg / b['max_error_threshold']
    error_score = (1 - min(1, error_penalty)) * b['weighting']['errors']

    # Hidden key computation: stability bonus based on latency consistency
    stability_metric = analyze_stability(latencies)
    stability_bonus = 0.1 * math.exp(-stability_metric / 50)  # Max 0.1 bonus

    # Combine all factors
    base_score = latency_score + throughput_score + error_score
    final_raw = base_score + stability_bonus

    # Scale to 100-point scale
    scaled_result = final_raw * 100

    # Distractor: unused rounding variants
    _ = round(scaled_result, 0)
    _ = int(scaled_result + 0.5)

    # Critical assignment point
    final_score = int(round(scaled_result))

    # More decoys below
    audit_log = defaultdict(list)
    audit_log['components'].append({'raw': base_score, 'bonus': stability_bonus})

    return final_score

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark)

# Print result as required
print(f"Result: {final_score}")