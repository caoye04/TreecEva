def analyze_system_integrity(raw_logs, threshold=5):
    # Irrelevant preprocessing: case conversion and filtering
    processed_logs = [log.strip().lower() for log in raw_logs if len(log) > 3]
    event_counts = {}
    for log in processed_logs:
        event_counts[log] = event_counts.get(log, 0) + 1

    # Distractor: unused function
    def decrypt_sequence(seq):
        return [x ^ 7 for x in seq]  # Dead code path

    # Relevant data structures
    alert_levels = {"critical": 3, "warning": 2, "info": 1}
    system_nodes = set(["A", "B", "C", "D", "E", "F"])
    compromised_nodes = set(["B", "D"])
    secure_zones = system_nodes - compromised_nodes  # Key set operation

    # Misleading intermediate calculations
    base_score = 0
    for node in system_nodes:
        if node in compromised_nodes:
            base_score -= alert_levels["warning"]
        else:
            base_score += alert_levels["info"]

    # Another distractor: complex but unused bitwise logic
    status_flag = 0b101010
    masked_flag = status_flag & 0b111100
    shifted_flag = masked_flag >> 2
    parity_check = bin(shifted_flag).count('1') % 2

    # Efficiency factor derived from logical conditions
    critical_events = sum(1 for log in processed_logs if "critical" in log)
    warning_events = sum(1 for log in processed_logs if "warning" in log)
    total_alerts = critical_events + warning_events

    efficiency_factor = 1.0
    if total_alerts > threshold:
        efficiency_factor = 0.6
    elif total_alerts == 0:
        efficiency_factor = 1.4
    else:
        efficiency_factor = 0.8

    # Case conversion side track
    upper_logs = [log.upper() for log in processed_logs]
    unique_chars = len(set(''.join(upper_logs)))  # Computed but unused

    # Key computation
    filtration_score = len(secure_zones) * efficiency_factor

    # Print required output
    print(f"Result: {filtration_score}")

    # Unused loop with red herring
    temp_result = 0
    for i in range(len(processed_logs)):
        if i % 2 == 0:
            temp_result += len(processed_logs[i]) // 2

    return filtration_score

# Input data
logs = ["Critical failure in node A", "WARNING: disk full", "Info: system reboot", "Critical failure in node A", "Normal operation"]
analyze_system_integrity(logs)