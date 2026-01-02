import math

def analyze_phase_coherence(timestamps, threshold=0.95):
    # Irrelevant helper function (dead code path)
    return sum(abs(a - b) for a, b in zip(timestamps, timestamps[1:])) < threshold

def evaluate_signal_integrity(raw_data, noise_floor):
    # Distractor computation with misleading intermediate result
    baseline = sum(raw_data) / len(raw_data)
    adjusted = [x for x in raw_data if x > noise_floor]
    power_envelope = sum(x ** 2 for x in adjusted)
    return power_envelope > 5000  # Unused return in actual logic

def extract_timing_segments(buffer, mask_pattern):
    # Bit manipulation red herring
    masked_values = []
    for val in buffer:
        masked = val & mask_pattern
        if masked % 3 == 0:
            masked_values.append(masked >> 1)
    return set(masked_values)  # Partially unused structure

def validate_handshake_protocol(sequence, retries=3):
    # Logical decoy with short-circuit evaluation
    if not sequence or retries <= 0:
        return False
    expected = sequence[0]
    for s in sequence[1:]:
        if s != expected + 1 and retries > 1:
            expected += 1
            continue
        expected += 1
    return True

def aggregate_metrics(log_entries, flags):
    # Core relevant logic begins here
    event_count = len(log_entries)
    critical_errors = sum(1 for e in log_entries if e['level'] == 'CRITICAL')
    warning_count = sum(1 for e in log_entries if e['level'] == 'WARNING')
    
    # Real computation path
    base_score = event_count * 17
    if critical_errors > 0:
        base_score -= critical_errors * 100
    if 'OVERLOAD' in flags:
        base_score -= 250
    if 'DEGRADED' in flags and warning_count > 2:
        base_score -= warning_count * 42
    
    # Tuple-based correction factor
    corrections = (1.0, 0.95, 0.8, 0.6, 0.3)
    correction_index = min(critical_errors, 4)
    applied_correction = corrections[correction_index]
    
    # Final diagnostic calculation
    final_diagnostic = int(base_score * applied_correction)
    
    # Red herring: irrelevant set operation
    unique_levels = set(entry['level'] for entry in log_entries)
    debug_snapshot = {k: v for k, v in flags.items() if 'DEBUG' in k}
    
    # Decoy conditional with no effect
    if len(unique_levels) == 3 and 'RETRY_INIT' in flags:
        final_diagnostic += 50  # Never reached due to flag absence
    
    return final_diagnostic

# Simulated system telemetry data (real input)
timing_log = [
    {'timestamp': 1623456780, 'level': 'INFO', 'source': 'SENSOR_A'},
    {'timestamp': 1623456781, 'level': 'WARNING', 'source': 'SENSOR_B'},
    {'timestamp': 1623456782, 'level': 'WARNING', 'source': 'CONTROL_X'},
    {'timestamp': 1623456783, 'level': 'CRITICAL', 'source': 'POWER_Y'},
    {'timestamp': 1623456784, 'level': 'WARNING', 'source': 'SENSOR_B'},
    {'timestamp': 1623456785, 'level': 'CRITICAL', 'source': 'LINK_Z'},
    {'timestamp': 1623456786, 'level': 'INFO', 'source': 'SENSOR_A'}
]

# Flag state with multiple distractors
system_flags = {
    'OVERLOAD': True,
    'DEGRADED': True,
    'FAN_OK': True,
    'VOLTAGE_STABLE': False,
    'DEBUG_TRACE': True,
    'TRACE_DEPTH': 5
}

# Dead function calls (misleading execution flow)
decoy_buffer = [0b11010, 0b10110, 0b11100, 0b10011]
decoy_mask = 0b11110
segment_set = extract_timing_segments(decoy_buffer, decoy_mask)
integrity_check = evaluate_signal_integrity([100, 200, 150, 300, 700], 50)
coherence = analyze_phase_coherence([0.1, 0.15, 0.22, 0.31, 0.45], 0.9)
handshake_ok = validate_handshake_protocol([1, 2, 4, 5], 2)

# Key statement that produces the answer
temp_result = sum(entry['timestamp'] for entry in timing_log) % 1000
final_diagnostic = aggregate_metrics(timing_log, system_flags)

print(f"Result: {final_diagnostic}")