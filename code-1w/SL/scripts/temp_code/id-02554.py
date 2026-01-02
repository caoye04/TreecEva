import itertools

# Simulated sensor array data and system state flags
def process_sensor_array(raw_readings, calibration_factor=1.05):
    filtered = [x for x in raw_readings if x > 0]
    adjusted = [x * calibration_factor for x in filtered]
    baseline_offset = sum(adjusted) / len(adjusted) if adjusted else 0
    
    # Irrelevant intermediate transformation (distractor)
    spectral_analysis = [abs((x - baseline_offset) ** 0.5) for x in adjusted]
    peak_detection = max(spectral_analysis) if spectral_analysis else 0
    entropy_approx = sum(1 for x in spectral_analysis if x > 0.7 * peak_detection)

    # Relevant path: normalization step
    normalized = [round((x - baseline_offset) * 1.1, 6) for x in adjusted]
    return normalized

# Misleading auxiliary function (dead code path)
def deprecated_signal_filter(signal_list):
    """This function is no longer used but appears relevant."""
    return list(itertools.compress(signal_list, [x % 2 == 0 for x in range(len(signal_list))]))

# System diagnostic flag interpreter
def decode_system_flags(flag_bytes):
    # Parse bit-encoded status flags from hardware
    combined_flag = 0
    for fb in flag_bytes:
        combined_flag |= fb
    
    # Extract specific bits (bit manipulation red herring)
    power_state = (combined_flag >> 3) & 1
    thermal_alert = (combined_flag >> 7) & 1
    io_lockdown = (combined_flag >> 1) & 1
    
    # Actual relevant logic: checksum of active flags
    flag_sum = bin(combined_flag).count('1')
    critical_count = thermal_alert + io_lockdown
    
    # Decoy calculation (irrelevant)
    security_nonce = (combined_flag ^ 0xAA) & 0xFF
    
    # Only this matters: weighted significance
    return flag_sum * 3 + critical_count * 5

# Signal coherence validation (unused but plausible)
def validate_coherence(signals):
    if len(signals) < 2:
        return True
    diffs = [abs(signals[i+1] - signals[i]) for i in range(len(signals)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return avg_diff < 10

# Main aggregation logic
def aggregate_metrics(norm_signals, flags):
    # Apply windowed averaging using itertools
    windows = list(itertools.pairwise(norm_signals))
    if not windows:
        window_avg = 0
    else:
        window_avg = sum((a + b) / 2 for a, b in windows) / len(windows)
    
    # Secondary metric: count of positive deviations
    baseline_estimate = sum(norm_signals) / len(norm_signals)
    positive_spikes = sum(1 for x in norm_signals if x > baseline_estimate)
    
    # Distractor: unused spike analysis
    spike_pairs = list(itertools.combinations([x for x in norm_signals if x > baseline_estimate], 2))
    potential_interference = len(spike_pairs) > 5
    
    # Hidden relevant operation: product of non-zero normalized values
    nonzero_product = 1
    zero_count = 0
    for val in norm_signals:
        if abs(val) > 1e-6:
            nonzero_product *= abs(val)
        else:
            zero_count += 1
    
    # Final computation (only some components are actually used)
    signal_metric = round(nonzero_product ** 0.1, 6)
    flag_influence = flags * 0.7
    
    # The real answer comes from this combination only
    result = int((signal_metric + flag_influence) * 1000)
    return result

# --- Entry Point ---
if __name__ == '__main__':
    # Simulated input data
    raw_sensor_data = [12, -5, 23, 18, 31, -2, 19, 25, 14]
    system_status_flags = [0b10101010, 0b11000011, 0b00111100]

    # Step 1: Process sensor readings (generates normalized signals)
    normalized_signals = process_sensor_array(raw_sensor_data, calibration_factor=1.05)
    
    # Step 2: Decode system flags (generates flag score)
    system_flags = decode_system_flags(system_status_flags)
    
    # Step 3: Aggregate metrics - KEY EXECUTION POINT
    final_diagnostic = aggregate_metrics(normalized_signals, system_flags)
    
    # Irrelevant downstream operations (red herrings)
    diagnostic_chain = []
    for i in range(3):
        temp_diag = (final_diagnostic ^ (0xBEEF + i)) % 10000
        diagnostic_chain.append(temp_diag)
    
    # Final output (only final_diagnostic matters)
    print(f"Result: {final_diagnostic}")