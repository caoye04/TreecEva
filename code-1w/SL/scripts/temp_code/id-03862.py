def analyze_sensor_data(raw_stream, threshold=0.75):
    # Simulate preprocessing of sensor input (irrelevant filtering)
    filtered_data = [x for x in raw_stream if abs(x) > 0.1]
    normalized = [val / max(filtered_data) for val in filtered_data if max(filtered_data) != 0]

    # Irrelevant auxiliary computation (distractor)
    peak_magnitude = max(normalized, default=0)
    spike_count = sum(1 for x in normalized if x > threshold)
    decay_rate = 0.95
    damping_sequence = [peak_magnitude * (decay_rate ** i) for i in range(5)]

    # Real signal segmentation using slicing
    window_size = 4
    segmented = [normalized[i:i+window_size] for i in range(0, len(normalized), window_size)]
    truncated_segments = [seg[:3] for seg in segmented if len(seg) == 4]  # Use only full windows

    # Extract features with enumerate and zip (core relevant logic)
    feature_vector = []
    for idx, segment in enumerate(segmented):
        if len(segment) >= 3:
            index_offset = idx * 0.01
            avg_val = sum(segment) / len(segment)
            weighted_index = idx * segment[2] + index_offset
            feature_vector.append((avg_val, weighted_index))

    # Secondary transformation chain (partially relevant)
    transposed = list(zip(*[seg for seg in segmented if len(seg) >= 3]))  # Use zip across segments
    column_averages = [sum(col) / len(col) for col in transposed] if transposed else [0]

    # Decoy statistical analysis (dead path)
    median_doubled = 2 * sorted(column_averages)[len(column_averages)//2] if column_averages else 0
    entropy_approx = 0
    for c in column_averages:
        if c > 0: entropy_approx -= c * c

    # Core calculation path begins here
    base_metric = sum(column_averages) * len(feature_vector)
    adjustment = 0
    for i, (avg, weight) in enumerate(feature_vector):
        adjustment += avg * (weight % 1) * (-1)**i

    aggregate_score = base_metric + adjustment

    # Red herring: unused recursive function
    def calculate_depth(n):
        return 1 + calculate_depth(n-1) if n > 0 else 0

    # Another distraction: irrelevant bit manipulation
    bitmask = 0b101010
    masked_values = [i ^ bitmask for i in range(len(normalized)) if i % 3 == 0]

    # Final diagnostics (target assignment)
    correction_factor = 1.03
    offset_value = -2.15
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Output result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data (deterministic seed)
sensor_input = [0.12, 0.35, 0.88, 0.73, 0.05, 0.91, 0.67, 0.44, 0.29, 0.77]
analyze_sensor_data(sensor_input)