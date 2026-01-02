import math

# Simulated system health monitoring and performance scoring engine
def monitor_system_health(sensor_data, thresholds):
    # Irrelevant helper function (dead code path)
    return sum(1 for val in sensor_data if val > thresholds.get('critical', 100))

# Legacy diagnostic routine (unused)
def legacy_diagnostics(payload):
    return [x ^ 255 for x in payload if x % 2 == 0]

# Core metric transformation pipeline
def transform_metrics(raw_entries):
    transformed = []
    for idx, entry in enumerate(raw_entries):
        if idx % 3 == 0:
            # Apply logarithmic scaling on every 3rd record
            transformed.append(math.log(entry + 1) * 1.5)
        elif idx % 5 == 0:
            # Apply square root with offset
            transformed.append(math.sqrt(entry + 10))
        else:
            # Linear scaling
            transformed.append(entry * 0.75)
    return transformed

# Auxiliary checksum calculator (distractor)
def compute_checksum(data_stream):
    chk = 0
    for val in data_stream:
        chk = (chk << 1) ^ int(val) & 0xFF
    return chk % 97

# Recursive feature normalizer (partially relevant)
def normalize_features(values, depth=0):
    if depth >= 3 or len(values) <= 1:
        return [round(v / max(values), 4) if max(values) != 0 else 0 for v in values]
    even_idx = [v for i, v in enumerate(values) if i % 2 == 0]
    odd_idx = [v for i, v in enumerate(values) if i % 2 == 1]
    norm_even = normalize_features(even_idx, depth + 1)
    norm_odd = normalize_features(odd_idx, depth + 1)
    result = []
    e_iter, o_iter = iter(norm_even), iter(norm_odd)
    for i in range(len(values)):
        result.append(next(e_iter) if i % 2 == 0 else next(o_iter))
    return result

# Bitmask-based anomaly filter (red herring)
def detect_anomalies(bit_series):
    mask = 0b10101010
    anomalies = []
    for b in bit_series:
        if (b & mask) == mask:
            anomalies.append(b)
    return anomalies

# Main evaluation engine
def evaluate_performance(log, config):
    # Step 1: Extract baseline metrics
    base_metrics = [log['cpu'], log['memory'], log['disk_io']]
    
    # Step 2: Transform using non-linear functions
    processed = transform_metrics(base_metrics)
    
    # Step 3: Inject synthetic timestamp features (irrelevant)
    ts_features = [hash(str(t)) % 100 for t in [123456, 123457, 123458]]
    ts_weighted = sum(ts * 0.01 for ts in ts_features)  # Distractor contribution
    
    # Step 4: Normalize critical dimensions
    critical_subset = [processed[0], processed[1]]  # CPU and memory only
    normalized = normalize_features(critical_subset)
    
    # Step 5: Apply configuration weights
    weights = config['weights']
    weighted_sum = sum(normalized[i] * weights[i] for i in range(len(normalized)))
    
    # Step 6: Add environmental adjustment factor (misleading intermediate)
    env_factor = math.sin(config['temp']) + math.cos(config['humidity'])
    adjusted = weighted_sum + env_factor  # Looks important but minor impact
    
    # Step 7: Apply final activation threshold
    if adjusted < config['threshold']:
        score = adjusted * 100
    else:
        score = adjusted * 85
    
    # Step 8: Correct rounding to match expected precision
    return round(score, 4)

# Additional decoy structure (never used)
decoys = {
    'placeholder_1': lambda x: x ** 2,
    'placeholder_2': lambda x: math.exp(-x),
    'debug_flag': False,
    'version': 'legacy_v2'
}

# Real input data
metrics_log = {
    'cpu': 89,
    'memory': 144,
    'disk_io': 21,
    'network_kbps': 987,
    'context_switches': 456
}

benchmark_config = {
    'weights': [0.6, 0.4],  # Only first two are used
    'threshold': 0.75,
    'temp': 23.5,
    'humidity': 68.2,
    'mode': 'aggressive'
}

# Simulated sensor readings (unused but plausible)
sensor_readings = [95, 102, 88, 110, 97, 130, 77]
threshold_map = {'warning': 90, 'critical': 120}

# Unused zip and enumerate example (plausible distractor)
labels = ['A', 'B', 'C', 'D']
for i, (lbl, val) in enumerate(zip(labels, sensor_readings)):
    pass  # No effect

# Key execution point
final_score = evaluate_performance(metrics_log, benchmark_config)
print(f"Target result: {final_score}")