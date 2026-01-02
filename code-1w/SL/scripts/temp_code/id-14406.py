def process_sensor_array():
    # Simulated environmental sensor readings (temperature, humidity, pressure)
    raw_readings = [
        (23.5, 45.2, 1013.25), (24.1, 47.8, 1012.90), (19.8, 60.1, 1014.05),
        (22.0, 55.0, 1013.80), (35.2, 30.5, 1010.10), (20.1, 58.9, 1013.95),
        (21.8, 50.0, 1013.40), (25.0, 40.0, 1012.00), (18.9, 65.3, 1015.10)
    ]

    # Irrelevant transformation: convert to strings for logging (dead end)
    string_logs = [f'T:{t} H:{h} P:{p}' for t, h, p in raw_readings]
    debug_snapshot = string_logs[::2]  # Unused snapshot

    # Thresholds for anomaly detection (real logic begins)
    threshold_map = {
        'temp_high': 30.0,
        'temp_low': 20.0,
        'humidity_high': 60.0,
        'pressure_stable_range': (1012.0, 1014.5)
    }

    # Distractor: complex unused statistical calculation
    avg_temp = sum(r[0] for r in raw_readings) / len(raw_readings)
    variance_proxy = sum((r[0] - avg_temp) ** 2 for r in raw_readings)
    entropy_like_metric = -(sum((v / 9) * (v / 9) for v in range(9)))  # Fake info theory

    # Real filtering: isolate potentially faulty sensors
    filtered_data = []
    for idx, (t, h, p) in enumerate(raw_readings):
        if t > threshold_map['temp_high'] or h > threshold_map['humidity_high']:
            filtered_data.append((idx, t, h, p))

    # Red herring: unused data structure transformation
    indexed_pairs = list(enumerate(zip([r[1] for r in raw_readings], [r[2] for r in raw_readings])))
    set_operations_test = set(range(len(raw_readings))) - {1, 3, 7}  # Not used later

    # Core analysis function (depends on filtered_data and threshold_map)
    def analyze_readings(anomalies, thresholds):
        severity_score = 0
        pressure_warnings = 0

        for entry in anomalies:
            _, t, h, p = entry
            if t > thresholds['temp_high']:
                severity_score += 3
            if h > thresholds['humidity_high']:
                severity_score += 2
            if not (thresholds['pressure_stable_range'][0] <= p <= thresholds['pressure_stable_range'][1]):
                pressure_warnings += 1

        # Real answer computation
        base_diagnostic = severity_score * 100
        adjustment = pressure_warnings * 50
        final_diagnostic = base_diagnostic + adjustment

        # Distractor: irrelevant slicing and enumeration
        slices = [anomalies[i:i+2] for i in range(0, len(anomalies), 2)]
        for i, s in enumerate(slices):
            _ = i * len(s)  # No effect

        return final_diagnostic

    # Execution point of interest
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")

    # Dead code path: never executed
    def deprecated_analysis():
        return sum(1 for x in [1, 2, 3] if x > 1) * 1000

    return final_diagnostic

# Execute and capture result
def main():
    result = process_sensor_array()
    return result

main()