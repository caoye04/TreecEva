from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly scoring
def analyze_readings(raw_data):
    readings_count = defaultdict(int)
    anomalies = []
    temp_sum = 0
    valid_sensors = set()

    for entry in raw_data:
        sensor_id = entry['sensor']
        value = entry['value']
        timestamp = entry['time']

        readings_count[sensor_id] += 1
        temp_sum += value

        # Irrelevant filtering based on arbitrary time condition
        if timestamp % 10 == 0:
            pass  # Dead code: doesn't affect outcome

        # Actual anomaly detection logic
        if value < -10 or value > 90:
            anomalies.append((sensor_id, value))

        if 5 <= value <= 85:
            valid_sensors.add(sensor_id)

    avg_value = temp_sum / len(raw_data) if raw_data else 0

    # Misleading intermediate calculation (not used later)
    outlier_ratio = len(anomalies) / len(raw_data) if raw_data else 0

    return readings_count, anomalies, avg_value, valid_sensors


def calculate_stability_score(anomaly_list, total_entries):
    # Complex but partially irrelevant scoring
    score = 100.0
    severity = 0

    for sensor, val in anomaly_list:
        if val < -10:
            severity += 3
        elif val > 90:
            severity += 2

    # Early termination based on threshold
    if severity > 10:
        return 20.0

    deduction = severity * 5
    score -= deduction

    # Extra computation that looks important but isn't final
    normalized = max(score, 0)
    return normalized


def calculate_final_score(data, thresholds):
    counts, anomalies, average, valid_set = analyze_readings(data)

    base_score = calculate_stability_score(anomalies, len(data))

    # Secondary adjustment using counter
    sensor_usage = Counter([d['sensor'] for d in data])
    high_freq_sensors = [s for s, c in sensor_usage.items() if c > thresholds['usage_threshold']]

    # Bonus logic with distractor variables
    bonus_applied = False
    debug_info = []
    temp_buffer = []

    for record in data:
        if record['sensor'] in high_freq_sensors and record['value'] > 75:
            temp_buffer.append(record)  # Collected but not used

    # Only sensors in both high-frequency and above threshold contribute
    bonus = len(high_freq_sensors) * 3 if average > thresholds['average_threshold'] else 0
    if bonus > 0:
        bonus_applied = True
        debug_info.append('Bonus condition met')  # Logging, not affecting logic

    final_score = base_score + bonus

    # Red herring: complex-looking normalization (never applied)
    if final_score > 100:
        final_score = 100

    return int(final_score)

# Main execution
if __name__ == '__main__':
    # Input data - deterministic sensor logs
    sensor_data = [
        {'sensor': 'S1', 'value': 95, 'time': 10},
        {'sensor': 'S1', 'value': 80, 'time': 11},
        {'sensor': 'S2', 'value': -12, 'time': 12},
        {'sensor': 'S2', 'value': 70, 'time': 13},
        {'sensor': 'S3', 'value': 98, 'time': 14},
        {'sensor': 'S3', 'value': 75, 'time': 15},
        {'sensor': 'S4', 'value': 82, 'time': 16},
        {'sensor': 'S4', 'value': 88, 'time': 17},
        {'sensor': 'S5', 'value': 20, 'time': 18},
        {'sensor': 'S5', 'value': 30, 'time': 19}
    ]

    config = {
        'usage_threshold': 1,
        'average_threshold': 60.0
    }

    # Key statement
    final_score = calculate_final_score(sensor_data, config)
    
    print(f"Result: {final_score}")