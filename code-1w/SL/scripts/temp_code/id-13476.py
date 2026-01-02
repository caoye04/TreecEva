def analyze_signal(samples, threshold=12.5):
    # Irrelevant preprocessing block (distractor)
    normalized = [round(x / max(samples) * 100, 2) for x in samples]
    filtered = [x for x in normalized if x > 10]
    histogram = {i: sum(1 for x in filtered if i*10 <= x < (i+1)*10) for i in range(1, 11)}

    # Core computation path (relevant)
    raw_magnitude = sum(abs(x) for x in samples)
    peak_count = len([x for x in samples if abs(x) > threshold])
    average_power = raw_magnitude / len(samples) if samples else 0

    # Secondary analysis with red herring
    anomalies = []
    for i, x in enumerate(samples):
        if i > 0 and abs(x - samples[i-1]) > 15:
            anomalies.append(i)
    spike_rate = len(anomalies) / len(samples) if samples else 0

    # Decoy function that's never called
    def compute_entropy(data):
        from math import log
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        total = len(data)
        return -sum((count/total) * log(count/total) for count in freq.values())

    # Destructuring assignment (relevant)
    first_quartile, median_val, third_quartile = sorted(samples)[::len(samples)//4][:3] if len(samples) >= 4 else (0,0,0)

    # Bit manipulation red herring
    checksum = 0
    for x in samples[:5]:
        shifted = int(abs(x)) << 2
        checksum ^= shifted & 0xFF

    # Conditional expression with actual relevance
    signal_class = 'strong' if average_power > 8 else 'weak'
    weight_factor = 1.75 if signal_class == 'strong' else 0.9

    # Set operations (required feature) - partially relevant
    unique_samples = set(samples)
    outlier_set = {x for x in unique_samples if abs(x) > 3 * average_power}
    valid_set = unique_samples - outlier_set

    # Actual core calculation chain starts here
    base_metric = sum(valid_set) / len(valid_set) if valid_set else 0
    fluctuation_index = third_quartile - first_quartile
    aggregate_measure = base_metric * fluctuation_index

    # Slicing operation (required feature) - relevant
    history_window = samples[-8:-1] if len(samples) > 8 else samples
    temporal_bias = sum(history_window[-3:]) / len(history_window[-3:]) if history_window else 0

    # Correction logic with conditional expression
    correction_factor = 1.0 if len(outlier_set) < 4 else 0.85
    offset_value = 5 if len(history_window) % 2 == 1 else -3

    # Key statement containing the answer
    final_diagnostic = aggregate_measure * correction_factor + offset_value

    # Dead code path (distractor)
    if False:
        backup_system = [x for x in samples if x < 0]
        recovery_state = sum(backup_system) >> 2

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
sensor_readings = [3.2, -7.1, 15.6, 8.9, -2.4, 18.3, 6.7, 4.1, 11.0, -5.8, 9.4]
analyze_signal(sensor_readings)