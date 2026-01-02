def analyze_signal(samples, baseline):
    filtered = [x for x in samples if abs(x - baseline) > 1.5]
    anomalies = set()
    for i, val in enumerate(filtered):
        if i > 0 and val > filtered[i-1]:
            anomalies.add(val)
    return sorted(anomalies, reverse=True)


def compute_envelope(amplitude, phase):
    # Irrelevant computation - dead path
    envelope = []
    for a, p in zip(amplitude, phase):
        envelope.append(a * (1 + 0.5 * (p % 2)))
    smoothed = [envelope[0]]
    for e in envelope[1:]:
        smoothed.append(0.7 * smoothed[-1] + 0.3 * e)
    return smoothed


def generate_sequence(n):
    # Distractor function - not used in final result
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def extract_features(raw_data):
    segments = raw_data[::2]  # slicing every other element
    segment_set = set(segments)
    noise_floor = sum(segment_set) / len(segment_set)
    peaks = [x for x in segment_set if x > noise_floor + 2]
    return peaks, noise_floor


def aggregate_metrics(data_stream, criteria):
    base_values = [x for x in data_stream if x in criteria]
    if not base_values:
        return -1
    mean_val = sum(base_values) / len(base_values)
    deviation = [abs(b - mean_val) for b in base_values]
    dev_set = set(deviation)
    upper_dev = sum(1 for d in dev_set if d > 0.75)
    lower_dev = sum(1 for d in dev_set if d <= 0.75)
    adjustment_factor = (upper_dev - lower_dev) * 0.1
    return round(mean_val + adjustment_factor, 6)

# Main execution with distractors
sensor_readings = [3.2, 1.8, 4.5, 2.1, 3.6, 4.9, 2.7, 3.3, 4.1, 5.2, 2.4, 3.0]
baseline_ref = 3.0

# Irrelevant transformation chain
transformed = compute_envelope([int(x) for x in sensor_readings], list(range(len(sensor_readings))))
processed_transform = transformed[1::2]  # slicing operation - red herring

# Critical data path
anomaly_list = analyze_signal(sensor_readings, baseline_ref)
trend_data = [x + 0.1 for x in anomaly_list if x > 2.5]

# Set operations as core logic component
divergence_pool = {round(x * 1.1, 1) for x in sensor_readings}
threshold_set = {3.5, 4.0, 4.5, 5.0, 5.5}
common_modes = divergence_pool & threshold_set  # intersection - relevant

# Dead code block - misleading control flow
if len(common_modes) > 10:
    fallback = generate_sequence(10)
    trend_data.extend(fallback)
elif len(common_modes) == 3:
    temp_adjust = sum(common_modes) / 3
    trend_data = [t + temp_adjust for t in trend_data]
else:
    # This branch runs, but contains irrelevant min/max usage
    peak, trough = max(trend_data), min(trend_data)
    spread = peak - trough
    dummy_correction = min(spread, 1.5)

# Key assignment using multiple concepts
interim_snapshot = extract_features(trend_data)
feature_peaks, floor_level = interim_snapshot

# Final computation point
final_diagnostic = aggregate_metrics(trend_data, threshold_set)

# Output requirement
print(f"Result: {final_diagnostic}")