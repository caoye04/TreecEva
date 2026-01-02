def analyze_sensor_readings(readings):
    # Irrelevant preprocessing: normalize all values (not actually used)
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)), 4) for x in readings]
    
    # Distractor: frequency analysis with dead-end logic
    freq_map = {}
    for val in readings:
        freq_map[val] = freq_map.get(val, 0) + 1
    
    # Real computation: extract peaks above dynamic baseline
    baseline = sum(readings) / len(readings)
    peaks = [v for v in readings if v > baseline * 1.3]
    return peaks if len(peaks) > 0 else [baseline]


def compute_health_score(metrics, weights):
    # Complex but irrelevant weighted harmonic mean calculation (dead code path)
    try:
        inv_sum = sum(w / m for m, w in zip(metrics, weights) if m != 0)
        harm_mean = len(metrics) / inv_sum
    except:
        harm_mean = 0
    
    # Misleading fallback: uses arithmetic mean instead
    arith_mean = sum(metrics) / len(metrics)
    return round(arith_mean, 3)


def validate_turbine_sequence(sequence):
    # Bit manipulation red herring
    checksum = 0
    for s in sequence:
        checksum ^= int(s * 17) & 0xF
    
    # Unused recursive validation (decoy function)
    def verify_recursive(data, idx=0):
        if idx >= len(data):
            return True
        if data[idx] < 0:
            return False
        return verify_recursive(data, idx + 2)
    
    # Actual simple rule: check monotonic increase in second half
    mid = len(sequence) // 2
    return all(sequence[i] <= sequence[i+1] for i in range(mid, len(sequence)-1))

# Main data processing chain
def aggregate_metrics(sensor_data, config_map):
    results = []
    
    # Enumerate over turbine systems with zip to align metadata
    for idx, (turbine_id, readings) in enumerate(zip(config_map['ids'], sensor_data)):
        
        # Extract thresholds using complex lookup (some irrelevant)
        critical_level = config_map['thresholds'].get(turbine_id, {}).get('critical', 85)
        warning_level = config_map['thresholds'].get(turbine_id, {}).get('warning', 60)
        
        # Real signal: analyze only turbines with valid sequence pattern
        raw_metrics = analyze_sensor_readings(readings)
        peak_value = max(raw_metrics)
        
        # Control flow with early exit red herring
        if peak_value > 100:
            # This block looks important but is logically unreachable due to clamping below
            results.append(0)
            continue
        
        # Actual processing: clamp and scale
        clamped_peak = min(peak_value, 95)
        adjusted = clamped_peak * 0.9
        
        # Conditional branching based on validation (only some turbines are valid)
        if validate_turbine_sequence(readings):
            adjusted *= 1.1
        
        # Use set operations to detect anomaly patterns (partially relevant)
        unique_anomalies = set(readings) & {99, 101, 103}
        if len(unique_anomalies) > 0:
            adjusted -= 5
        
        results.append(round(adjusted, 2))
    
    # Final aggregation: use only last three turbines (key insight)
    focus_group = results[-3:]
    
    # Compute final diagnostic score
    final_diagnostic = int(sum(focus_group) / len(focus_group))
    return final_diagnostic

# Simulated input data
sensor_data = [
    [45, 50, 52, 55, 53, 51],           # Turbine A: low readings
    [60, 68, 72, 79, 83, 88],           # Turbine B: rising trend
    [70, 75, 80, 88, 91, 94],           # Turbine C: high, valid sequence
    [55, 60, 65, 70, 75, 80],           # Turbine D: steady rise
    [40, 42, 41, 44, 43, 45]            # Turbine E: stable low
]

threshold_map = {
    'ids': ['T-A7', 'T-B2', 'T-C9', 'T-D4', 'T-E1'],
    'thresholds': {
        'T-A7': {'warning': 50, 'critical': 90},
        'T-B2': {'warning': 55, 'critical': 85},
        'T-C9': {'warning': 60, 'critical': 95},
        'T-D4': {'warning': 65, 'critical': 80},
        'T-E1': {'warning': 45, 'critical': 75}
    }
}

# Execute main logic
turbine_data = sensor_data
final_diagnostic = aggregate_metrics(turbine_data, threshold_map)
print(f"Target result: {final_diagnostic}")