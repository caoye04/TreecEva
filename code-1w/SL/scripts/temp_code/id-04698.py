import itertools

def analyze_throughput(data, window_size):
    """Irrelevant function: analyzes network throughput with sliding window."""
    if len(data) < window_size:
        return [0]
    return [sum(data[i:i+window_size]) for i in range(len(data) - window_size + 1)]

def generate_checksum(sequence):
    """Decoy function: computes XOR checksum (not used in main logic)."""
    checksum = 0
    for val in sequence:
        checksum ^= (val % 256)
    return checksum

def validate_integrity(record):
    """Misleading function that appears important but is never called."""
    return sum(v ** 2 for v in record.values()) < 10000

# Simulated sensor data (distraction)
sensor_readings = [117, 234, 89, 156, 201, 73, 134]
throughput_trend = analyze_throughput(sensor_readings, 3)

# Baseline configuration with red herring parameters
baseline_config = {
    'threshold': 85,
    'weight_a': 0.6,
    'weight_b': 0.4,
    'offset': -10,
    'decay_factor': 0.95,  # unused but looks relevant
    'max_limit': 200       # misleading bound
}

# Performance metrics log - core data
metrics_log = [
    {'latency': 45, 'success': 1, 'load': 70},
    {'latency': 92, 'success': 0, 'load': 88},
    {'latency': 61, 'success': 1, 'load': 75},
    {'latency': 105, 'success': 0, 'load': 95},
    {'latency': 54, 'success': 1, 'load': 68}
]

# Auxiliary transformation map (partially used)
latency_band_map = {range(0, 50): 'A', range(50, 80): 'B', range(80, 100): 'C', range(100, 200): 'D'}

def map_latency_band(value):
    for band, label in latency_band_map.items():
        if value in band:
            return label
    return 'X'

# Decoy list comprehension with zip and enumerate (no effect)
decoys = [i * x for i, x in enumerate(zip(
    [x['load'] for x in metrics_log],
    [x['success'] for x in metrics_log[::-1]]
))]

# Complex preprocessing using itertools (some parts irrelevant)
expanded_metrics = []
for idx, entry in enumerate(metrics_log):
    expanded = {
        'idx': idx,
        'raw_latency': entry['latency'],
        'normalized_latency': max(0, entry['latency'] - baseline_config['offset']),
        'success_flag': bool(entry['success']),
        'load_level': entry['load'],
        'band': map_latency_band(entry['latency'])
    }
    expanded_metrics.append(expanded)

# Secondary derived structure (distractor)
summary_stats = {
    'total_entries': len(expanded_metrics),
    'avg_load': sum(e['load_level'] for e in expanded_metrics) / len(expanded_metrics),
    'failure_count': len([e for e in expanded_metrics if not e['success_flag']]),
    'high_latency_count': len([e for e in expanded_metrics if e['band'] == 'D'])
}

# Critical function with early returns and modular arithmetic
def evaluate_performance(log, config):
    score = 0
    threshold = config['threshold']
    weight_a = config['weight_a']
    weight_b = config['weight_b']

    for item in log:
        latency = item['latency']
        success = item['success']
        load = item['load']

        # Base penalty for high latency
        if latency > threshold:
            penalty = (latency - threshold) * weight_b
            score -= int(penalty)

        # Reward for success under load
        if success:
            bonus = (load * weight_a) if load > threshold else (load * weight_a * 0.5)
            score += int(bonus)

        # Modular adjustment based on index pattern (hidden rule)
        entry_index = log.index(item)
        if (entry_index + 1) % 3 == 0:  # every third entry gets extra adjustment
            score = (score * 2) % 1000  # modular wrap to prevent explosion

        # Early exit condition (never triggered due to data, but looks plausible)
        if score < -200:
            return -100  # dead code path

    # Final non-linear transformation
    final_adjustment = abs(score) ** 0.5 if score < 0 else score ** 0.5
    return int(final_adjustment)

# Key execution point
final_score = evaluate_performance(metrics_log, baseline_config)

# Irrelevant dictionary operations
diagnostics = {}
for k, v in baseline_config.items():
    diagnostics[k + '_flag'] = v > 50

# Unused Cartesian product via itertools
combinations = list(itertools.product([1, 2], ['low', 'high']))

# Output result as required
print(f"Result: {final_score}")