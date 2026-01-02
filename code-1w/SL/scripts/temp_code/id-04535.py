def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Simulate multi-stage signal processing with distractions
    sample_size = len(raw_samples)
    normalized = [x / 100.0 for x in raw_samples]

    # Irrelevant statistical artifacts (distractors)
    mean_value = sum(normalized) / sample_size if sample_size else 0
    variance = sum((x - mean_value) ** 2 for x in normalized) / sample_size if sample_size else 0
    peak_magnitude = max(normalized, default=0)
    decay_constant = 0.89
    temp_buffer = [0] * sample_size

    # Real logic: detect anomalies using windowed slices
    window_size = 3
    rolling_averages = []
    for i in range(sample_size - window_size + 1):
        window = normalized[i:i+window_size]
        avg = sum(window) / window_size
        rolling_averages.append(avg)

    # Introduce decoy transformation path (never used)
    def deprecated_filter(data):
        return [x * 0.9 for x in data[::2]]

    filtered_outlier_candidates = []
    for val in rolling_averages:
        if val > threshold:
            filtered_outlier_candidates.append(val * 1.5)
        elif val < 0.1:
            filtered_outlier_candidates.append(-val)

    # Another red herring: unused complex structure
    class SignalNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    linked_peak_list = []
    for v in normalized[:5]:
        linked_peak_list.append(SignalNode(v * 2))

    # Actual relevant computation begins here
    binary_flags = [1 if x > threshold else 0 for x in rolling_averages]
    flag_transitions = 0
    for i in range(1, len(binary_flags)):
        if binary_flags[i] != binary_flags[i-1]:
            flag_transitions += 1

    # Destructuring assignment distraction
    (alpha, beta, gamma) = (1.1, 2.2, 3.3)
    metadata_tuple = ('Q4', 'diagnostic', 42)
    quarter, mode, _ = metadata_tuple

    # Core diagnostic chain
    base_score = sum(binary_flags)
    transition_penalty = flag_transitions * 0.25
    anomaly_score = base_score - transition_penalty

    # Bit manipulation decoy (irrelevant)
    masked_result = sample_size & 0xFF
    shift_offset = (masked_result << 2) ^ 0xAA

    # Real aggregation path
    aggregate_metrics = [base_score]
    aggregate_metrics.append(flag_transitions)
    aggregate_metrics.append(masked_result)  # Misleading inclusion
    aggregate_metrics.append(len(filtered_outlier_candidates))  # Red herring
    aggregate_metrics.append(anomaly_score)   # Key value embedded

    # Final scaling with slicing-based weight
    recent_metrics = aggregate_metrics[-3:]  # Slice of last three
    scaling_factor = sum(recent_metrics) / 3 if recent_metrics else 1

    # Critical statement
    final_diagnostic = aggregate_metrics[-1] + anomaly_score * scaling_factor

    # Output required result
    print(f"Result: {final_diagnostic}")

# Simulated input data
input_samples = [80, 85, 90, 60, 55, 95, 92, 40, 30, 70, 68]
analyze_signal_integrity(input_samples)