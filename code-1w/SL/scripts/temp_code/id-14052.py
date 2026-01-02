from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation
def analyze_sensor_network():
    raw_readings = [
        (101, 23.4, 'temp'), (102, 45.1, 'pressure'), (103, 23.4, 'temp'),
        (104, 18.9, 'humidity'), (105, 45.1, 'pressure'), (106, 23.4, 'temp'),
        (107, 52.3, 'pressure'), (108, 18.9, 'humidity'), (109, 23.4, 'temp'),
        (110, 41.0, 'pressure'), (111, 18.9, 'humidity'), (112, 23.4, 'temp')
    ]

    # Irrelevant mapping - distractor
    status_codes = {200: 'OK', 404: 'Not Found', 500: 'Server Error'}
    lookup_table = [[i * j for j in range(5)] for i in range(5)]  # Unused computation

    # Filter relevant sensors (only temp and humidity)
    filtered_data = [r for r in raw_readings if r[2] in ['temp', 'humidity']]

    # Decoy statistical summary
    pressure_values = [r[1] for r in raw_readings if r[2] == 'pressure']
    avg_pressure = sum(pressure_values) / len(pressure_values) if pressure_values else 0
    variance_pressure = sum((x - avg_pressure) ** 2 for x in pressure_values) / len(pressure_values)

    # Build threshold map (only temp has dynamic threshold)
    base_thresholds = {'temp': 20.0, 'humidity': 15.0}
    threshold_map = defaultdict(float)
    for key, val in base_thresholds.items():
        threshold_map[key] = val + (5.0 if key == 'temp' else 0)

    # Red herring: complex frequency analysis on sensor IDs
    sensor_id_counter = Counter(r[0] for r in raw_readings)
    frequent_ids = {k for k, v in sensor_id_counter.items() if v > 1}
    id_correlation_matrix = {(i, j): abs(i - j) for i in frequent_ids for j in frequent_ids if i != j}

    # Real logic: count how many readings exceed thresholds
    exceeded = defaultdict(int)
    for sid, value, stype in filtered_data:
        if value > threshold_map[stype]:
            exceeded[stype] += 1

    # Dead code path - never executed due to prior filtering
    def compute_flow_rate(pressure, temp):
        return (pressure * 100) / (temp + 273.15)  # Kelvin conversion

    flow_rates = []
    for r in raw_readings:
        if r[2] == 'pressure':
            # Would need temperature co-location, which we don't have
            pass  # Simulate complex missing data logic

    # Secondary distraction: string-based event tagging
    events = []
    for r in filtered_data:
        label = f"sensor_{r[0]}_event"
        tokens = label.split('_')
        events.append((int(tokens[1]), tokens[2], r[2]))

    event_summary = Counter(e[2] for e in events)

    # Core diagnostic function
    def process_readings(data, thresholds):
        counts = defaultdict(int)
        type_values = defaultdict(list)

        # Group values by type
        for _, val, t in data:
            type_values[t].append(val)

        # Compute mean for each type
        means = {t: sum(vals) / len(vals) for t, vals in type_values.items() if vals}

        # Count outliers
        for _, val, t in data:
            if val > thresholds[t]:
                counts[t] += 1

        # Apply weighting formula: weighted anomaly score
        total_anomalies = 0
        weights = {'temp': 2, 'humidity': 3}
        for t, cnt in counts.items():
            expected = len(type_values[t]) * 0.25  # 25% baseline
            excess = max(0, cnt - expected)
            total_anomalies += excess * weights.get(t, 1)

        # Complex adjustment based on mean deviation
        adjustment = 0
        ref_mean = means.get('temp', 0)
        if ref_mean > 22.0:
            adjustment += 2
        if means.get('humidity', 0) > 17.0:
            adjustment += 1

        return int(total_anomalies * 10 + adjustment * 5)

    # Misleading intermediate result
    dummy_diagnostic = len(frequent_ids) * 7 + len(lookup_table)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output required format
    print(f"Result: {final_diagnostic}")

    # Never reached - dead code
    cleanup_buffer = [0] * 100
    del cleanup_buffer

    return final_diagnostic

analyze_sensor_network()