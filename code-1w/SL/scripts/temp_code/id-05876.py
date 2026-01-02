import math

# Simulated system performance metrics (real data)
metrics = {
    'latency': 42.5,
    'throughput': 870,
    'error_rate': 0.034,
    'cpu_util': 78.2,
    'memory_efficiency': 65.4,
    'concurrency': 120
}

# Weight configuration for evaluation (domain-specific tuning)
weights = {
    'latency': 0.15,
    'throughput': 0.20,
    'error_rate': -0.25,  # Negative weight: lower is better
    'cpu_util': 0.10,
    'memory_efficiency': 0.18,
    'concurrency': 0.12
}

# Irrelevant auxiliary data (distraction)
benchmark_history = [
    {'version': '1.0', 'score': 76.2, 'outliers': [1.2, 0.9]},
    {'version': '1.1', 'score': 78.5, 'outliers': []},
    {'version': '1.2', 'score': 81.0, 'outliers': [2.1]}
]

# Decoy function – looks important but unused in final calculation
def calculate_legacy_score(data):
    base = data.get('latency', 0) * 0.3
    bonus = data.get('throughput', 0) * 0.001
    penalty = data.get('error_rate', 0) * 50
    return base + bonus - penalty

# Auxiliary transformation (misleading intermediate step)
def normalize(value, min_val=0, max_val=100):
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))

# Complex helper that appears useful but is only partially used
noise_floor = 0.005
def apply_nonlinear_adjustment(x, method='sigmoid'):
    if method == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif method == 'tanh':
        return math.tanh(x)
    else:
        return x + noise_floor

# Red herring: elaborate preprocessing with no impact
preprocessed_metrics = {}
for k, v in metrics.items():
    if k == 'error_rate':
        preprocessed_metrics[k] = round(100 * (1 - v), 3)
    elif k in ['latency', 'cpu_util']:
        preprocessed_metrics[k] = round(v * 1.05, 3)  # Artificial inflation
    else:
        preprocessed_metrics[k] = round(v * 0.95, 3)

# Dead code path (never executed)
def deprecated_evaluation(m):
    total = 0
    for key in m:
        total += hash(key) % 10
    return total % 100

# Unused normalization map (distractor)
normalization_map = {key: (10 if 'rate' in key else 100) for key in metrics}

# Core evaluation logic buried among distractions
def evaluate_performance(met, wts):
    raw_contributions = {}
    adjusted_total = 0.0
    weight_sum = 0.0

    for metric_name, value in met.items():
        weight = wts[metric_name]

        # Real transformation used in calculation
        if metric_name == 'latency':
            # Invert and scale latency: lower latency → higher score
            transformed = 100 * (1 - min(value / 100.0, 1))
        elif metric_name == 'error_rate':
            transformed = 100 * (1 - min(value * 10, 1))
        elif metric_name == 'throughput':
            transformed = min(value / 1000.0 * 100, 100)
        else:
            # Linear scaling for other metrics
            transformed = min(value, 100)

        # Apply weight
        contribution = transformed * abs(weight)
        raw_contributions[metric_name] = contribution
        adjusted_total += contribution
        weight_sum += abs(weight)

    # Final aggregation
    base_score = adjusted_total / weight_sum if weight_sum > 0 else 0

    # Secondary adjustment based on concurrency threshold (actual conditional use)
    concurrency = met['concurrency']
    if concurrency > 100:
        base_score *= 1.05  # 5% bonus for high concurrency
    elif concurrency < 50:
        base_score *= 0.95

    # Minor bit manipulation check (actual usage)
    int_part = int(base_score)
    if int_part & 1:  # If integer part is odd
        base_score += 1.5

    return round(base_score, 6)

# Spurious analysis function that does nothing
def generate_diagnostic_report():
    return {"status": "nominal", "flags": [], "checksum": 0}

generate_diagnostic_report()  # Call with no side effects

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Output required result
print(f"Result: {final_score}")