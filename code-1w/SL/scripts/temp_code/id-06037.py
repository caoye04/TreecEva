from collections import defaultdict
import math

# Simulate network node performance evaluation
def analyze_node_response(times):
    avg = sum(times) / len(times)
    variance = sum((t - avg) ** 2 for t in times) / len(times)
    return math.sqrt(variance)

# Misleading auxiliary function (not directly used in final result)
def calculate_efficiency_ratio(throughput, latency):
    if latency == 0:
        return 0
    ratio = throughput / latency
    adjustment = 1.5 if ratio > 100 else 0.8
    return ratio * adjustment

# Core metric processor
def process_metrics(raw_data):
    processed = defaultdict(float)
    total_entries = 0

    for key, values in raw_data.items():
        total_entries += len(values)
        if key == 'response_time':
            # Compute harmonic mean for response time
            inv_sum = sum(1 / (v + 1e-9) for v in values)
            processed['rt_hmean'] = len(values) / inv_sum
        elif key == 'bandwidth':
            processed['peak_bw'] = max(values)
            processed['stability'] = len([v for v in values if v > 0.9 * max(values)])
        elif key == 'errors':
            error_rate = sum(values) / sum(raw_data.get('requests', [1]))
            processed['error_freq'] = error_rate

    # Dummy normalization (semi-relevant)
    for k in processed:
        if 'rt_' in k:
            processed[k] = round(processed[k], 3)

    return processed, total_entries

# Main evaluation logic
def evaluate_performance(metrics, weights):
    base_score = 0
    temp_adjustment = 0

    # Key computation branches
    if 'rt_hmean' in metrics:
        base_score += weights['latency'] * (100 / metrics['rt_hmean'])
        temp_adjustment += 5

    if 'peak_bw' in metrics:
        base_score += weights['bandwidth'] * min(metrics['peak_bw'], 100)

    if 'error_freq' in metrics:
        penalty = weights['error'] * metrics['error_freq'] * 100
        base_score -= penalty

    # Irrelevant intermediate calculation (distractor)
    noise_factor = sum([i**2 for i in range(3)]) * 0.1  # Always 1.4
    dummy_tracker = {'noise': noise_factor, 'count': 0}
    for _ in [1, 2]:
        dummy_tracker['count'] += 1

    # Final non-linear adjustment (depends on base score)
    if base_score > 70:
        base_score = base_score * 0.95 + 3
    elif base_score > 50:
        base_score = base_score * 1.05

    return int(round(base_score))

# Input data setup
raw_input = {
    'response_time': [12, 15, 10, 18, 14],
    'bandwidth': [88, 92, 85, 94, 90],
    'errors': [2, 1, 3],
    'requests': [100, 95, 105]
}

weights_config = {
    'latency': 0.4,
    'bandwidth': 0.35,
    'error': 0.25
}

# Preprocessing step with side-variable
interim_results, entry_count = process_metrics(raw_input)

# Secondary irrelevant analysis
response_deviation = analyze_node_response(raw_input['response_time'])
dummy_list = list(map(lambda x: x * 0.9 + 2, raw_input['bandwidth']))
filtered_bandwidth = [b for b in dummy_list if b > 80]

# Critical execution point
final_score = evaluate_performance(interim_results, weights_config)

# Print result
print(f"Result: {final_score}")