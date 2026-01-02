def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if x > threshold]
    return len(filtered) > 0 and sum(filtered) / len(filtered) > threshold * 1.5

# Irrelevant helper function (decoy)
def deprecated_util(val):
    return (val ** 2 + 3) % 7

# Unused transformation chain
def transform_sequence(seq):
    return [((x << 2) ^ 5) & 15 for x in seq if x % 3 != 0]

# Simulated sensor readings (distraction data)
sensor_log = [0.1, 0.4, 0.8, 0.6, 0.3]
depth_map = [2, 4, 1, 8, 5]

# Red herring: complex but unused bitwise analysis
bit_analysis = 0
for d in depth_map:
    bit_analysis ^= (d << 3) | (d >> 1)
bit_analysis = (bit_analysis + 97) % 1000

# Real metric computation begins here
def compute_stability_index(timestamps):
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_diff = sum(diffs) / len(diffs)
    variance = sum((d - avg_diff) ** 2 for d in diffs) / len(diffs)
    return 1 / (1 + variance) if variance > 0 else 1.0

# Timestamps from system events (used later)
event_timestamps = [10, 12, 15, 19, 24]  # Differences: 2,3,4,5 → avg=3.5, var=1.25

# Health indicators with misleading naming
system_health_flags = {
    'overheat': False,
    'pressure_ok': True,
    'flow_rate': 0.77,
    'vibration': 0.3
}

# Distractor dictionary with plausible but unused entries
config_params = {
    'gain': 2.3,
    'offset': -0.15,
    'thresholds': [0.1, 0.4, 0.8],
    'mode': 'turbo'
}

# Core evaluation logic
metrics = {
    'latency': 0.45,
    'jitter': 0.12,
    'throughput': 850,
    'consistency': compute_stability_index(event_timestamps),
    'signal_quality': float(analyze_signal(sensor_log))
}

# Weighting scheme – some weights are decoys
weights = {
    'latency': 0.3,
    'jitter': 0.2,
    'throughput': 0.25,
    'consistency': 0.15,
    'power_draw': 0.1,  # Unused weight (red herring)
    'legacy_mode': 0.0   # Explicitly zero-weighted
}

# Evaluate performance using only matching keys
valid_keys = set(metrics.keys()) & set(weights.keys())
weighted_sum = sum(metrics[k] * weights[k] for k in valid_keys if weights[k] > 0)

total_effective_weight = sum(weights[k] for k in valid_keys if weights[k] > 0)

# Normalize score
normalized_throughput = min(metrics['throughput'] / 1000, 1.0)

# Final computation
final_score = weighted_sum / total_effective_weight if total_effective_weight > 0 else 0

# Introduce irrelevant floating-point artifact
temp_cache = {i: (i * 1.618) % 1 for i in range(1, 6)}
checksum = int(sum(temp_cache.values()) * 100)

# Spurious conditional that doesn't affect result
if checksum > 200:
    final_score *= 0.9

# Print result as required
print(f"Result: {final_score}")