import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x > 0) - len(data)

# Misleading intermediate calculation
temp_offset = 17.3
dummy_cache = [i * 2 + temp_offset for i in range(50)]
rolling_buffer = [0] * 10

# Core data structures with red herrings
metrics = {
    'accuracy': 0.92,
    'latency_ms': 45,
    'throughput': 210,
    'consistency': 0.88,
    'reliability': 0.95
}

weights = {
    'accuracy': 0.3,
    'latency_ms': -0.1,  # negative weight as penalty
    'throughput': 0.2,
    'consistency': 0.15,
    'reliability': 0.25
}

# Distractor: complex but unused transformation
transformed_metrics = {
    k: (v ** 1.1 if isinstance(v, float) else math.log(v))
    for k, v in metrics.items()
}

# Decoy normalization function (never called)
def normalize_scores(scores):
    max_val = max(scores.values())
    return {k: v / max_val for k, v in scores.items()}

# Real logic buried among distractions
baseline_threshold = 0.85
penalty_factor = 0.9
boost_active = any(metrics[k] > baseline_threshold for k in ['accuracy', 'reliability'])

correction_term = 0
if metrics['consistency'] < 0.9:
    correction_term -= 5
    if metrics['latency_ms'] > 40:
        correction_term -= 3
        for i in range(5):
            rolling_buffer[i] = dummy_cache[i]  # Red herring update

# Secondary distraction: fake aggregation
aggregate_metric = sum(
    metrics[k] * abs(weights[k]) 
    for k in weights if k != 'latency_ms'
) / sum(abs(weights[k]) for k in weights if k != 'latency_ms')

# Actual evaluation logic
weighted_sum = sum(metrics[metric] * weight for metric, weight in weights.items())
scale_factor = 100

# Conditional adjustment based on logical expression
adjustment = (20 if all(
    metrics[m] >= 0.9 for m in ['accuracy', 'reliability', 'consistency']
) else -10) if boost_active else 0

# Final computation obscured by context
final_score = (weighted_sum * scale_factor) + adjustment + correction_term

# Output result as required
print(f"Result: {final_score}")