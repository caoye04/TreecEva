import itertools

# System telemetry simulation with diagnostic flags
def generate_telemetry(baseline, threshold=0.75):
    return [x * 1.05 for x in baseline if x > threshold]

# Irrelevant helper - simulates network jitter (dead code path)
def calc_jitter(samples):
    if not samples:
        return 0.0
    variance = sum((x - sum(samples)/len(samples))**2 for x in samples) / len(samples)
    return variance * 0.33

# Misleading data transformation (not used in final result)
def obsolete_normalization(data):
    max_val = max(data)
    return [round(x / max_val, 4) for x in data]

# Core processing function with key logic
def evaluate_stability(readings, config):
    tolerance = config.get('tolerance', 0.1)
    critical_floor = config['base'] * (1 - tolerance)
    
    # Filter valid readings above noise floor
    valid_readings = [r for r in readings if r >= critical_floor]
    
    # Compute decay-corrected average (relevant calculation)
    corrected_sum = 0
    decay_factor = 0.9
    for i, val in enumerate(valid_readings):
        corrected_sum += val * (decay_factor ** i)
    decay_avg = corrected_sum / len(valid_readings) if valid_readings else 0
    
    # Spurious secondary metric (distractor)
    peak_ratio = max(valid_readings) / min(valid_readings) if valid_readings else 0
    
    # Return only decay_avg as it's used downstream
    return decay_avg

# Unused legacy function for rollback estimation (red herring)
def estimate_rollback_points(events):
    timestamps = sorted([e[0] for e in events if e[1] == 'ERROR'])
    gaps = [t2 - t1 for t1, t2 in zip(timestamps, timestamps[1:])] if timestamps else []
    return len([g for g in gaps if g > 300])

# Main data processing pipeline
def process_metrics(events, state):
    # Extract sensor values using dictionary operations and filtering
    raw_values = [e['value'] for e in events if e['type'] == 'SENSOR']
    
    # Augment with offset from system state (key dependency)
    augmented = [v + state['offset'] for v in raw_values]
    
    # Apply generator-based transformation (itertools usage)
    grouped = list(itertools.groupby(sorted(augmented), key=lambda x: int(x)))
    reduced = [sum(val for val in vals) / len(list(vals)) for _, vals in grouped]
    
    # Configuration map for evaluation
    config_map = {
        'base': state['reference'],
        'tolerance': 0.12,
        'active': True
    }
    
    # Evaluate stability - this is the critical computation path
    stability_score = evaluate_stability(reduced, config_map)
    
    # Dead code: historical anomaly detection (never called)
    def detect_anomalies(seq):
        return [i for i in range(1, len(seq)-1) if abs(seq[i]-seq[i-1]) > 2*abs(seq[i+1]-seq[i])]
    
    # Final diagnostic computed from stability score
    adjustment = state['gain'] * 0.25
    final_diagnostic = round(stability_score * adjustment, 6)
    
    # Irrelevant aggregation (misleads with complex-looking code)
    entropy_proxy = -sum(p * __import__('math').log(p) for p in [0.1, 0.2, 0.7] if p > 0)
    
    return final_diagnostic

# Simulated input data
logged_events = [
    {'type': 'SENSOR', 'value': 23.1, 'ts': 1001},
    {'type': 'LOG', 'msg': 'OK', 'ts': 1002},
    {'type': 'SENSOR', 'value': 23.1, 'ts': 1003},
    {'type': 'SENSOR', 'value': 24.3, 'ts': 1004},
    {'type': 'SENSOR', 'value': 25.7, 'ts': 1005},
    {'type': 'ERROR', 'code': 42, 'ts': 1006},
    {'type': 'SENSOR', 'value': 25.7, 'ts': 1007},
    {'type': 'SENSOR', 'value': 26.9, 'ts': 1008},
]

system_state = {
    'reference': 24.0,
    'offset': 1.5,
    'gain': 4.0,
    'mode': 'ACTIVE'
}

# Generate intermediate datasets (some irrelevant)
telemetry_data = generate_telemetry([0.1, 0.3, 0.8, 0.9, 1.0], threshold=0.75)
normalized_telem = obsolete_normalization(telemetry_data)  # Dead assignment
jitter_metric = calc_jitter([0.1, 0.4, 0.2])  # Irrelevant computation

# Critical execution point
final_diagnostic = process_metrics(logged_events, system_state)

# Output target result
print(f"Target result: {final_diagnostic}")