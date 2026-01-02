def analyze_system_status(raw_logs):
    # Parse and filter system logs
    entries = [line.split() for line in raw_logs if line.strip()]
    timestamps = [int(entry[0]) for entry in entries if len(entry) > 1]
    events = [entry[1] for entry in entries if len(entry) > 1]

    # Irrelevant transformation (distractor)
    event_stats = {}
    for e in set(events):
        event_stats[e] = events.count(e)

    # Extract numeric readings from log (key data)
    readings = []
    for entry in entries:
        if len(entry) > 2 and entry[1] == 'READ':
            try:
                readings.append(float(entry[2]))
            except ValueError:
                continue

    # Misleading statistical calculation (semi-relevant but unused)
    avg_reading = sum(readings) / len(readings) if readings else 0
    variance_proxy = sum((x - avg_reading) ** 2 for x in readings) / len(readings) if readings else 0

    return readings

# Additional helper with conditional expression
is_critical = lambda x: 'CRIT' if x > 85 else 'OK'

# Threshold logic using conditional expression
threshold_func = lambda x: x > 75 if x % 2 == 0 else x > 80

# Simulate sensor data processing
sensor_data = [
    "1001 INIT System A",
    "1002 READ 67.3",
    "1003 EVENT reboot",
    "1004 READ 82.1",
    "1005 READ 76.4",
    "1006 READ 88.9",
    "1007 READ 73.2",
    "1008 READ 91.5"
]

# Dead code path - never called (distractor)
def debug_snapshot(data):
    return {"size": len(data), "max_val": max(data) if data else 0}

# Core processing function
def process_readings(data_list, threshold_check):
    # Filter valid high-readings
    high_alerts = [val for val in data_list if threshold_check(val)]
    
    # Bitwise-based status flag (only even-indexed alerts contribute)
    flag_sum = 0
    for idx, val in enumerate(high_alerts):
        if idx % 2 == 0:
            flag_sum ^= int(val)  # XOR into diagnostic flag

    # Secondary filtering for average computation
    clipped_values = [v for v in high_alerts if v < 90]
    safe_average = round(sum(clipped_values) / len(clipped_values), 2) if clipped_values else 0.0

    # Final diagnostic combines multiple concepts
    base_score = len(high_alerts) * 10
    adjustment = sum(1 for v in data_list if v > 90) * -5  # penalty
    final_score = base_score + adjustment

    # This variable is the actual answer
    final_diagnostic = final_score + (flag_sum & 255)  # limit flag impact

    # Red herring: unused complex structure
    diagnostics_report = {
        "readings_count": len(data_list),
        "high_alerts_detail": [(i, v) for i, v in enumerate(high_alerts)],
        "safe_avg": safe_average,
        "temp_flag": flag_sum
    }

    return final_diagnostic

# Execution flow
parsed_readings = analyze_system_status(sensor_data)
final_diagnostic = process_readings(parsed_readings, threshold_func)
print(f"Result: {final_diagnostic}")