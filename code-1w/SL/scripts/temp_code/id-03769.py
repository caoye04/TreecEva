import itertools

# Simulated spacecraft telemetry and fault diagnosis system
def process_telemetry_chunk(chunk):
    accumulated = 0
    for val in chunk:
        if val < 0:
            accumulated ^= val & 0xF
        elif val > 100:
            accumulated += val % 17
        else:
            accumulated -= (val // 3) ^ 2
    return accumulated

# Irrelevant helper - simulates sensor calibration (dead code path)
def calibrate_sensors(baseline):
    adjustment = 0
    for i in range(len(baseline)):
        if i % 3 == 0:
            adjustment += baseline[i] * 0.1
    return adjustment  # Never used

# Misleading intermediate function - computes decoy metric
def compute_decoherence_index(data_stream):
    index = 0
    pairs = list(itertools.combinations(data_stream[:8], 2))
    for a, b in pairs:
        if (a + b) % 5 == 0:
            index += 1
    return index * 1.5  # Looks important but unused in final result

# Core diagnostic logic
def detect_anomaly_patterns(log_segment):
    critical_flags = set()
    for i, reading in enumerate(log_segment):
        if reading in [231, 184, 97]:
            critical_flags.add(i % 4)
        elif reading > 200 and reading % 2 == 1:
            critical_flags.discard((i-1) % 4) if (i-1)%4 in critical_flags else None
    return critical_flags

# Red herring: Power subsystem analysis (not connected to output)
def analyze_power_rails(voltage_trace):
    spike_count = 0
    for v in voltage_trace:
        if 110 < v < 115 or v > 220:
            spike_count += 1
    normalized_score = spike_count / len(voltage_trace) if voltage_trace else 0
    return normalized_score

# Real computation path buried among distractions
def fuse_diagnostic_signals(primary, secondary, threshold=5):
    signal_chain = []
    for p, s in zip(primary, secondary):
        fused = (p ^ s) + (p & 7) - (s % 9)
        signal_chain.append(fused)
    
    # Apply moving window filter (3-level nesting here)
    filtered = []
    for i in range(2, len(signal_chain)):
        window_avg = sum(signal_chain[i-2:i+1]) / 3
        if abs(window_avg - signal_chain[i]) < threshold:
            filtered.append(int(window_avg))
    
    return sum(filtered) if filtered else 0

# Key function that produces the answer
def analyze_fault_sequence(telemetry_log, system_flags):
    # Step 1: Process raw telemetry
    chunked_result = process_telemetry_chunk(telemetry_log)
    
    # Step 2: Detect pattern-based anomalies
    anomaly_set = detect_anomaly_patterns(telemetry_log)
    
    # Step 3: Generate secondary signal from system flags
    flag_values = [f * 37 for f in system_flags]
    
    # Step 4: Fuse two diagnostic dimensions
    fused_diagnostics = fuse_diagnostic_signals(
        [chunked_result, len(anomaly_set), sum(flag_values)],
        [system_flags[0], 42, len(telemetry_log)]
    )
    
    # Step 5: Final computation (answer derivation)
    entropy_component = len(anomaly_set) ** 2
    stability_offset = telemetry_log.count(42) * -8
    final_diagnostic = fused_diagnostics + entropy_component + stability_offset
    
    # Numerous irrelevant computations below (distractors)
    decoherence = compute_decoherence_index(telemetry_log)  # Unused
    power_diag = analyze_power_rails([120, 118, 221, 122, 119])  # Unused
    calibrated = calibrate_sensors([1,2,3,4,5])  # Dead code
    temp_flag = (len(telemetry_log) + decoherence) % 13  # Nowhere used
    
    return final_diagnostic

# Main execution with realistic data
if __name__ == '__main__':
    # Simulated telemetry log from satellite subsystem
    telemetry_log = [
        231, 42, 184, 97, 104, 203, 42, 177,
        88, 191, 42, 133, 231, 42, 97, 152
    ]
    
    # System operational flags (bit-encoded status)
    system_flags = [1, 0, 1, 1, 0, 1]
    
    # Critical execution point
    final_diagnostic = analyze_fault_sequence(telemetry_log, system_flags)
    
    # Irrelevant post-processing (more distraction)
    summary_stats = {
        'max_telem': max(telemetry_log),
        'flag_xor': system_flags[0] ^ system_flags[-1],
        'pair_count': len(list(itertools.combinations(system_flags, 2)))
    }
    
    # Only this line matters
    print(f"Result: {final_diagnostic}")