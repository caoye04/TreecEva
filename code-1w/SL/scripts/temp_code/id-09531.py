def analyze_sensor_data(raw_readings, config):
    baseline = sum(raw_readings) / len(raw_readings)
    adjusted_readings = [x - baseline for x in raw_readings]

    # Irrelevant transformation (dead path)
    temp_offsets = [abs(x) ** 0.5 for x in adjusted_readings if x < 0]
    ignored_correction = sum(temp_offsets) / len(temp_offsets) if temp_offsets else 0

    squared_energy = [x**2 for x in adjusted_readings]
    energy_threshold = config.get('energy_floor', 1.5)

    # Distractor: complex but unused filter
    filtered_segments = []
    segment = []
    for idx, val in enumerate(squared_energy):
        if val > energy_threshold * 1.1:
            segment.append(val)
        else:
            if len(segment) > 3:
                filtered_segments.append(segment.copy())
            segment.clear()
    # Never used again

    # Real processing begins: frequency analysis via sign transitions
    sign_changes = 0
    prev_positive = None
    for val in adjusted_readings:
        current_positive = val > 0
        if prev_positive is not None and current_positive != prev_positive:
            sign_changes += 1
        prev_positive = current_positive

    # Compute harmonic distortion proxy (relevant)
    distortion = sum(abs(x) for x in adjusted_readings if abs(x) > baseline * 0.75)

    # Bit manipulation red herring
    bit_fingerprint = 0
    for i, x in enumerate(adjusted_readings):
        shifted = int(abs(x) * 100) << (i % 5)
        bit_fingerprint ^= shifted
    decoy_hash = bin(bit_fingerprint).count('1')  # Unused

    # Real signal: compute diagnostic scores using slicing and zip
    window_size = 4
    rolling_metrics = []
    for i in range(len(adjusted_readings) - window_size + 1):
        window = adjusted_readings[i:i + window_size]
        metric = (sum(window) / window_size) * (i + 1)
        rolling_metrics.append(metric)

    # Use enumerate and zip to align with metadata indices (real use)
    index_weights = [0.8, 1.2, 0.9, 1.1] * (len(rolling_metrics) // 4 + 1)
    index_weights = index_weights[:len(rolling_metrics)]
    weighted_metrics = []
    for idx, (metric, weight) in enumerate(zip(rolling_metrics, index_weights)):
        weighted_metrics.append(metric * weight * (idx % 3 + 1))

    # Another distractor: tuple unpacking with irrelevant data
    stats_summary = []
    for i in range(0, len(weighted_metrics) - 1, 2):
        if i + 1 < len(weighted_metrics):
            first, second = weighted_metrics[i], weighted_metrics[i + 1]
            diff_sq = (first - second) ** 2
            stats_summary.append((first, second, diff_sq))  # Collected but unused

    # Core logic hidden among noise: final diagnostic depends on sign_changes and distortion
    critical_score = sign_changes * 1000 + int(distortion * 100)

    # Simulated threshold comparison chain (misleading control flow)
    debug_flags = config.get('debug_levels', [1, 2])
    mode_offset = 0
    for flag in debug_flags:
        if flag == 1:
            mode_offset += 10
        elif flag == 3:
            mode_offset += 50  # Never reached

    # Actual answer calculation buried here
    diagnostics = [critical_score, mode_offset, decoy_hash, len(filtered_segments)]
    thresholds = {'min_score': 1500, 'penalty_factor': 0.9}

    def aggregate_diagnostics(diagnostics, t):
        base = diagnostics[0]  # Only this matters
        penalty = diagnostics[1] * 0.1
        noise = (diagnostics[2] % 50) * 2
        return int(base - penalty + noise)  # Final logic

    final_diagnostic = aggregate_diagnostics(diagnostics, thresholds)

    # Dead code path: recursive traversal never called
    def traverse_tree(data, depth=0):
        if depth > 2 or not data:
            return 0
        mid = len(data) // 2
        return data[mid] + traverse_tree(data[:mid], depth + 1)

    # Print result as required
    print(f"Target result: {final_diagnostic}")

# Execute with sample input
data_stream = [3.2, -1.8, 4.5, -2.1, 0.9, -3.3, 2.7, -0.4]
settings = {'energy_floor': 1.6, 'debug_levels': [1, 2]}
analyze_sensor_data(data_stream, settings)