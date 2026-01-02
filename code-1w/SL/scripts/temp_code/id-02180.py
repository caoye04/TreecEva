from collections import defaultdict, Counter

# Simulate sensor data processing for a diagnostic system
def analyze_readings(readings):
    stats = defaultdict(int)
    temp_readings = []
    pressure_events = 0

    for r in readings:
        category = r['type']
        value = r['value']
        timestamp = r['time']

        if category == 'temperature':
            temp_readings.append(value)
            stats['temp_count'] += 1
            if value > 75:
                stats['overheat_events'] += 1
        elif category == 'pressure':
            stats['pressure_sum'] += value
            if value > 100:
                pressure_events += 1

    # Irrelevant aggregation
    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
    stats['avg_temp'] = avg_temp
    stats['pressure_alerts'] = pressure_events

    # Dummy transformation
    transformed = [x * 0.95 + 2 for x in temp_readings]
    stats['adjusted_avg'] = sum(transformed) / len(transformed) if transformed else 0

    return stats


def compute_stability_index(log_entries, limits):
    severity_score = 0
    fluctuation_count = 0
    baseline = None

    for entry in log_entries:
        current = entry['metric']
        if baseline is not None:
            change = abs(current - baseline)
            if change > limits['delta_threshold']:
                fluctuation_count += 1
            baseline = current
        else:
            baseline = current

        # Accumulate severity based on range violations
        if current > limits['critical_high']:
            severity_score += 3
        elif current > limits['warning_high']:
            severity_score += 1

    # Complex but partially redundant logic
    penalty_factor = 1.0
    if fluctuation_count > 5:
        penalty_factor = 1.75
    elif fluctuation_count > 2:
        penalty_factor = 1.4

    index = (severity_score * penalty_factor) + (fluctuation_count * 0.5)

    # Additional computation that doesn't affect final result
    outlier_report = Counter([e['source'] for e in log_entries if e['metric'] > limits['warning_high']])
    total_outliers = sum(outlier_report.values())
    avg_per_source = total_outliers / len(outlier_report) if outlier_report else 0

    return int(index)

# Main execution flow
sensor_data = [
    {'type': 'temperature', 'value': 68, 'time': 100},
    {'type': 'pressure', 'value': 95, 'time': 101},
    {'type': 'temperature', 'value': 70, 'time': 102},
    {'type': 'temperature', 'value': 82, 'time': 103},
    {'type': 'pressure', 'value': 105, 'time': 104},
    {'type': 'temperature', 'value': 76, 'time': 105},
    {'type': 'temperature', 'value': 88, 'time': 106},
    {'type': 'temperature', 'value': 69, 'time': 107}
]

# Analyze raw readings (distractor call)
analysis_result = analyze_readings(sensor_data)

# Prepare health log from relevant subset
health_log = [
    {'metric': 68, 'source': 'T1'},
    {'metric': 70, 'source': 'T1'},
    {'metric': 82, 'source': 'T1'},
    {'metric': 76, 'source': 'T1'},
    {'metric': 88, 'source': 'T1'},
    {'metric': 69, 'source': 'T1'}
]

# Thresholds for stability computation
thresholds = {
    'warning_high': 75,
    'critical_high': 85,
    'delta_threshold': 8
}

# Key statement
final_diagnostic = compute_stability_index(health_log, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")