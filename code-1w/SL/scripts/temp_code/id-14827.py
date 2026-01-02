def system_check(log, threshold):
    # Irrelevant diagnostic counters (distractors)
    debug_cycles = 0
    temp_buffer = [0] * 15
    anomaly_count = 0
    calibration_offset = sum([i % 4 for i in range(10)])  # Red herring computation

    # Real logic begins: analyze event severities
    severity_map = {"OK": 1, "WARN": 2, "ERROR": 3, "CRITICAL": 4}
    filtered_entries = {k: v for k, v in log.items() if v != "OK"}  # dict comprehension

    # Simulate sensor decay correction (unused path)
    corrected_values = []
    for i in range(len(temp_buffer)):
        corrected_values.append(temp_buffer[i] + (i * 0.1) - calibration_offset)

    # Critical path: compute weighted risk score
    risk_score = 0
    for tag, status in log.items():
        base_level = severity_map.get(status, 0)
        if base_level >= threshold:
            if tag.startswith("S"):
                risk_score += base_level * 2
            elif tag.startswith("A"):
                risk_score += base_level * 3
            else:
                risk_score += base_level

    # Decoy branching: looks important but unused
    if risk_score > 20:
        anomaly_count += 5
        debug_cycles = 100
        post_process_flag = True
        shadow_copy = log.copy()
        for key in shadow_copy:
            if "temp" in key:
                del shadow_copy[key]

    # Secondary analysis: count critical subsystems
    critical_subsystems = set()
    for key in log:
        prefix = key.split('_')[0]
        if prefix in ["S", "A", "P"] and log[key] == "CRITICAL":
            critical_subsystems.add(prefix)

    # Final aggregation with conditional expression
    subsystem_penalty = len(critical_subsystems) * 10 if critical_subsystems else 0
    final_risk = risk_score + subsystem_penalty

    # Misleading normalization (not actually used in output)
    normalized_diagnostic = round(final_risk / (1 + calibration_offset), 6)

    # Key assignment: this is the answer variable
    final_diagnostic = final_risk - 5  # Core deterministic result

    # Dead code path: never executed due to fixed threshold
    if threshold < 0:
        reset_sequence = [0] * 10
        for i in range(len(reset_sequence)):
            reset_sequence[i] = i * calibration_offset

    return final_diagnostic

# Setup realistic input data
results_log = {
    "S_01": "OK",
    "S_02": "ERROR",
    "A_03": "CRITICAL",
    "P_04": "WARN",
    "S_05": "CRITICAL",
    "M_06": "OK",
    "A_07": "ERROR",
    "P_08": "CRITICAL"
}
active_threshold = 2

# Execute critical statement
final_diagnostic = system_check(results_log, active_threshold)

print(f"Result: {final_diagnostic}")