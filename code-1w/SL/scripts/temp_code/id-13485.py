def analyze_event_sequence(events):
    # Irrelevant transformation: converts timestamps but not used in final result
    temp_timestamps = [e[0] % 100 for e in events if e[0] > 1000]
    filtered_events = [e for e in events if e[2] != 'DEBUG']

    # Misleading counter that looks important but is unused
    error_count_shadow = sum(1 for e in events if e[2] == 'ERROR')

    severity_map = {'CRITICAL': 5, 'ERROR': 4, 'WARN': 3, 'INFO': 2}
    total_severity = 0
    event_phases = []

    for idx, (timestamp, module, level, phase) in enumerate(filtered_events):
        weight = severity_map.get(level, 1)
        phase_id = hash(phase) % 7
        adjusted_weight = weight * (idx + 1) // (phase_id + 1)
        total_severity += adjusted_weight
        event_phases.append((idx, phase_id))

    return total_severity, event_phases


def compute_system_health(sensor_data, thresholds):
    # Dead code path: never called
    def legacy_calibrate(x):
        return (x * 0.97) + 3.2

    calibrated = [x * 1.02 for x in sensor_data]
    outliers = [c for c in calibrated if c > thresholds['max_critical']]
    
    # Distractor: complex-looking but irrelevant statistical moment
    moment_3 = sum((x - sum(calibrated)/len(calibrated))**3 for x in calibrated) / len(calibrated) if calibrated else 0

    healthy_count = sum(1 for x in calibrated if thresholds['min_safe'] <= x <= thresholds['max_safe'])
    return healthy_count


def extract_signatures(payload):
    # Uses string methods and slicing — relevant later
    chunks = payload.split('|')
    signatures = []
    for chunk in chunks:
        trimmed = chunk.strip()
        if len(trimmed) < 4:
            continue
        # Meaningful slicing: first two and last two chars
        sig = trimmed[:2] + trimmed[-2:]
        signatures.append(sig)
    return signatures


def aggregate_metrics(log_entries, system_flags):
    # Key function with multiple concepts
    base_score, phases = analyze_event_sequence(log_entries)
    
    # Decoy variable that mimics importance
    baseline_projection = base_score * 0.85 + len(phases) * 2
    
    # Health from sensors
    sensor_readings = [98, 95, 102, 88, 97, 110, 93]
    health_params = {'min_safe': 90, 'max_safe': 100, 'max_critical': 105}
    fitness_index = compute_system_health(sensor_readings, health_params)
    
    # Use of zip and enumerate together (required feature)
    adjustments = []
    for i, (phase_idx, pid) in enumerate(phases):
        adj = (base_score // (i + 1)) % (pid + 1) if i < len(phases) and pid > 0 else 0
        adjustments.append(adj)
    
    combined_adjustment = sum(adjustments)
    
    # String-based signature extraction — impacts final result
    raw_payload = "A1X9|B2Y8|C3Z7|D4W6"
    sigs = extract_signatures(raw_payload)
    sig_value = sum(ord(c) for s in sigs for c in s) % 1000  # Contributes to final answer
    
    # Control flow with short-circuit logic
    override_flag = system_flags.get('OVERRIDE') and system_flags.get('CONFIRMED')
    if override_flag and base_score > 50:
        final_diagnostic = 999
    else:
        # Actual computation path
        intermediate = base_score + fitness_index + combined_adjustment
        final_diagnostic = (intermediate * 3 + sig_value) // 7  # Final deterministic result

    # Unused red herring variables
    diagnostic_trace = {"score": base_score, "fitness": fitness_index, "adjust": combined_adjustment}
    audit_log = [f"Entry_{i}" for i in range(len(log_entries))]
    
    return final_diagnostic

# Main execution
log_data = [
    (1500, "net", "CRITICAL", "init"),
    (1501, "io", "ERROR", "run"),
    (1502, "mem", "WARN", "run"),
    (1503, "cpu", "INFO", "post")
]

flags = {"OVERRIDE": False, "CONFIRMED": True}  # Short-circuit prevents override

final_diagnostic = aggregate_metrics(log_entries=log_data, system_flags=flags)
print(f"Result: {final_diagnostic}")