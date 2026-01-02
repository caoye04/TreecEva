from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code)
def analyze_sentiment(text):
    return sum(1 for c in text if c in 'aeiou') % 3

def normalize_vector(vec):
    norm = math.sqrt(sum(x ** 2 for x in vec))
    return [x / norm for x in vec] if norm > 0 else vec

# Distractor data structure
temp_readings = {
    'sensor_a': [23.5, 24.1, 22.9, 25.0],
    'sensor_b': [19.8, 20.2, 19.7, 21.0],
    'sensor_c': [30.1, 29.8, 31.0, 30.5]
}

# Real data used in computation
metrics = defaultdict(float)
metrics['latency'] = 120
metrics['throughput'] = 85
metrics['accuracy'] = 96
metrics['energy_efficiency'] = 78
metrics['scalability'] = 88

# Benchmark weights — only some are used
benchmark_weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'accuracy': 0.35,
    'energy_efficiency': 0.05,
    'reliability': 0.05,  # unused weight (red herring)
    'security': 0.1       # unused weight (red herring)
}

# Decoy list of strings with embedded numbers (distraction)
data_strings = [
    "perf_92_check",
    "metric_45_valid",
    "score_77_fail",
    "result_81_pass"
]

# Extract and count digits from strings — irrelevant operation
digit_counts = Counter()
for s in data_strings:
    digit_counts[s] = len([c for c in s if c.isdigit()])

# Another distraction: string-based threshold map
threshold_map = {
    'critical': 90,
    'high': 80,
    'medium': 60,
    'low': 30
}

# Simulated early exit condition that doesn't trigger
critical_failure = any(v < 10 for v in metrics.values())
if critical_failure:
    final_score = -1
    print("System failure detected")
else:
    # Core logic begins here — real path
    weighted_sum = 0.0
    total_weight = 0.0

    # Only iterate over keys present in both metrics and weights
    for key in metrics:
        if key in benchmark_weights:
            if key == 'latency':
                # Invert latency since lower is better
                normalized = 100 - min(metrics[key], 90)  # cap at 90 for fairness
            else:
                normalized = metrics[key]
            weighted_sum += normalized * benchmark_weights[key]
            total_weight += benchmark_weights[key]
    
    # Normalize by total active weight
    adjusted_score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Apply non-linear boost for high performers
    if adjusted_score >= 85:
        bonus = 5 * math.log(adjusted_score, 10)
    elif adjusted_score >= 70:
        bonus = 2
    else:
        bonus = 0
    
    # Final adjustment using string-derived fake metric (irrelevant)
    fake_factor = sum(ord(w[0]) for w in threshold_map) % 10  # red herring
    
    # But actual final score ignores fake_factor
    final_score = adjusted_score + bonus

# Print result as required
print(f"Target result: {final_score}")