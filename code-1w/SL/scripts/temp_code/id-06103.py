from collections import defaultdict, Counter

# Simulate sensor data processing with performance scoring
def analyze_readings(log_entries):
    readings_count = defaultdict(int)
    anomalies = []
    total_power = 0
    base_threshold = 42

    for entry in log_entries:
        sensor_id = entry['sensor']
        value = entry['val']
        timestamp = entry['ts']

        readings_count[sensor_id] += 1
        total_power += value ** 0.5

        if value > base_threshold * 2:
            anomalies.append(timestamp)

    return readings_count, len(anomalies), total_power

def normalize_metrics(raw_counts, size):
    norm_factor = max(raw_counts.values()) if raw_counts else 1
    return {k: round(v / norm_factor * 100, 2) for k, v in raw_counts.items()}

def calculate_performance(flags, metrics):
    base_score = sum(metrics.values())
    adjustment = 0

    # Complex conditional logic with red herrings
    temp_offset = 0
    for flag in flags:
        if 'calibration' in flag:
            temp_offset += 3.5
        elif 'maintenance' in flag:
            temp_offset -= 1.2  # Not actually used later
        else:
            temp_offset += 0.1

    # Distractor computation - looks important but unused
    diagnostic_trace = [base_score * 0.1 for _ in range(5)]
    trace_sum = sum(diagnostic_trace)

    # Actual logic path
    if len(flags) > 2:
        adjustment += 15
    if 'urgent' in flags:
        adjustment += 25
    elif 'pending' in flags:
        adjustment += 5
    else:
        adjustment += 10

    # Final score calculation
    final_component = base_score + adjustment

    # Additional irrelevant tracking
    audit_log = []
    for i in range(3):
        audit_log.append(f"Check {i}: OK")

    return int(final_component)

# Main execution block
if __name__ == "__main__":
    # Input data - realistic sensor logs
    logs = [
        {'sensor': 'A1', 'val': 85, 'ts': 1001},
        {'sensor': 'B2', 'val': 93, 'ts': 1002},
        {'sensor': 'A1', 'val': 47, 'ts': 1003},
        {'sensor': 'C3', 'val': 120, 'ts': 1004},
        {'sensor': 'B2', 'val': 65, 'ts': 1005},
        {'sensor': 'D4', 'val': 150, 'ts': 1006}
    ]

    # Step 1: Analyze raw readings
    counts, anomaly_count, power_metric = analyze_readings(logs)

    # Step 2: Normalize for scoring
    normalized = normalize_metrics(counts, len(logs))

    # Irrelevant intermediate transformation
    reversed_map = {v: k for k, v in normalized.items()}
    sorted_vals = sorted(reversed_map.keys(), reverse=True)

    # Bonus conditions (flags)
    bonus_flags = ['calibration_ok', 'system_stable', 'urgent']

    # Efficiency metrics from normalized sensor frequencies
    efficiency_metrics = normalized

    # Key statement: calculate final performance score
    final_score = calculate_performance(bonus_flags, efficiency_metrics)

    # Print result as required
    print(f"Result: {final_score}")