import math

# System telemetry and decoy parameters
telemetry_snapshot = {
    'voltage': 234.5,
    'current_phase': 1.78,
    'temperature_celsius': 67.2,
    'humidity_ratio': 0.43,
    'pressure_kpa': 101.3
}

# Irrelevant sensor calibration data (red herring)
calibration_matrix = [
    [0.98, 1.02, 0.99],
    [1.01, 0.97, 1.03],
    [0.96, 1.04, 1.00]
]

# Simulated quantum buffer with bit-level artifacts
quantum_buffer = [0b11010110, 0b10110011, 0b11100010, 0b00110101]

# Historical log entries - some relevant, some not
system_log = [
    {'event': 'power_on', 'timestamp': 1001, 'severity': 1},
    {'event': 'sync_fail', 'timestamp': 1023, 'severity': 4},
    {'event': 'retry_init', 'timestamp': 1028, 'severity': 2},
    {'event': 'data_align', 'timestamp': 1055, 'severity': 1},
    {'event': 'phase_lock', 'timestamp': 1089, 'severity': 3}
]

# Unused diagnostic function (dead code path)
def legacy_diagnostic(seq):
    return sum((x >> 2) & 0x0F for x in seq) * 0.75

# Auxiliary transformation map (partially used)
transform_map = {
    1: lambda x: x ** 2,
    2: lambda x: x + 10 if x < 50 else x - 10,
    3: lambda x: int(bin(x)[::-1], 2),  # bit reverse
    4: lambda x: x ^ 0xFF  # one's complement
}

# Misleading intermediate calculation (distractor)
baseline_offset = (telemetry_snapshot['voltage'] * 0.1) + (telemetry_snapshot['pressure_kpa'] * 0.05)

# Decoy statistical aggregator (never called)
compute_anomaly_score = lambda logs, weight: sum(l['severity'] ** weight for l in logs)

# Critical processing function with nested logic and distractors
def analyze_quantum_sequence(buffer, threshold_multiplier=1.3):
    cumulative = 0
    shift_key = 0
    
    for i, byte in enumerate(buffer):
        # Extract high and low nibbles
        high_nibble = (byte >> 4) & 0x0F
        low_nibble = byte & 0x0F
        
        # Real computation: XOR of transformed nibbles
        transformed_high = transform_map[3](high_nibble)  # bit reverse
        transformed_low = transform_map[1](low_nibble)   # square
        
        # Distraction: irrelevant phase modulation simulation
        phase_mod = math.sin(i * 0.5) * baseline_offset
        
        # Actual contribution to result
        step_value = transformed_high ^ transformed_low
        if step_value > 7:
            step_value = transform_map[4](step_value)  # invert bits if > 7
        
        cumulative += (step_value * (i + 1))
        
        # Early termination red herring (condition never met due to data)
        if high_nibble == 0x0A:
            shift_key += 1
            break
    
    # Final adjustment using multiplier (not affected by break)
    return int(cumulative * threshold_multiplier)

# Secondary analysis with dictionary reduction
def evaluate_event_risk(log_entries):
    severity_count = {}
    for entry in log_entries:
        sev = entry['severity']
        if sev not in severity_count:
            severity_count[sev] = 0
        severity_count[sev] += 1
    
    # Use lambda to compute weighted risk (only certain keys matter)
    risk_fn = lambda s: s * 3 if s >= 3 else s * 1
    total_risk = 0
    for k, v in severity_count.items():
        if k >= 2:  # only consider medium+ severity events
            total_risk += risk_fn(k) * v
    
    return total_risk

# Dummy function that looks important but does nothing critical
def normalize_telemetry(data):
    norm = {}
    for k, v in data.items():
        norm[k] = (v - min(data.values())) / (max(data.values()) - min(data.values())) if isinstance(v, (int, float)) else v
    return norm

# Main diagnostic workflow
normalized_telem = normalize_telemetry(telemetry_snapshot)  # unused result

# Begin real analysis chain
event_risk_score = evaluate_event_risk(system_log)

# Quantum sequence analysis (core component)
raw_quantum_score = analyze_quantum_sequence(quantum_buffer)

# Fake fusion algorithm (distractor)
fusion_metric = 0
for key, val in telemetry_snapshot.items():
    if 'temp' in key or 'humid' in key:
        fusion_metric += val * 0.2

# Final system state analysis - this is where the answer is determined
def analyze_system_state(qbuf, log):
    q_score = analyze_quantum_sequence(qbuf)
    e_risk = evaluate_event_risk(log)
    
    # Core decision logic with early exit
    if q_score < 100:
        return -1  # system unstable
    elif e_risk > 20:
        adjustment = 0
        for item in log:
            if item['timestamp'] > 1050:
                adjustment += 1
        return q_score - (adjustment * 2)
    else:
        # This branch is taken
        base = q_score // 3
        modifier = len([b for b in qbuf if (b & 0x0F) % 2 == 1])  # count odd low nibbles
        return base + (modifier * 5)

# Execute main analysis
temp_diagnostic_hint = legacy_diagnostic(quantum_buffer)  # dead code call (no effect)

final_diagnostic = analyze_system_state(quantum_buffer, system_log)

print(f"Result: {final_diagnostic}")