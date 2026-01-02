import itertools

# Simulated sensor array data from a distributed monitoring system
def fetch_sensor_readings():
    raw_data = [127, 255, 192, 64, 32, 8, 16, 48]
    noise_floor = 7
    adjusted = [x ^ noise_floor for x in raw_data]
    return adjusted

# Legacy calibration routine (partially deprecated)
def apply_legacy_calibration(data):
    calibrated = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            calibrated.append(val * 1.05)
        else:
            calibrated.append(val * 0.98)
    return [int(x) for x in calibrated]

# Signal normalization using z-score approximation (simplified)
def normalize_signal(signal_stream):
    mean_estimate = sum(signal_stream) / len(signal_stream)
    variance_estimate = sum((x - mean_estimate) ** 2 for x in signal_stream) / len(signal_stream)
    std_dev = variance_estimate ** 0.5
    normalized = [(x - mean_estimate) / std_dev for x in signal_stream]
    return [round(x, 3) for x in normalized]

# Flag generation based on threshold crossing patterns
def generate_system_flags(norm_vals):
    flags = []
    for idx, val in enumerate(norm_vals):
        if val > 1.0:
            flags.append((idx, 'HIGH_VOLTAGE'))
        elif val < -1.0:
            flags.append((idx, 'LOW_VOLTAGE'))
        elif abs(val) < 0.1:
            flags.append((idx, 'STANDBY'))
        else:
            flags.append((idx, 'NORMAL'))
    return flags

# Auxiliary debug function (never called - red herring)
def log_diagnostic_trace(signal, labels):
    for i, (val, label) in enumerate(zip(signal, labels)):
        print(f'[DBG] Node {i}: {val} -> {label}')

# Unused transformation matrix (distractor)
transformation_matrix = [
    [1, 0, 0], [0, 1, 0], [0, 0, 1],
    [2, 1, 0], [1, 2, 1], [0, 1, 2]
]

# Simulated environmental interference (unused but plausible)
environmental_jitter = list(itertools.accumulate([1, -1, 1, -1, 1], lambda x, y: (x + y) % 4))
baseline_drift = [x * 0.01 for x in range(8)]

# Critical diagnostic aggregation engine
def aggregate_metrics(nsig, sflags):
    # Weighting logic based on flag severity
    severity_map = {
        'HIGH_VOLTAGE': 3,
        'LOW_VOLTAGE': 3,
        'NORMAL': 1,
        'STANDBY': 0
    }
    
    # Extract relevant indices and weights
    active_indices = [i for i, f in sflags if f != 'STANDBY']
    weighted_sum = 0
    total_weight = 0
    
    # Core calculation with tuple unpacking and filtering
    for index, flag_type in sflags:
        if flag_type in severity_map and severity_map[flag_type] > 0:
            weight = severity_map[flag_type]
            raw_contribution = nsig[index] * weight
            weighted_sum += raw_contribution
            total_weight += weight
    
    # Secondary adjustment using bitwise influence mask (simulated EMI effect)
    influence_mask = 0
    for i in active_indices:
        influence_mask ^= i << 1  # Bit shift and XOR accumulation
    
    # Final adjustment with masked contribution (only if non-zero)
    if influence_mask > 0:
        adjustment_factor = bin(influence_mask).count('1')  # Population count
        weighted_sum += adjustment_factor * 0.5
    
    # Normalize if possible, otherwise return raw adjusted sum
    if total_weight > 0:
        result = weighted_sum / total_weight
    else:
        result = weighted_sum
    
    return round(result, 6)

# Orchestration pipeline
if __name__ == '__main__':
    # Step 1: Fetch raw sensor data
    raw_signals = fetch_sensor_readings()
    
    # Step 2: Apply legacy calibration (required for compatibility)
    calibrated_signals = apply_legacy_calibration(raw_signals)
    
    # Step 3: Normalize signal stream for analysis
    normalized_signals = normalize_signal(calibrated_signals)
    
    # Step 4: Generate system status flags
    system_flags = generate_system_flags(normalized_signals)
    
    # Step 5: Compute final diagnostic metric
    final_diagnostic = aggregate_metrics(normalized_signals, system_flags)
    
    # Irrelevant post-processing (dead code path)
    if final_diagnostic > 10:
        final_diagnostic *= 0.95
    elif final_diagnostic < -5:
        magnitude = abs(final_diagnostic)
        final_diagnostic = -(magnitude ** 0.5)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")