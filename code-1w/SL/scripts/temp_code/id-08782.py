import itertools

# Simulated user preference weights (some are red herrings)
user_weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'memory_usage': 0.2,
    'cache_hit': 0.1,
    'disk_io': 0.0,  # Irrelevant - not used in final calculation
    'network_latency': 0.0  # Irrelevant
}

# Raw performance metrics from system monitoring
metric_data = {
    'accuracy': [0.92, 0.94, 0.91, 0.95],
    'latency': [120, 110, 130, 105],
    'memory_usage': [450, 470, 430, 460],
    'cache_hit': [0.88, 0.91, 0.85, 0.93]
}

# Distractor: unused function that looks important
def calculate_disk_pressure(io_reads, io_writes):
    return sum(io_reads) * 0.7 + sum(io_writes) * 0.3

# Distractor: fake normalization that isn't used
def legacy_normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

# Real processing begins here
baseline_thresholds = {
    'accuracy': 0.90,
    'latency': 150,
    'memory_usage': 500,
    'cache_hit': 0.85
}

# Compute average of each metric
averages = {key: sum(vals) / len(vals) for key, vals in metric_data.items()}

# Transform latency into a score (lower is better → invert)
latency_score = 1 - (averages['latency'] / 200)

# Accuracy score (higher is better)
accuracy_score = averages['accuracy']

# Memory usage score (normalize relative to threshold)
memory_score = 1 - (averages['memory_usage'] / baseline_thresholds['memory_usage'])

# Cache hit rate score
cache_score = averages['cache_hit']

# Composite normalized scores (only some weights matter)
score_components = {
    'accuracy': accuracy_score,
    'latency': latency_score,
    'memory_usage': memory_score,
    'cache_hit': cache_score
}

# Weighted scoring (ignores disk_io and network_latency)
weighted_sum = 0
weight_sum = 0
for metric, weight in user_weights.items():
    if metric in score_components:  # Skip irrelevant weights
        weighted_sum += score_components[metric] * weight
        weight_sum += weight

# Final normalized score
normalized_composite = weighted_sum / weight_sum

# Secondary adjustment based on trend analysis (unused distractor)
def analyze_trend(data):
    diffs = [b - a for a, b in itertools.pairwise(data)]
    return 'improving' if sum(diffs) > 0 else 'declining'

# Bit manipulation decoy: looks complex but unused
trend_flag = 0
for val in metric_data['accuracy']:
    trend_flag ^= int(val * 100)
trend_flag &= 0xFF  # Mask to 8 bits

# Another dead path: conditional that never triggers
if len(metric_data['accuracy']) > 10:
    final_score = -999
else:
    # This is the real computation path
    base_final = normalized_composite * 1000  # Scale up
    
    # Additional correction: if all metrics meet baseline
    all_met = all(
        averages[m] >= baseline_thresholds[m] or m == 'latency' 
        for m in averages.keys()
    )
    # But latency is inverted: lower is better
    latency_ok = averages['latency'] <= baseline_thresholds['latency']
    others_ok = all(
        averages[m] >= baseline_thresholds[m] 
        for m in ['accuracy', 'memory_usage', 'cache_hit']
    )
    if latency_ok and others_ok:
        base_final *= 1.1  # Bonus
    
    final_score = int(base_final)

# Print result as required
print(f"Result: {final_score}")