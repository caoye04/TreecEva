import math

def analyze_event_risk(timestamp, severity_code):
    # Irrelevant risk analysis (distractor)
    base_risk = (timestamp % 7) * severity_code
    if base_risk > 20:
        return base_risk * 0.8
    else:
        return base_risk + 3


def compute_signal_strength(frequency, distance):
    # Distractor function: used in unrelated subsystem
    attenuation = 20 * math.log10(distance)
    return frequency / (attenuation + 1e-5)


def detect_anomalies(logs):
    # Real but indirect contributor: extracts suspicious entries
    anomalies = set()
    critical_ids = set()
    temp_buffer = []

    for entry in logs:
        log_id, code, time, status = entry
        if code > 5 and 'ERROR' in status:
            anomalies.add(log_id)
            temp_buffer.append(time)
        if code == 9:
            critical_ids.add(log_id)  # Rare but not directly used

    # Dead code path - never accessed in current logic
    if len(temp_buffer) == 0:
        temp_buffer.append(-1)

    return anomalies


def calculate_stability_index(readings):
    # Computes average deviation (distraction with partial relevance)
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    stability = 100 / (1 + variance) if variance > 0 else 100
    return round(stability, 2)


def monitor_system_health(log_entries, flags):
    # Core function containing key logic
    active_flags = {k: v for k, v in flags.items() if v is True}
    anomaly_set = detect_anomalies(log_entries)

    # Key data structures
    severity_levels = []
    timestamp_sequence = []
    id_sum = 0

    # Primary logic chain
    for entry in log_entries:
        eid, code, tstamp, msg = entry
        timestamp_sequence.append(tstamp)

        if eid in anomaly_set:
            severity_levels.append(code)
            id_sum ^= eid  # Bitwise accumulation (key step)

    # Intermediate distractor computation
    if len(severity_levels) > 0:
        max_sev = max(severity_levels)
        min_t = min(timestamp_sequence)
        range_t = max(timestamp_sequence) - min_t

        # Fake dependency
        fake_weight = max_sev * range_t / (min_t + 1)

        # Actual key calculation
        raw_score = sum(severity_levels) * 7
        id_contribution = id_sum & 0xFF  # Use last 8 bits

        # Control flow red herring
        if 'debug_mode' in active_flags:
            raw_score += 100  # Never reached

        # Real contribution
        adjustment = len(anomaly_set) if 'safe_mode' not in active_flags else 0
        final_score = raw_score + id_contribution - adjustment

        # Final decision logic
        if final_score > 200:
            health_code = 55
        elif final_score > 100:
            health_code = 42
        else:
            health_code = 10

        # Critical assignment
        final_diagnostic = health_code + 13
    else:
        final_diagnostic = 0

    # Dead code block (misleading)
    backup_logs = [e for e in log_entries if e[1] < 3]
    if len(backup_logs) % 2 == 0:
        final_diagnostic *= 2  # Not triggered due to logic above

    return final_diagnostic


# Simulated input data
log_data = [
    (101, 6, 1678800000, 'ERROR: timeout'),
    (102, 3, 1678800060, 'WARNING: retry'),
    (103, 8, 1678800120, 'ERROR: auth fail'),
    (104, 2, 1678800180, 'INFO: heartbeat'),
    (105, 7, 1678800240, 'ERROR: db down'),
]

system_config = {
    'debug_mode': False,
    'safe_mode': False,
    'audit_enabled': True,
    'encrypt_logs': True
}

# Execute main logic
final_diagnostic = monitor_system_health(log_data, system_config)
print(f"Result: {final_diagnostic}")