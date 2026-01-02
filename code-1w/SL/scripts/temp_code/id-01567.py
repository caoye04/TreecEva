def analyze_system_health(raw_logs, thresholds):
    # Irrelevant preprocessing (distractor)
    clean_logs = [entry.strip().lower() for entry in raw_logs if entry]
    filtered_logs = [log for log in clean_logs if 'error' not in log]
    temp_analysis = ''.join(filtered_logs)[:100]

    # Misleading metric calculation (red herring)
    anomaly_score = sum(1 for c in temp_analysis if c in 'xyz') * 3.7
    baseline_shift = len(temp_analysis) % 7 if anomaly_score > 10 else 0

    # Actual relevant data extraction
    severity_levels = []
    for entry in raw_logs:
        if 'CRITICAL' in entry:
            severity_levels.append(5)
        elif 'ERROR' in entry:
            severity_levels.append(3)
        elif 'WARN' in entry:
            severity_levels.append(2)

    # Dead code path - never executed due to logic (distractor)
    if baseline_shift < 0:
        correction_factor = -1
        adjusted_logs = [l[::-1] for l in filtered_logs]
        severity_levels.extend([correction_factor] * len(adjusted_logs))

    # Relevant aggregation with string method distraction
    log_text = ' '.join(raw_logs)
    heartbeat_count = log_text.count('HEARTBEAT')
    timeout_count = log_text.count('TIMEOUT')

    # Complex conditional expression (required feature)
    load_factor = 1.5 if timeout_count > 0 else (0.8 if heartbeat_count > 10 else 1.0)

    # Bit manipulation decoy (irrelevant but looks important)
    encoded_state = 0
    for i, char in enumerate('diagnostics'):
        encoded_state ^= ord(char) << (i % 4)
    encoded_state = encoded_state & 0xFFFF  # Mask to 16 bits

    # Core computation chain (actual answer path)
    avg_severity = sum(severity_levels) / len(severity_levels) if severity_levels else 0
    spike_count = sum(1 for s in severity_levels if s >= 3)
    stability_index = len(raw_logs) - timeout_count

    # Multiple nested operations with modular arithmetic
    trend_weight = (spike_count * 7) % 5
    normalized_stability = max(1, min(stability_index, 20))  # Clamp to 1-20

    # Conditional override based on system state (early return red herring)
    emergency_override = False
    if 'FAILSAFE_ACTIVATED' in log_text:
        return -999  # Dead code - condition never met

    # Distractor: unused function definition
    def calculate_entropy(data):
        from math import log2
        freq = {}
        for item in data:
            freq[item] = freq.get(item, 0) + 1
        total = len(data)
        return -sum((count/total) * log2(count/total) for count in freq.values())

    # Real processing begins here
    adjustment = 0
    if spike_count >= 3:
        adjustment += 2
    if timeout_count == 0:
        adjustment += 1

    # Final multi-step transformation
    base_metric = avg_severity * normalized_stability
    decay_factor = 0.9 ** spike_count
    refined_score = base_metric * decay_factor + adjustment

    # Secondary processing with string-based condition (required feature)
    system_age_str = "system_v2.1.9"
    version_numeric = float(system_age_str.split('_v')[1][:3])
    version_boost = 1.2 if 'beta' not in system_age_str else 0.8

    # Final diagnostic computed through complex chain
    final_diagnostic = int(refined_score * version_boost * load_factor)

    # Output requirement
    print(f"Result: {final_diagnostic}")

    # Irrelevant cleanup
    del encoded_state, anomaly_score

    return final_diagnostic


def process_metrics(log_entries, load_profile):
    # Wrapper that adds another layer of indirection
    threshold_map = {'critical': 5, 'warning': 3}
    temp_val = sum(threshold_map.get(k, 1) for k in load_profile.keys()) % 4

    result = analyze_system_health(log_entries, threshold_map)
    return result + temp_val - 2  # Net offset of +1 due to temp_val=3

# Simulated input data
logs = [
    "[TIMESTAMP_001] HEARTBEAT OK",
    "[TIMESTAMP_002] WARN disk_usage_high",
    "[TIMESTAMP_003] HEARTBEAT OK",
    "[TIMESTAMP_004] CRITICAL database_down",
    "[TIMESTAMP_005] ERROR connection_timeout",
    "[TIMESTAMP_006] WARN memory_leak_suspected",
    "[TIMESTAMP_007] HEARTBEAT OK",
    "[TIMESTAMP_008] CRITICAL service_crash",
    "[TIMESTAMP_009] ERROR auth_failure",
    "[TIMESTAMP_010] HEARTBEAT OK",
    "[TIMESTAMP_011] CRITICAL network_partition",
    "[TIMESTAMP_012] WARN cpu_spike"
]

load_stats = {
    'cpu_avg': 0.78,
    'mem_peak': 0.92,
    'disk_io': 340,
    'active_sessions': 117
}

# Entry point
final_diagnostic = process_metrics(logs, load_stats)