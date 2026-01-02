from collections import defaultdict, Counter
import itertools

# Irrelevant utility function (dead code path)
def calculate_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p).log2() if p > 0 else 0
    return entropy

# Misleading data structure with decoy values
decoys = {
    'outliers': [999, -888, 777],
    'noise_floor': 42,
    'phantom_metric': float('inf')
}

# Simulated sensor readings with redundant transformations
raw_readings = [3.1, 2.8, 3.3, 3.0, 3.2, 2.9]
filtered = [x for x in raw_readings if x > 2.7]
scaled = [(x - 2.5) * 10 for x in filtered]
baseline_adjusted = [round(x - 5.0, 1) for x in scaled]

# Unused transformation chain (distractor)
shifted = list(itertools.accumulate(baseline_adjusted))
normalized = [x / max(shifted) for x in shifted if x != 0]

# Core data for evaluation
metric_data = {
    'throughput': [120, 135, 128, 141, 130],
    'latency': [24, 21, 26, 19, 22],
    'jitter': [3.1, 2.9, 3.3, 2.8, 3.0]
}

# Benchmark thresholds (partially relevant)
benchmarks = {
    'throughput_min': 125,
    'latency_max': 25,
    'jitter_max': 3.2
}

# Red herring: complex but unused scoring matrix
weight_matrix = defaultdict(lambda: 1.0)
weight_matrix.update({
    ('throughput', 'high'): 1.2,
    ('latency', 'low'): 0.8
})

# Decoy function that looks important but is never called
def analyze_trend(series):
    diffs = [b - a for a, b in zip(series, series[1:])]
    trend_score = sum(1 for d in diffs if d > 0) - sum(1 for d in diffs if d < 0)
    return trend_score

# Auxiliary computation with misleading intermediate result
aggregate_stats = {}
for key, values in metric_data.items():
    aggregate_stats[key + '_avg'] = sum(values) / len(values)
    aggregate_stats[key + '_peak'] = max(values)

# Fake fusion logic (distractor)
fusion_weights = {'a': 0.3, 'b': 0.5, 'c': 0.2}
fused_score = sum(fusion_weights[k] * len(decoys['outliers']) for k in fusion_weights)

# Real logic begins here — subtle and buried among noise
def assess_dimension(data, threshold, direction='above'):
    average = sum(data) / len(data)
    if direction == 'above':
        return 1 if average >= threshold else -1
    else:
        return 1 if average <= threshold else -1

# Another relevant helper
def count_passing(values, limit, type='lt'):
    return len([v for v in values if (v < limit if type == 'lt' else v > limit)])

# Critical function that computes the actual answer
def evaluate_performance(metrics, criteria):
    score = 0
    
    # Throughput: add 10 per passing measurement above threshold
    tp_pass = count_passing(metrics['throughput'], criteria['throughput_min'], 'gt')
    score += tp_pass * 10
    
    # Latency: subtract 5 for each measurement exceeding max
    lat_fail = count_passing(metrics['latency'], criteria['latency_max'], 'gt')
    score -= lat_fail * 5
    
    # Jitter: add 3 for each within tolerance
    jit_pass = count_passing(metrics['jitter'], criteria['jitter_max'], 'lt')
    score += jit_pass * 3
    
    # Bonus logic: if more than 3 throughput readings are increasing consecutively
    increases = 0
    for i in range(len(metrics['throughput']) - 1):
        if metrics['throughput'][i+1] > metrics['throughput'][i]:
            increases += 1
    if increases > 3:
        score += 7
    
    # Penalty for high jitter variance
    jitter_range = max(metrics['jitter']) - min(metrics['jitter'])
    if jitter_range > 0.4:
        score -= 4
    
    return score

# Execution point of interest
final_score = evaluate_performance(metric_data, benchmarks)

# Print result as required
print(f"Result: {final_score}")