import itertools

# System telemetry simulation for a distributed sensor array
def monitor_sensor_array(telemetry_streams, baseline_threshold=0.75):
    stream_scores = []
    diagnostic_trace = []
    
    for stream in telemetry_streams:
        active_peaks = 0
        noise_floor = 0.1
        signal_strength = 0.0
        
        # Irrelevant peak detection (red herring)
        for reading in stream:
            if reading > 0.9:
                active_peaks += 1

        # Core signal integration (relevant path)
        filtered_readings = [r for r in stream if r > noise_floor]
        if filtered_readings:
            signal_strength = sum(filtered_readings) / len(filtered_readings)
        
        score = signal_strength * (1 + active_peaks * 0.05)
        stream_scores.append(score)
        diagnostic_trace.append((score, active_peaks))

    return stream_scores, diagnostic_trace

# Decoy function - looks important but unused
def legacy_compatibility_mode(data, mode='basic'):
    if mode == 'advanced':
        return [x ** 0.5 for x in data if x > 0]
    return [x for x in data if x < 1]

# Data transformation pipeline with distractors
def transform_spectral_data(raw_spectrum):
    # Distractor: frequency masking (unused later)
    masked_frequencies = [f for f in raw_spectrum if 0.2 <= f <= 0.8]
    normalized = [f * 1.25 for f in raw_spectrum]
    
    # Real processing path
    shifted = [abs(f - 0.5) for f in normalized]
    inverted = [1.0 - s for s in shifted]
    return list(itertools.accumulate(inverted, lambda a, b: a * 0.9 + b))

# Main diagnostic aggregator (critical function)
def aggregate_diagnostics(log, flags):
    base_weight = 0.6
    flag_bonus = 0.0
    
    # Irrelevant flag decoding (misleading)
    if 'STANDBY_OVERRIDE' in flags:
        flag_bonus += 0.1
    if 'CALIBRATION_LOCK' in flags:
        flag_bonus -= 0.05  # This never triggers

    # Core logic: extract and combine only specific trace entries
    valid_entries = [entry[0] for entry in log if entry[0] > 0.4]
    
    # Complex filtering using slicing and set operations (relevant)
    sorted_entries = sorted(valid_entries)
    mid_range = sorted_entries[1:-1] if len(sorted_entries) > 2 else sorted_entries
    unique_mid = list(set(mid_range))
    
    # Final computation
    if unique_mid:
        stability_factor = sum(unique_mid) / len(unique_mid)
        flag_bonus += 0.15 if 'STANDBY_OVERRIDE' in flags else 0.0
        return int((stability_factor + flag_bonus) * 10000)
    else:
        return -1

# Simulated input data
sensor_1 = [0.12, 0.88, 0.91, 0.25, 0.67, 0.89]
sensor_2 = [0.05, 0.95, 0.33, 0.76, 0.81, 0.11]
sensor_3 = [0.99, 0.01, 0.54, 0.77, 0.77, 0.43]

# Generate stream scores and diagnostics (used)
technical_scores, diagnostics_log = monitor_sensor_array([sensor_1, sensor_2, sensor_3])

# Transform spectral data (partially irrelevant)
spectral_input = [0.1, 0.3, 0.5, 0.7, 0.9]
spectral_output = transform_spectral_data(spectral_input)

# Flag configuration (only STANDBY_OVERRIDE matters)
system_flags = ['STANDBY_OVERRIDE', 'TEMPORAL_FILTER']

# Critical assignment statement
final_diagnostic = aggregate_diagnostics(diagnostics_log, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")