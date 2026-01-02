import math

# Simulated sensor data from wind turbine array
turbine_readings = [
    [3.2, 4.1, 5.0, 3.8, 4.5],
    [2.9, 3.7, 4.6, 4.2, 5.1],
    [3.3, 4.0, 4.8, 3.9, 4.7],
    [3.0, 3.6, 4.4, 4.3, 5.0]
]

# Irrelevant auxiliary data (distractor)
pressure_zones = [[1013, 1015], [1012, 1010], [1014, 1016], [1009, 1011]]
humidity_levels = [45, 52, 58, 47, 50]

# Calibration coefficients for sensor drift correction (some are decoys)
calibration_map = {
    'gain': [1.02, 0.98, 1.01, 0.99, 1.03],
    'offset': [0.1, -0.2, 0.15, -0.1, 0.05],
    'thermal_drift': [0.05, 0.03, 0.07, 0.02, 0.04]  # Unused
}

# Historical performance log (dead code path)
def update_historical_log(entry):
    if entry['efficiency'] > 0.85:
        status = 'OPTIMAL'
    elif entry['efficiency'] > 0.75:
        status = 'ACCEPTABLE'
    else:
        status = 'DEGRADED'
    return {'status': status, 'timestamp': 'N/A'}

# Unused transformation function (decoy)
def compute_fourier_magnitude(signal):
    N = len(signal)
    fft_result = []
    for k in range(N):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = -sum(signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        fft_result.append(math.sqrt(real**2 + imag**2))
    return [round(x, 3) for x in fft_result]

# Auxiliary processing with red herring logic
def analyze_vibration_pattern(vib_data):
    envelope = [abs(x - sum(vib_data)/len(vib_data)) for x in vib_data]
    threshold = 0.5
    spikes = [i for i, e in enumerate(envelope) if e > threshold]
    return len(spikes) > 0  # Not used in main flow

# Real-time anomaly detection stub (irrelevant)
active_alerts = []
for idx, readings in enumerate(turbine_readings):
    if max(readings) - min(readings) > 1.5:
        active_alerts.append(f'Turbine-{idx+1}-VARIANCE')

# Core diagnostic engine
def normalize_readings(raw_data, calib_coeffs):
    corrected = []
    for row in raw_data:
        adjusted = [
            (val * calib_coeffs['gain'][i] + calib_coeffs['offset'][i])
            for i, val in enumerate(row)
        ]
        corrected.append(adjusted)
    return corrected

# Secondary validation filter (partially used)
validation_rules = lambda x: all(2.0 < val < 5.5 for val in x)

# Data fusion and metric aggregation
def aggregate_metrics(sensor_data, calibration):
    # Step 1: Apply calibration
    calibrated_data = normalize_readings(sensor_data, calibration)
    
    # Step 2: Filter valid sequences
    valid_sequences = [seq for seq in calibrated_data if validation_rules(seq)]
    
    # Step 3: Compute per-turbine efficiency scores
    efficiency_scores = []
    for seq in valid_sequences:
        avg_reading = sum(seq) / len(seq)
        variance = sum((x - avg_reading) ** 2 for x in seq) / len(seq)
        efficiency = avg_reading / (1 + variance * 0.1)
        efficiency_scores.append(efficiency)
    
    # Step 4: Cross-reference with auxiliary indices (red herring)
    dummy_index = [math.sin(i * 0.5) for i in range(len(efficiency_scores))]
    weighted_sum = sum(eff * (1 + 0.1 * math.cos(idx)) 
                       for idx, eff in enumerate(efficiency_scores))
    
    # Step 5: Apply final diagnostic algorithm
    baseline = 3.7
    adjustments = []
    for i, (orig_row, calib_row) in enumerate(zip(sensor_data, calibrated_data)):
        orig_avg = sum(orig_row) / len(orig_row)
        calib_avg = sum(calib_row) / len(calib_row)
        delta = calib_avg - orig_avg
        adjustment_factor = delta * calibration['offset'][i % 5]
        adjustments.append(adjustment_factor)
    
    # Step 6: Aggregate final diagnostic score
    total_adjustment = sum(adjustments)
    base_performance = sum(efficiency_scores) / len(efficiency_scores)
    final_score = base_performance + total_adjustment * 0.2
    
    # Step 7: Apply hidden offset from unused data (misdirection)
    # Note: humidity_levels and pressure_zones are not actually used
    phantom_influence = 0.0  # Was intended but removed
    
    # Step 8: Final normalization using character count distraction
    # (Distractor comment: legacy requirement from old spec)
    magic_offset = len('diagnostic_engine_v3') * 0.01  # 20 chars → 0.2
    final_diagnostic = round(final_score + magic_offset, 6)
    
    return final_diagnostic

# Key execution point
calibration_sequence = {
    'gain': [1.02, 0.98, 1.01, 0.99, 1.03],
    'offset': [0.1, -0.2, 0.15, -0.1, 0.05],
    'thermal_drift': [0.05, 0.03, 0.07, 0.02, 0.04]
}

# Execute main pipeline
turbine_data = turbine_readings
final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
print(f"Result: {final_diagnostic}")