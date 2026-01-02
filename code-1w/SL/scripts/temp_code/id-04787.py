import math

# Simulated sensor array diagnostics with noise filtering and calibration
sensor_ids = [f'SEN-{i:03d}' for i in range(1, 17)]
raw_signals = [round(math.sin(i * 0.5) * 100 + (i % 3) * 5, 2) for i in range(16)]
timestamps = [1623456000 + i * 60 for i in range(16)]

# Irrelevant auxiliary data (distractor)
environment_logs = {
    'humidity': [45, 46, 48, 50, 55, 60, 62, 61, 59, 56, 52, 50, 49, 47, 46, 45],
    'temperature_c': [22.1, 22.3, 22.6, 23.0, 23.5, 24.1, 24.6, 25.0, 25.1, 25.0, 24.8, 24.5, 24.2, 23.9, 23.6, 23.3],
    'pressure_mb': [1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004, 1003, 1002, 1001, 1000, 999, 998]
}

# Signal quality flags (partially relevant but used as red herring)
quality_flags = ['OK' if i % 4 != 2 else 'NOISE' for i in range(16)]
valid_indices = [i for i, flag in enumerate(quality_flags) if flag == 'OK']

# Nested diagnostic readings (core data structure)
nested_readings = [
    {
        'id': sensor_ids[i],
        'signal': raw_signals[i],
        'ts': timestamps[i],
        'meta': {
            'gain': 1.0 + (i % 3) * 0.1,
            'offset': -5 + (i % 5),
            'calibrated': False
        }
    } for i in range(16)
]

# Decoy function – looks important but unused (dead code path)
def analyze_spectral_components(signals):
    fft_magnitude = []
    for i in range(len(signals)):
        magnitude = 0
        for j in range(len(signals)):
            angle = 2 * math.pi * i * j / len(signals)
            magnitude += signals[j] * math.cos(angle)
        fft_magnitude.append(round(magnitude, 2))
    return fft_magnitude

# Auxiliary transformation (distractor computation)
shifted_signals = [sig * 1.05 for sig in raw_signals]
adjusted_signals = [sig + (5 if idx % 2 == 0 else -3) for idx, sig in enumerate(shifted_signals)]

# Conditional expression based normalization factor (relevant)
normalization_factor = 1.0 if sum(raw_signals) > 800 else 0.9

# Complex filtering with set operations (core logic)
active_zone_set = {f'SEN-{i:03d}' for i in range(5, 13)}
critical_zone_set = {f'SEN-{i:03d}' for i in range(1, 9)}
overlap_zone = active_zone_set & critical_zone_set  # Intersection

filtered_readings = [
    reading for reading in nested_readings 
    if reading['id'] in overlap_zone
]

# Calibration logic with conditional expressions and state mutation
baseline_reference = sum(r['signal'] for r in filtered_readings[:4]) / 4

calibration_factor = (
    1.25 if baseline_reference < 40 \
    else (1.15 if any(r['signal'] > 75 for r in filtered_readings) else 1.05)
)

# Misleading intermediate calculation (decoy metric)
avg_temperature = sum(environment_logs['temperature_c']) / len(environment_logs['temperature_c'])
thermal_drift_compensation = round(avg_temperature * 0.03, 3)

# Core aggregation function with multiple concepts
def aggregate_metrics(readings, calib):
    # Apply calibration and corrections
    calibrated_values = []
    for r in readings:
        corrected = (r['signal'] * calib * r['meta']['gain']) + r['meta']['offset']
        r['meta']['calibrated'] = True
        calibrated_values.append(corrected)
    
    # Compute statistical metrics (only mean is used later)
    mean_val = sum(calibrated_values) / len(calibrated_values)
    variance = sum((x - mean_val) ** 2 for x in calibrated_values) / len(calibrated_values)
    std_dev = math.sqrt(variance)
    
    # Determine outlier threshold (unused but distracting)
    lower_bound = mean_val - 1.5 * std_dev
    upper_bound = mean_val + 1.5 * std_dev
    
    # Filter outliers using list comprehension with condition
    filtered_calibrated = [v for v in calibrated_values if lower_bound <= v <= upper_bound]
    
    # Final diagnostic is weighted combination of mean and stability index
    stability_index = (max(filtered_calibrated) - min(filtered_calibrated)) / std_dev if std_dev != 0 else 0
    
    # Key result computation
    final_score = mean_val * 0.85 + (100 - stability_index * 10) * 0.15
    
    # Dead code branch – never executed but looks important
    if False:
        backup_system = {'status': 'STANDBY', 'last_sync': timestamps[-1]}
        return backup_system['status']
    
    return round(final_score, 4)

# Secondary decoy function (unused)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Spurious transformation chain (irrelevant)
denoised_signals = [s for s in raw_signals if quality_flags[raw_signals.index(s)] == 'OK']
smoothed_signals = [sum(denoised_signals[max(0,i-1):i+2])/len(denoised_signals[max(0,i-1):i+2]) for i in range(len(denoised_signals))]

# Main execution point
if __name__ == '__main__':
    # Irrelevant pre-check
    system_status = 'ACTIVE' if len([r for r in nested_readings if 'ERR' not in r['id']]) == 16 else 'DEGRADED'
    
    # Critical statement
    final_diagnostic = aggregate_metrics(filtered_readings, calibration_factor)
    
    # Output requirement
    print(f"Target result: {final_diagnostic}")