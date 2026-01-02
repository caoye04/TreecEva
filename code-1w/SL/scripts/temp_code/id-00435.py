def analyze_data(records):
    totals = {}
    counts = {}
    for r in records:
        key = r['category']
        value = r['value']
        if key not in totals:
            totals[key] = 0
            counts[key] = 0
        totals[key] += value
        counts[key] += 1

    averages = {k: totals[k] / counts[k] for k in totals}
    return averages

# Irrelevant helper function (dead code path)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Another decoy function with misleading intermediate results
def transform_values(arr):
    result = []
    for i, val in enumerate(arr):
        if i % 2 == 0:
            result.append(val * 2 + 1)
        else:
            result.append(val * 3 - 1)
    return result

# Simulated system metrics with noise
def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    return [x for x in data if abs(x - median_val) < threshold]

# Core logic buried among distractions
config_flags = {
    'enable_optimization': True,
    'use_legacy_mode': False,
    'debug_trace': True  # unused
}

raw_metrics = [
    {'category': 'latency', 'value': 120},
    {'category': 'latency', 'value': 140},
    {'category': 'throughput', 'value': 85},
    {'category': 'throughput', 'value': 95},
    {'category': 'errors', 'value': 2},
    {'category': 'errors', 'value': 1}
]

processed_averages = analyze_data(raw_metrics)

# Distractor: complex bit manipulation with no real impact
bit_flag = 0b101010
shifted_flag = (bit_flag << 3) & 0b11111111
masked_result = shifted_flag ^ 0b11001100  # red herring

# Weight configuration (some weights are decoys)
all_weights = {
    'latency': 0.4,
    'throughput': 0.5,
    'errors': 0.3,  # relevant
    'retries': 0.1,  # irrelevant — no such metric
    'timeout_count': 0.05  # irrelevant
}

# Normalize only the used weights
used_keys = ['latency', 'throughput', 'errors']
weight_sum = sum(all_weights[k] for k in used_keys)
normalized_weights = {k: all_weights[k] / weight_sum for k in used_keys}

# Simulate additional noise
noisy_buffer = [0] * 5
for idx, val in enumerate([3, 1, 4, 1, 5]):
    noisy_buffer[idx] = val << 1

# Actual performance evaluation
def evaluate_performance(metrics_map, weight_map):
    score = 0.0
    latency_val = metrics_map.get('latency', 0)
    throughput_val = metrics_map.get('throughput', 0)
    error_val = metrics_map.get('errors', 0)

    # Inverse scoring for latency and errors (lower is better)
    normalized_latency = (100 - min(latency_val, 100)) * 0.01
    normalized_throughput = min(throughput_val, 100) / 100
    normalized_errors = (2 - min(error_val, 2)) * 0.5

    # Apply normalized weights
    w_lat = weight_map['latency']
    w_tp = weight_map['throughput']
    w_er = weight_map['errors']

    score += normalized_latency * w_lat
    score += normalized_throughput * w_tp
    score += normalized_errors * w_er

    # Additional distraction: zip and enumerate used meaningfully but partially irrelevant
    aux_data = [normalized_latency, normalized_throughput, normalized_errors]
    weights_list = [w_lat, w_tp, w_er]
    for i, (val, wgt) in enumerate(zip(aux_data, weights_list)):
        if i % 2 == 0:
            score += val * wgt * 0.05  # minor perturbation, still contributes

    return int(score * 1000)  # scale to integer

# Final computation
final_score = evaluate_performance(processed_averages, normalized_weights)

# Dead code branch (never executed)
if config_flags['use_legacy_mode']:
    final_score *= 0.9

# Print result as required
Result: {final_score}