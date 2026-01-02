import math

# Irrelevant utility function (dead code path)
def normalize_data(data):
    return [x / sum(data) for x in data]

# Distractor variables
temp_buffer = [0] * 100
redundant_flag = True
junk_sum = 0
for i in range(50):
    junk_sum += (i ** 2) % 7

# Core data structures
metrics = {
    'latency': [120, 85, 95, 110, 130],
    'throughput': [420, 460, 430, 475, 440],
    'error_rate': [0.01, 0.005, 0.02, 0.003, 0.015]
}

benchmark = {
    'latency_baseline': 100,
    'throughput_baseline': 450,
    'tolerance': 0.05
}

# Decoy transformation (not used in final calculation)
transformed_metrics = {}
if 'latency' in metrics:
    transformed_metrics['latency_z'] = [
        (x - 100) / 15 for x in metrics['latency']
    ]

# Unused intermediate result
correlation_proxy = 0
for x, y in zip(metrics['latency'], metrics['throughput']):
    correlation_proxy += (x - 100) * (y - 450)

# Real processing begins here
latency_deviation = sum(
    abs(x - benchmark['latency_baseline']) for x in metrics['latency']
) / len(metrics['latency'])

throughput_ratio = sum(
    x / benchmark['throughput_baseline'] for x in metrics['throughput']
) / len(metrics['throughput'])

# Bit manipulation red herring
bitmask = 0b110101
shifted_mask = (bitmask << 3) & 0b111111
obscure_value = (bitmask ^ shifted_mask) | 0b001000

# Logical trap with short-circuit evaluation
effective_multiplier = 1.0
if latency_deviation < 20 and (lambda x: x > 0.9)(throughput_ratio) or False:
    effective_multiplier = 1.2
elif len(metrics['error_rate']) > 0:
    avg_error = sum(metrics['error_rate']) / len(metrics['error_rate'])
    if avg_error < 0.01:
        effective_multiplier = 1.1
    else:
        effective_multiplier = 0.9
else:
    effective_multiplier = 0.8

# Set of irrelevant keys (distractor)
unused_keys = set(benchmark.keys()) - {'tolerance'}

# Main scoring logic hidden among noise
def evaluate_performance(data, config):
    base_score = 100.0

    # Latency penalty
    latencies = data['latency']
    base_score -= sum(max(0, x - config['latency_baseline']) for x in latencies) * 0.2

    # Throughput bonus
    base_score += (sum(data['throughput']) / 1000) * 0.5

    # Error rate scaling
    error_factor = 1 - min(0.5, sum(data['error_rate']) / 0.1)
    base_score *= error_factor

    # Apply multiplier from earlier logic
    nonlocal effective_multiplier
    base_score *= effective_multiplier

    # Final adjustment using modular arithmetic red herring
    mod_key = (len(latencies) * 7) % 6
    adjustment_table = {0: 0, 1: -5, 2: 3, 3: -2, 4: 4, 5: 0}
    base_score += adjustment_table[mod_key]

    return round(base_score, 4)

# Critical execution point
final_score = evaluate_performance(metrics, benchmark)

# Additional distractor computation (never used)
aggregated = []
for k in metrics:
    aggregated.append(sum(metrics[k]) // len(metrics[k]))
synthetic_index = math.floor(aggregated[0] * 0.1 + aggregated[1] * 0.01)

# Print target result
Target result: {final_score}