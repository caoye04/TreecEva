import math

# Simulated system telemetry data with mixed relevance
def collect_telemetry():
    raw_signals = [0.88, 0.72, 0.91, 0.65, 0.83]
    noise_floor = 0.1
    filtered = [x - noise_floor for x in raw_signals if x > 0.5]
    baseline = sum(filtered) / len(filtered)
    return {'baseline': baseline, 'readings': filtered, 'timestamp': 1294875}

# Irrelevant audio processing stub (dead path)
def analyze_audio(signal):
    fft_size = 1024
    window_gain = 1.2
    # This function is never called
    return [math.sin(i * window_gain) for i in range(fft_size)]

# Auxiliary checksum (distractor)
def compute_checksum(data_list):
    chk = 0
    for val in data_list:
        chk = (chk + int(val * 100)) % 257
    return chk

# Core diagnostic engine with conditional logic and distractors
def evaluate_health(metrics, flags):
    risk_score = 0.0
    anomaly_count = 0
    
    # Distractor variables
    temp_threshold = 85.0
    voltage_stability = True
    latency_spike = False
    
    for metric in metrics:
        if metric > 0.85:
            risk_score += 1.5
        elif metric > 0.75:
            risk_score += 0.8
        else:
            anomaly_count += 1
    
    # Misleading intermediate computation (not used in final result)
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    adjusted_risk = risk_score * (1 + 0.1 * anomaly_count)
    
    # Conditional expression (required Python feature)
    health_status = 'CRITICAL' if risk_score >= 3.0 else 'STABLE'
    
    # Embedded bit manipulation red herring
    flag_state = flags.get('debug_mode', False)
    debug_key = 0
    if flag_state:
        debug_key = (17 ^ 255) >> 2  # Never activates due to flag

    # Key logic: apply exponential decay on risk score
    decayed_risk = risk_score * math.exp(-0.3 * anomaly_count)
    
    # Dead code block (unused branch)
    if voltage_stability and latency_spike:
        decayed_risk *= 0.9
    
    return decayed_risk

# Data transformation with tuple unpacking (irrelevant but realistic)
def extract_context(metadata):
    base, readings, _ = metadata['baseline'], metadata['readings'], metadata['timestamp']
    weighted_sum = sum(r * (i+1) for i, r in enumerate(readings))
    scale_factor = 2.0 if base > 0.7 else 1.5
    return (weighted_sum, scale_factor)

# Main processing pipeline
def process_metrics(entries, config):
    primary_metrics = []
    secondary_cache = []
    
    for entry in entries:
        val = entry.get('value')
        category = entry.get('type')
        
        # Conditional filtering with inline expression
        if category == 'sensor' and (val > 0.5 or config.get('allow_low', False)):
            scaled_val = val * 1.1 if config.get('calibrate', True) else val
            primary_metrics.append(scaled_val)
        else:
            secondary_cache.append(val * 0.5)  # Unused accumulation
    
    # Distractor: character counting in labels (no impact)
    total_chars = sum(len(e.get('label', '')) for e in entries)
    char_mod = total_chars % 7
    
    # Another decoy variable using modular arithmetic
    dummy_accum = 0
    for i in range(len(primary_metrics)):
        dummy_accum = (dummy_accum + i * 13) % 19
    
    # Actual evaluation using relevant metrics
    core_risk = evaluate_health(primary_metrics, config)
    
    # Final adjustment using conditional expression (required feature)
    final_boost = 1.25 if char_mod > 5 else 1.0
    boosted_result = core_risk * final_boost
    
    # This is the actual answer variable
    final_diagnostic = int(boosted_result * 1000)  # Scale to integer
    
    # Print required for traceability
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Simulated input data
log_entries = [
    {'value': 0.88, 'type': 'sensor', 'label': 'temp_01'},
    {'value': 0.72, 'type': 'sensor', 'label': 'voltage_mid'},
    {'value': 0.91, 'type': 'sensor', 'label': 'load_peak'},
    {'value': 0.65, 'type': 'network', 'label': 'latency_sample'},  # non-sensor excluded
    {'value': 0.83, 'type': 'sensor', 'label': 'flow_rate'}
]

system_flags = {
    'debug_mode': False,
    'calibrate': True,
    'allow_low': False
}

# Initial telemetry (unused in final path)
telemetry_data = collect_telemetry()
context_tuple = extract_context(telemetry_data)

# Checksum distractor (computed but not used)
dummy_checksum = compute_checksum(log_entries[0]['value'] * 100 for _ in range(1))

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_flags)