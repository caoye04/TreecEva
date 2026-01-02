from collections import defaultdict, Counter

# Simulated sensor network data with metadata
def collect_diagnostics():
    raw_readings = [
        (102, 'temp', 'sensor_a'), (150, 'pressure', 'sensor_b'),
        (205, 'temp', 'sensor_c'), (98, 'temp', 'sensor_a'),
        (300, 'pressure', 'sensor_b'), (198, 'temp', 'sensor_c'),
        (400, 'flow', 'sensor_x'), (250, 'pressure', 'sensor_b')
    ]

    # Irrelevant aggregation: distractor using enumerate and zip
    indices = list(enumerate([r[0] for r in raw_readings if r[1] == 'temp']))
    temp_values = [v for v, _, _ in raw_readings if v > 100 and 'sensor_' in _]
    paired = list(zip(indices, temp_values))  # Dead computation

    # Misleading transformation chain
    temp_stats = defaultdict(lambda: {'sum': 0, 'count': 0})
    pressure_caps = {k: 250 for k in ['sensor_b']}
    flow_mask = [0.9, 0.85]  # Unused in logic

    for value, reading_type, sensor_id in raw_readings:
        if reading_type == 'temp':
            temp_stats[sensor_id]['sum'] += value
            temp_stats[sensor_id]['count'] += 1

    avg_temps = {sid: data['sum'] / data['count'] for sid, data in temp_stats.items()}

    # Decoy function that's defined but not used
    def analyze_trend(seq, weight=1.1):
        return sum(x * weight for x in seq) % 100

    # Threshold map for validation (used later)
    threshold_map = {
        'temp': {s: 190 for s in ['sensor_a', 'sensor_c']},
        'pressure': {'sensor_b': 275}
    }

    # Filter relevant high-value pressure readings
    filtered_data = []
    spike_count = 0
    for val, typ, sid in raw_readings:
        if typ == 'pressure' and sid == 'sensor_b':
            if val > 200:
                spike_count += 1
            if val > 150:
                filtered_data.append((val, typ, sid))

    # Secondary filtering based on temporal pattern (simulated order)
    ordered_pairs = sorted(filtered_data, key=lambda x: x[0])
    if len(ordered_pairs) > 3:
        ordered_pairs = ordered_pairs[-3:]  # Keep last three highest

    # Actual processing function with embedded logic
    def process_readings(data, thresholds):
        result_set = []
        type_groups = defaultdict(list)

        # Group by type and sensor
        for v, t, s in data:
            type_groups[t].append((v, s))

        for typ, records in type_groups.items():
            for val, sensor in records:
                base_threshold = thresholds.get(typ, {}).get(sensor, 0)
                if val > base_threshold:
                    # Complex conditional expression
                    penalty = 5 if val > base_threshold + 50 else 2
                    adjusted = val - penalty
                    result_set.append(adjusted)

        # Use of Counter as final aggregation
        counts = Counter(result_set)
        total = sum(counts.values())
        magnitude = sum(k * v for k, v in counts.items())
        return magnitude // total if total else 0

    # Red herring: unused statistical smoothing
    smoothed = [round(avg_temps[s] * 0.95) for s in avg_temps if 'sensor_' in s]
    status_codes = {s: 200 if v < 200 else 400 for s, v in avg_temps.items()}

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return to prevent external interference
    return final_diagnostic

# Execute
collect_diagnostics()