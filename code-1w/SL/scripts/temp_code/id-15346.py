from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation
def analyze_sensor_network(raw_logs):
    # Irrelevant preprocessing: log formatting (distractor)
    formatted_logs = [entry.strip().lower() for entry in raw_logs if entry.strip()]
    event_counter = Counter(formatted_logs)

    # Extract numeric readings from logs (actual relevant path)
    readings = []
    for log in raw_logs:
        parts = log.split(',')
        try:
            sensor_id = int(parts[0].split('-')[1])
            temp_val = float(parts[1])
            status_flag = int(parts[2])
            readings.append((sensor_id, temp_val, status_flag))
        except (IndexError, ValueError):
            continue  # Malformed log, skip

    # Filter active sensors with valid status (status_flag == 1)
    active_readings = [r for r in readings if r[2] == 1]

    # Compute baseline statistics (partially relevant)
    all_temps = [r[1] for r in readings]
    global_avg = sum(all_temps) / len(all_temps) if all_temps else 0
    high_readings = [t for t in all_temps if t > global_avg + 5]

    # Threshold map generation (red herring with complex structure)
    decoy_map = defaultdict(lambda: {'min': 0, 'max': 100, 'weight': 1.0})
    for i in range(1, 6):
        decoy_map[f'SENSOR-{i}']['threshold'] = (i * 17) % 11

    # Actual threshold logic (subtle and buried)
    threshold_map = {}
    for sid in set(r[0] for r in active_readings):
        recent_vals = [r[1] for r in active_readings if r[0] == sid][-5:]
        avg_val = sum(recent_vals) / len(recent_vals)
        # Bit manipulation obfuscation
        key_hash = (sid ^ 29) & 15
        adj_factor = (key_hash / 10.0) if key_hash > 5 else 0.5
        threshold_map[sid] = avg_val * adj_factor

    # Filtering based on dynamic criteria (critical)
    filtered_data = []
    for r in active_readings:
        sid, temp, _ = r
        if sid in threshold_map and temp > threshold_map[sid]:
            # Apply slicing to simulate windowing
            history_window = [r2[1] for r2 in readings if r2[0] == sid][-8:]
            fluctuation = max(history_window) - min(history_window)
            if fluctuation > 3.0:
                filtered_data.append(r)

    # Decoy aggregation (dead path)
    summary_stats = {}
    for r in readings:
        s_key = f'GROUP-{r[0] % 3}'
        if s_key not in summary_stats:
            summary_stats[s_key] = []
        summary_stats[s_key].append(r[1])

    # Real processing function (buried in complexity)
    def process_readings(data, thresholds):
        if not data:
            return -1
        # Character counting distraction
        code_phrase = "thermal_overload"
        bonus = len([c for c in code_phrase if c in 'aeiou'])  # 6 vowels

        # Core logic: weighted impact score
        impact_scores = []
        for entry in data:
            sensor_id, temp, _ = entry
            base_score = temp * (sensor_id & 7)  # bitwise AND
            # Conditional expression chain
            adj_score = base_score * 1.5 if temp > 40 else base_score * 0.8
            impact_scores.append(adj_score)

        # Combinatorics distraction: pairs count
        n = len(impact_scores)
        pair_count = (n * (n - 1)) // 2 if n > 1 else 0

        # Final computation (answer derivation)
        raw_total = sum(impact_scores)
        adjustment = pair_count * 0.1
        final_score = raw_total - adjustment + bonus
        return int(final_score)  # deterministic integer result

    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Misleading secondary calculation (decoy result)
    ghost_diagnostic = 0
    for k, v in summary_stats.items():
        ghost_diagnostic += len(v) * 13
    ghost_diagnostic ^= 0xFF

    return final_diagnostic

# Input data (simulated)
sensor_logs = [
    "S-3,38.2,1", "S-1,42.5,1", "S-2,35.8,0", "S-3,45.1,1",
    "S-1,39.7,1", "S-4,48.3,1", "S-2,41.0,1", "S-3,43.9,1",
    "S-1,40.2,0", "S-4,46.7,1", "S-5,37.5,1", "S-2,36.1,1",
    "S-3,47.2,1", "S-1,44.0,1", "S-5,39.8,0", "S-4,49.1,1"
]

result = analyze_sensor_network(sensor_logs)
print(f"Result: {result}")