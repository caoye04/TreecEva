def analyze_signal(samples, threshold=0.75):
    # Irrelevant preprocessing block (dead path)
    if len(samples) < 10:
        return -1
    temp_cache = {}
    for idx, val in enumerate(samples):
        temp_cache[idx] = val ** 2 + 0.1

    # Real processing begins: filter significant peaks
    filtered_peaks = []
    for i in range(1, len(samples) - 1):
        if samples[i] > samples[i-1] and samples[i] > samples[i+1] and samples[i] > threshold:
            filtered_peaks.append(samples[i])

    # Distractor: unused transformation
    shifted_spectrum = [x * 1.03 for x in samples]
    normalized = [x / sum(samples) for x in samples]  # Not used later

    # Critical feature engineering
    engineered_features = []
    for j, peak in enumerate(filtered_peaks):
        if j % 2 == 0:
            engineered_features.append(peak * 128)
        else:
            engineered_features.append(int(peak * 256))

    # Bit manipulation red herring
    decoy_state = 0
    for x in engineered_features:
        decoy_state ^= x & 255
        decoy_state += decoy_state << 1
        decoy_state &= 0xFFFF

    # Baseline offset computed from index patterns
    indices = list(range(len(filtered_peaks)))
    paired = list(zip(indices, filtered_peaks))
    baseline_offset = 0
    for index, value in paired:
        baseline_offset += index * int(value * 10)

    # Accumulation via summation with conditional modulation
    accumulator = 0
    modulation_factor = 1.5
    for k, feat in enumerate(engineered_features):
        if k < baseline_offset % 7:
            accumulator += feat * modulation_factor
        else:
            accumulator -= feat // 4

    # Fake aggregation function (never called)
    def dummy_aggregate(data):
        return sum(x ^ 17 for x in data) * 2

    # Real aggregation logic
    def aggregate_metrics(features, offset):
        result = offset
        for f in features:
            result += f % 19
            result = (result * 7) % 98765
        return int(result)

    # Unused recursive distraction
    def trace_path(node_id, depth):
        if depth <= 0 or node_id <= 1:
            return 1
        return trace_path(node_id - 2, depth - 1) + trace_path(node_id - 1, depth - 1)

    # Final computation
    final_diagnostic = aggregate_metrics(engineered_features, baseline_offset)
    print(f"Target result: {final_diagnostic}")

# Simulated sensor input (deterministic)
signal_data = [0.1, 0.82, 0.3, 0.85, 0.2, 0.91, 0.15, 0.88, 0.4]
analyze_signal(signal_data)