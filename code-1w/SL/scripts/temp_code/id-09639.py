import math

# Simulated sensor array data from environmental monitoring system
def acquire_sensor_data():
    raw_values = [23.4, 19.8, 20.1, 25.3, 18.7, 22.0, 24.8, 19.2]
    timestamps = [1623456780, 1623456790, 1623456800, 1623456810,
                  1623456820, 1623456830, 1623456840, 1623456850]
    return list(zip(timestamps, raw_values))

# Legacy calibration function (partially obsolete)
def apply_legacy_calibration(signal_list):
    calibrated = []
    for ts, val in signal_list:
        if val < 20.0:
            adjusted = val * 1.08
        elif val > 24.0:
            adjusted = val * 0.94
        else:
            adjusted = val * 1.02
        calibrated.append((ts, round(adjusted, 2)))
    return calibrated

# Signal smoothing using moving median (robust to outliers)
def smooth_signal(calibrated_data):
    smoothed_values = []
    values_only = [val for _, val in calibrated_data]
    
    for i in range(len(values_only)):
        window = values_only[max(0, i-1):min(i+2, len(values_only))]
        median_val = sorted(window)[len(window)//2]  # Simple median
        smoothed_values.append(round(median_val, 2))
    
    return [(calibrated_data[i][0], smoothed_values[i]) for i in range(len(smoothed_values))]

# Advanced noise detection (unused in final path - red herring)
def detect_noise_patterns(signal_seq):
    noise_flags = []
    diffs = [abs(signal_seq[i+1][1] - signal_seq[i][1]) for i in range(len(signal_seq)-1)]
    avg_diff = sum(diffs) / len(diffs)
    for d in diffs:
        noise_flags.append(d > 2.5 * avg_diff)
    return noise_flags  # Never actually used

# Main processing pipeline
def process_environmental_signals(raw_input):
    # Step 1: Apply legacy calibration
    calibrated_signals = apply_legacy_calibration(raw_input)
    
    # Step 2: Smooth the signal
    smoothed_signals = smooth_signal(calibrated_signals)
    
    # Step 3: Normalize timestamps to relative seconds
    base_time = smoothed_signals[0][0]
    normalized = [(ts - base_time, val) for ts, val in smoothed_signals]
    
    # Step 4: Extract values and compute rolling statistics
    values = [val for _, val in normalized]
    squared_devs = [(v - sum(values)/len(values))**2 for v in values]
    variance_estimate = sum(squared_devs) / len(squared_devs)
    stability_score = round(100 / (1 + variance_estimate), 2)
    
    # Step 5: Categorize readings (distractor computation)
    category_map = {}
    for val in values:
        cat = 'LOW' if val < 20.5 else 'HIGH' if val > 22.5 else 'NORMAL'
        category_map[round(val,1)] = cat
    
    # Step 6: Generate summary metrics (only one used later)
    summary_stats = {
        'count': len(values),
        'peak': max(values),
        'baseline': min(values),
        'average': round(sum(values)/len(values), 2),
        'stability': stability_score,
        'threshold_met': any(v > 21.0 for v in values),
        'duration': normalized[-1][0] - normalized[0][0]
    }
    
    # Irrelevant transformation chain (dead code path)
    temp_array = [int(v * 10) for v in values]
    bit_analysis = [bin(x).count('1') for x in temp_array]
    parity_check = sum(bit_analysis) % 4
    encoded_stream = ''.join([hex(x)[2:] for x in temp_array])
    fingerprint = hash(encoded_stream) % 10000  # Not used
    
    # Actual return structure
    return {
        'timestamps': [ts for ts, _ in normalized],
        'readings': values,
        'metrics': summary_stats,
        'raw_source': raw_input  # For traceability
    }

# Diagnostic engine for processed signals
def analyze_readings(system_state):
    readings = system_state['readings']
    metrics = system_state['metrics']
    
    # Compute harmonic mean (more sensitive to low values)
    inv_sum = sum(1/v for v in readings if v != 0)
    harmonic_mean = round(len(readings) / inv_sum, 3)
    
    # Detect sustained high phase (logical condition chain)
    high_phase_start = None
    for i, val in enumerate(readings):
        if val > 22.0:
            high_phase_start = i
            break
    
    if high_phase_start is not None:
        high_duration = len(readings) - high_phase_start
        recent_trend = 'rising' if readings[-1] > readings[-2] else 'falling'
    else:
        high_duration = 0
        recent_trend = 'none'
    
    # Multi-factor diagnostic score
    base_score = harmonic_mean * 10
    duration_factor = 1 + (high_duration / len(readings))
    trend_modifier = 1.1 if recent_trend == 'rising' else 0.95
    stability_bonus = 1.2 if metrics['stability'] > 85 else 1.0
    
    preliminary_diagnostic = base_score * duration_factor * trend_modifier * stability_bonus
    
    # Final adjustment based on bit pattern of integer part (obscure but deterministic)
    int_part = int(preliminary_diagnostic)
    binary_rep = bin(int_part)[2:]
    ones_ratio = binary_rep.count('1') / len(binary_rep)
    final_adjustment = 0.8 + (ones_ratio * 0.4)  # Maps 0.8 to 1.2
    
    final_diagnostic = round(preliminary_diagnostic * final_adjustment, 3)
    
    # Dead code - misleading alternate calculation
    alternative_path = []
    for r in readings[:3]:
        transformed = math.log(r) * math.sin(r/10)
        alternative_path.append(transformed)
    crypto_hash = sum(ord(c) for c in str(metrics)) % 999  # Decoy value
    
    return final_diagnostic

# --- Execution Flow ---
if __name__ == '__main__':
    # Acquire initial sensor data
    sensor_data = acquire_sensor_data()
    
    # Process through pipeline
    processed_signals = process_environmental_signals(sensor_data)
    
    # Generate final diagnostic assessment
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")