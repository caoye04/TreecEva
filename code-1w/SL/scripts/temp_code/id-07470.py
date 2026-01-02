def analyze_signal(samples, threshold=0.7):
    # Irrelevant constants and decoy variables
    calibration_offset = 0.041
    noise_floor = [0.1, 0.05, 0.2, 0.3]
    gain_factor = 1.8
    baseline_correction = sum(noise_floor) * calibration_offset

    # Distractor: complex-looking but unused signal transformation
    transformed = []
    for x in samples:
        if x > threshold:
            transformed.append((x ** 2) * gain_factor)
        else:
            transformed.append(x / (1 + x))

    # Real processing begins: filter and normalize
    filtered = [s for s in samples if s > threshold]
    normalized = [round(s / max(filtered), 3) for s in filtered] if filtered else [0]

    # Bit manipulation red herring
    checksum = 0
    for val in normalized:
        shifted = int(val * 1000)
        checksum ^= (shifted << 2) & 0xFF
        checksum += len(str(shifted))

    # Decoy data structure with misleading aggregation
    stats = {
        'peak': max(normalized, default=0),
        'avg': sum(normalized) / len(normalized) if normalized else 0,
        'variance': sum((x - sum(normalized)/len(normalized))**2 for x in normalized) / len(normalized) if normalized else 0
    }

    # Unused recursive function to increase distraction
    def recursive_decay(n, factor=0.9):
        if n <= 1:
            return n
        return factor * recursive_decay(n - 1, factor)

    # Actual relevant logic: count and slice
    processed_count = len(normalized)
    sample_window = normalized[-3:]  # Last three valid samples

    # Create fake patterns with slicing misdirection
    mirror_pattern = sample_window[::-1]
    paired_diffs = [a - b for a, b in zip(sample_window, mirror_pattern)]

    # Real metric: count how many normalized values are above median
    sorted_vals = sorted(normalized)
    mid = len(sorted_vals) // 2
    median_val = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    high_band_count = sum(1 for x in normalized if x > median_val)

    # Another decoy: attempt sorting but not used in final result
    frequency_map = {}
    for v in normalized:
        frequency_map[v] = frequency_map.get(v, 0) + 1
    sorted_by_freq = sorted(frequency_map.keys(), key=lambda k: (-frequency_map[k], k))

    # Key computation path: build aggregate_metrics using specific rules
    aggregate_metrics = []
    for i in range(7):
        if i % 3 == 0:
            metric = (stats['peak'] * 1000) + i
        elif i == high_band_count:
            metric = processed_count * 100 + checksum % 10
        else:
            metric = int(stats['avg'] * 100) ^ i  # XOR for bit-level distraction
        aggregate_metrics.append(int(metric))

    # Dead code path - looks important but unused
    if processed_count > 5:
        temp_result = []
        for j in range(processed_count):
            temp_result.append((j * stats['variance']) // (1 + baseline_correction))

    # Critical assignment - this is where the answer comes from
    final_diagnostic = aggregate_metrics[processed_count % 7]

    # Print required output
    print(f"Result: {final_diagnostic}")

# Execute with realistic input
data_stream = [0.81, 0.92, 0.68, 0.94, 0.75, 0.88, 0.91, 0.63]
analyze_signal(data_stream)