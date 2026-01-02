import math

# Simulated sensor diagnostics from a spacecraft subsystem
def analyze_sensor_readings(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return {'baseline': baseline, 'deviation': std_dev, 'status': 'stable' if std_dev < 10 else 'unstable'}

# Irrelevant helper: computes harmonic mean (not used in final path)
def harmonic_mean(vals):
    if 0 in vals:
        return 0.0
    return len(vals) / sum(1/x for x in vals)

# Signal processing with conditional logic and dictionary operations
def filter_anomalies(signal_data, config):
    filtered = {}
    anomaly_count = 0
    for key, values in signal_data.items():
        clean_vals = [v for v in values if config['min'] <= v <= config['max']]
        if len(clean_vals) != len(values):
            anomaly_count += 1
        filtered[key] = clean_vals
    # Distraction: unused transformation
    temp_snapshot = {k: sum(v) for k, v in filtered.items()}
    scaling_factor = config.get('scale', 1)
    normalized = {k: [v * scaling_factor for v in vals] for k, vals in filtered.items()}
    return normalized, anomaly_count

# Core logic buried among distractors
def evaluate_health_metrics(metrics):
    score = 0
    penalties = []
    for name, data in metrics.items():
        avg = sum(data) / len(data)
        if avg < 50:
            penalties.append(10)
        elif avg < 75:
            penalties.append(5)
    health = 100 - sum(penalties)
    adjustment = len([p for p in penalties if p > 0])
    # Red herring: complex but unused adjustment curve
    curve_map = {0: 1.0, 1: 0.85, 2: 0.6, 3: 0.3}
    adjusted_health = health * curve_map.get(adjustment, 0.1)
    return adjusted_health  # Not actually used in final output

# Decoy function that looks important but is never called
def compute_integrity_check(data_map):
    total = 0
    for k, v in data_map.items():
        if isinstance(v, list) and len(v) > 0:
            total += abs(v[0] - v[-1])
    checksum = math.sin(total) * 100
    return round(checksum, 3)

# Main processing chain with nested logic and distractions
def process_signals(diag, thresh):
    # Step 1: Analyze each sensor group
    analysis_results = {}
    for subsystem, readings in diag.items():
        result = analyze_sensor_readings(readings)
        analysis_results[subsystem] = result
    
    # Step 2: Extract baselines into working dict
    baselines = {k: v['baseline'] for k, v in analysis_results.items()}
    
    # Step 3: Create composite signal (relevant)
    composite_signal = []
    for val in baselines.values():
        if val > thresh['critical']:
            composite_signal.append(val * 0.75)
        elif val > thresh['warning']:
            composite_signal.append(val * 0.9)
        else:
            composite_signal.append(val * 1.0)
    
    # Step 4: Apply threshold masking (distraction)
    masked_values = [c for c in composite_signal if c > thresh['filter_floor']]
    magnitude = sum(masked_values) if masked_values else 0.0
    
    # Step 5: Conditional transformation using dictionary get()
    multiplier = thresh.get('amplify', 1)
    amplified = magnitude * multiplier
    
    # Step 6: Final adjustment based on count (key dependency)
    count_factor = len(composite_signal) if amplified > 200 else len(masked_values)
    
    # Step 7: Introduce bit manipulation red herring
    binary_tag = 0b1010
    for val in composite_signal[:2]:
        binary_tag ^= int(val) & 0b1111
    # Unused tag computation
    
    # Step 8: Actual final computation
    adjustment_ratio = 0.8 if len(diag) > 3 else 1.0
    interim = amplified + count_factor
    final_output = interim * adjustment_ratio
    
    # Print required target result
    print(f"Target result: {final_output}")
    return final_output

# Simulated input data
sensor_diagnostics = {
    'propulsion': [120, 125, 118, 130],
    'navigation': [88, 92, 85, 90],
    'comms': [65, 67, 63, 70],
    'life_support': [105, 102, 108, 100]
}

threshold_settings = {
    'min': 50,
    'max': 150,
    'warning': 80,
    'critical': 100,
    'filter_floor': 70,
    'scale': 1.1,
    'amplify': 2
}

# Irrelevant pre-processing (dead code path)
raw_stats = [sum(vals) for vals in sensor_diagnostics.values()]
avg_raw = sum(raw_stats) / len(raw_stats)

deviation_flags = {key: 'FLAGGED' for key, vals in sensor_diagnostics.items() if max(vals) - min(vals) > 15}

# Execute main logic
diagnostics = sensor_diagnostics.copy()
thresholds = threshold_settings
final_output = process_signals(diagnostics, thresholds)