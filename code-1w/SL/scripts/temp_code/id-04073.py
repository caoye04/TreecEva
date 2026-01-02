import itertools

# Simulated system health monitoring with performance metrics
# Note: Some variables are decoys for distraction (e.g., temp_log, checksum)

def analyze_stability(readings):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return mean if variance < 50 else mean * 0.9

def evaluate_latency(sequence):
    if not sequence:
        return 0
    sorted_seq = sorted(sequence)
    median = sorted_seq[len(sorted_seq) // 2]
    return median * 0.85

# Irrelevant helper - dead code path (never called in execution)
def compute_checksum(data):
    return sum(data) % 256

def process_metrics(raw_data):
    # Multiple data transformations with red herrings
    base_metrics = {}
    temp_log = []

    for key, values in raw_data.items():
        if key == 'response_time':
            base_metrics['latency'] = evaluate_latency(values)
        elif key == 'throughput':
            base_metrics['throughput'] = sum(values) / len(values)
        elif key == 'error_rate':
            filtered = [x for x in values if x < 10]
            base_metrics['reliability'] = 100 - (sum(filtered) / len(filtered))

    # Distractor computation - looks important but unused later
    outlier_count = 0
    for v in itertools.chain(raw_data['response_time'], raw_data['throughput']):
        if v > 100:
            outlier_count += 1

    adjustment_factor = 1.0
    if outlier_count > 5:
        adjustment_factor = 0.95

    # Decoy variable - appears to be used but isn't
    temp_log.append(adjustment_factor)

    return base_metrics

# Core aggregation logic
weights = {
    'latency': 0.4,
    'throughput': 0.3,
    'reliability': 0.3
}

# Simulated input data
raw_system_data = {
    'response_time': [120, 85, 90, 110, 95, 130, 80],
    'throughput': [70, 75, 80, 65, 85, 70, 78],
    'error_rate': [2.1, 3.0, 1.8, 4.2, 2.5, 3.3, 1.9]
}

# Processed metrics
metrics = process_metrics(raw_system_data)

# Additional distraction: unused conditional expression
system_status = 'stable' if metrics['latency'] < 100 else 'degraded'
health_flag = 'OK' if system_status == 'stable' else 'ALERT'

# Critical distractor block - computes something that seems relevant
baseline = [metrics['latency'], metrics['throughput'], metrics['reliability']]
corrected_baseline = [x * 1.05 for x in baseline if x > 50]  # Partial application?

# More decoy logic - creates illusion of complexity
snapshot = {k: v for k, v in zip(['A','B','C'], corrected_baseline)}
checksum_values = [len(baseline), len(corrected_baseline), 0 if health_flag=='OK' else 1]

# Actual key computation hidden among distractions
weighted_sum = 0
for name, metric_val in metrics.items():
    weighted_sum += metric_val * weights[name]

# Final score calculation - this is the real answer path
normalization_factor = analyze_stability(raw_system_data['throughput']) / 75

# Introduce conditional expression (Python idiom)
scaling_factor = 1.1 if normalization_factor > 1 else 0.95

# The actual target variable
final_score = weighted_sum * scaling_factor

# Print result for verification
print(f"Result: {final_score}")