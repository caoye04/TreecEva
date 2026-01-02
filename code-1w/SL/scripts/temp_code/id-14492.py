from collections import defaultdict

# Simulate system performance metrics from distributed components
data = [
    {'node': 'A', 'latency': 120, 'errors': 3, 'throughput': 850},
    {'node': 'B', 'latency': 95,  'errors': 1, 'throughput': 920},
    {'node': 'C', 'latency': 140, 'errors': 6, 'throughput': 740},
    {'node': 'D', 'latency': 110, 'errors': 2, 'throughput': 880},
    {'node': 'E', 'latency': 105, 'errors': 0, 'throughput': 905}
]

# Weight configuration for scoring (higher weight = more impact)
weights = defaultdict(float, {
    'latency': -0.3,
    'errors': -0.5,
    'throughput': 0.2
})

# Irrelevant baseline thresholds
thresholds = {
    'high_latency': 130,
    'critical_errors': 5,
    'min_throughput': 800
}

# Auxiliary function to compute node health (not directly used in final score)
def calculate_health(record):
    score = 100
    if record['latency'] > thresholds['high_latency']:
        score -= 15
    if record['errors'] >= thresholds['critical_errors']:
        score -= 25
    if record['throughput'] < thresholds['min_throughput']:
        score -= 20
    return max(score, 0)

# Distractor: unused helper that computes normalized latency
normalize_latency = lambda x: round((x - 80) / 150, 3)

# Track cumulative stats for debugging (semi-relevant)
cumulative = defaultdict(int)
for entry in data:
    cumulative['total_latency'] += entry['latency']
    cumulative['total_errors'] += entry['errors']
    cumulative['total_throughput'] += entry['throughput']

cumulative['avg_latency'] = cumulative['total_latency'] / len(data)
cumulative['avg_throughput'] = cumulative['total_throughput'] / len(data)

# Compute individual scores with weighted sum
weighted_scores = []
for record in data:
    raw_score = 0
    for key in weights:
        raw_score += record[key] * weights[key]
    # Base adjustment
    raw_score += 100
    weighted_scores.append(raw_score)

# Misleading transformation: sort in reverse but don't use
sorted_scores = sorted(weighted_scores, reverse=True)
decoy_result = [round(s * 0.95, 2) for s in sorted_scores]  # Unused path

# Actual processing logic
def process_metrics(metrics, w):
    base = 0
    for m in metrics:
        # Apply weights and aggregate
        contribution = 0
        for k in w:
            contribution += m[k] * w[k]
        base += contribution
    # Final adjustment based on average error rate
    avg_err = cumulative['total_errors'] / len(metrics)
    penalty = 10 if avg_err >= 2.5 else 5
    result = abs(round(base + 100 - penalty))  # deterministic scalar
    return result

# Execute main computation
final_score = process_metrics(data, weights)

# Print result as required
print(f"Target result: {final_score}")