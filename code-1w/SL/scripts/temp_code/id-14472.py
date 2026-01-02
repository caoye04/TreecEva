import math

# Simulated sensor array data from a distributed environmental monitoring system
def generate_sensor_readings():
    base_values = [12.5, 18.3, 9.7, 22.1, 15.6]
    noise_offsets = [0.1 * math.sin(i) for i in range(5)]
    return [base_values[i] + noise_offsets[i] for i in range(5)]

# Irrelevant transformation: frequency analysis of arbitrary signal (red herring)
def compute_harmonic_profile(signal):
    if len(signal) == 0:
        return [0]
    return [math.cos(x * math.pi / 4) for x in signal]

# Misleading diagnostic that appears important but is unused
unused_diagnostics = {
    'anomaly_score': 0.87,
    'spectral_entropy': 2.31,
    'peak_variance_ratio': 1.44
}

# Auxiliary function to normalize readings (used)
def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    if max_val == min_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]

# Another decoy function: processes unrelated temporal coherence (dead code path)
def calculate_temporal_coherence(timeseries):
    coherence_sum = 0
    for i in range(1, len(timeseries)):
        coherence_sum += abs(timeseries[i] - timeseries[i-1])
    return coherence_sum / len(timeseries) if timeseries else 0

# Core logic: mapping normalized health metrics to binary status via thresholds (critical)
def map_to_status(metrics, thresholds):
    return [1 if metrics[i] >= thresholds[i % len(thresholds)] else 0 for i in range(len(metrics))]

# Bit manipulation layer: encode status vector as bitmask (used in final step)
def pack_bits(status_vector):
    packed = 0
    for bit in status_vector:
        packed = (packed << 1) | bit
    return packed

# Higher-order function filter (distractor - not actually applied)
temporal_filter = lambda window: [x for x in window if x > 0.3]

# Main analysis pipeline (only some components are relevant)
def analyze_metrics(metrics, config_map):
    # Step 1: Normalize input metrics
    normalized = normalize_readings(metrics)
    
    # Step 2: Apply threshold-based classification
    active_thresholds = [config_map['t_critical'], config_map['t_warning']]
    classification = map_to_status(normalized, active_thresholds)
    
    # Step 3: Compute checksum (irrelevant)
    checksum = sum([i * v for i, v in enumerate(classification)])
    
    # Step 4: Pack into bit representation (key transformation)
    signature = pack_bits(classification)
    
    # Step 5: Spurious entropy calculation (distractor)
    entropy_proxy = -sum([p * math.log(p + 1e-9) for p in normalized[:3]])
    
    # Step 6: Conditional override logic (never triggers - misleading)
    override_flag = False
    if sum(classification) > 10 and entropy_proxy < 0:
        override_flag = True
        signature = 99999
    
    # Step 7: Final diagnostic derived from signature
    final_diagnostic = (signature * 17) ^ 0xAAAA
    
    # Dead code: unused aggregation mode
    aggregation_mode = 'rms' if len(metrics) > 3 else 'mean'
    
    return final_diagnostic

# Irrelevant preprocessing block (misleads with complex-looking transforms)
signal_buffer = [math.tanh(x) for x in generate_sensor_readings()]
harmonics = compute_harmonic_profile(signal_buffer)
smoothed = [x * 0.9 for x in harmonics]

# Actual entry point data
raw_health_data = [45, 12, 67, 23, 55, 18]
threshold_config = {
    't_critical': 0.4,
    't_warning': 0.25,
    't_ignore': 0.05  # unused threshold (decoy)
}

# Unused backup strategy map (distractor dictionary)
strategy_catalog = {
    'low_risk': {'action': 'monitor', 'delay': 30},
    'high_risk': {'action': 'alert', 'delay': 5}
}

# Key execution point
final_diagnostic = analyze_metrics(raw_health_data, threshold_config)
print(f"Target result: {final_diagnostic}")