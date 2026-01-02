def analyze_system_metrics(data_points):
    temp_cache = []
    checksum = 0
    for entry in data_points:
        if isinstance(entry, str) and 'err' in entry.lower():
            continue
        if isinstance(entry, (int, float)):
            checksum += entry * 0.1
    
    processed = [x for x in data_points if isinstance(x, (int, float))]
    if len(processed) < 3:
        return 0

    # Irrelevant transformation
    inverted_map = {i: 1/(x + 1) for i, x in enumerate(processed) if x != -1}
    normalization_factor = sum(inverted_map.values()) or 1

    # Distractor: complex but unused structure
    decoy_matrix = [[i * j for j in range(3)] for i in range(3)]
    for row in decoy_matrix:
        row.append(sum(row))

    # Actual relevant path starts here
    base_rating = sum(processed) / len(processed)
    variance = sum((x - base_rating) ** 2 for x in processed) / len(processed)
    efficiency_index = base_rating / (variance + 1)

    # Simulated log accumulation (uses string method)
    efficiency_log = ''
    steps = ['init', 'calibrate', 'stabilize', 'optimize']
    for step in steps:
        efficiency_log += f'{step}:{efficiency_index:.2f}|'
    efficiency_log = efficiency_log.strip('|')

    # Dead code path - never called
    def legacy_recalibrate(log):
        return len(log) % 7

    # Another red herring: modifies a variable not used later
    temp_threshold = 0
    for i in range(len(processed)):
        if i % 2 == 0:
            temp_threshold ^= processed[i]

    # Critical function definition
    def calculate_thermal_rating(log_str):
        segments = log_str.split('|')
        values = []
        for segment in segments:
            if ':' in segment:
                key, val = segment.split(':', 1)
                if val.replace('.', '').isdigit():
                    values.append(float(val))
        # Only the last three values are used
        relevant_vals = values[-3:]
        weighted_sum = sum(v * (i+1) for i, v in enumerate(relevant_vals))
        adjustment = len(log_str.split('|')) * 0.5
        return int(weighted_sum * adjustment) + 13

    # Key assignment
    thermal_capacity = calculate_thermal_rating(efficiency_log)

    # Unused cleanup
    temp_cache.clear()
    normalization_factor = None

    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Input data with mixed types and distractions
data_snapshot = [12.5, 8.3, 'status_ok', 15.1, 'debug_err_404', 7.9, 11.0]

result = analyze_system_metrics(data_snapshot)