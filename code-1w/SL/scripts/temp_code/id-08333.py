import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_data():
    raw_readings = [i * 0.5 + (i % 7) for i in range(120)]
    timestamps = list(range(len(raw_readings)))
    metadata = {'version': '2.1', 'calibrated': True}
    return list(zip(timestamps, raw_readings))


def filter_noise(data, threshold=15.0):
    filtered = []
    noise_log = []  # distractor: collected but not used later
    for t, val in data:
        if abs(val) > threshold:
            noise_log.append((t, val))
        else:
            filtered.append((t, val))
    return filtered


def segment_signal(data, window_size=10):
    segments = []
    for i in range(0, len(data), window_size):
        segment = data[i:i + window_size]
        if len(segment) == window_size:
            segments.append([val for _, val in segment])
    return segments


def enhance_resolution(segments):
    enhanced = []
    avg_magnitudes = []  # distractor: calculated but not directly used
    for seg in segments:
        magnitude = sum(abs(x) for x in seg)
        avg_magnitudes.append(magnitude / len(seg))
        upsampled = []
        for x in seg:
            upsampled.extend([x * 0.9, x * 1.1])  # simulate interpolation
        enhanced.append(upsampled)
    scaling_factor = sum(avg_magnitudes) / len(avg_magnitudes) if avg_magnitudes else 1.0
    return enhanced, scaling_factor


def compute_entropy(segment):
    # Simple entropy approximation based on value distribution
    counts = {}
    for x in segment:
        rounded = round(x, 1)
        counts[rounded] = counts.get(rounded, 0) + 1
    total = len(segment)
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    return entropy


def detect_anomalies(segments):
    anomalies = []
    baseline = 0
    for i, seg in enumerate(segments):
        mean_val = sum(seg) / len(seg)
        baseline += mean_val
    baseline /= len(segments) if segments else 1
    
    for i, seg in enumerate(segments):
        variance = sum((x - baseline) ** 2 for x in seg) / len(seg)
        if variance > 25.0:  # arbitrary threshold
            anomalies.append(i)
    return anomalies if anomalies else [0]  # ensure non-empty


def calculate_checksum(data_list):
    # Irrelevant utility function — red herring
    checksum = 0
    for item in data_list:
        if isinstance(item, (list, tuple)):
            for x in item:
                checksum ^= int(abs(x * 100)) % 256
        else:
            checksum ^= int(abs(item * 100)) % 256
    return checksum


def temporal_correlation(segments):
    # Distractor function: looks important but unused in final path
    if len(segments) < 2:
        return 0.0
    first_avg = sum(segments[0]) / len(segments[0])
    last_avg = sum(segments[-1]) / len(segments[-1])
    return (last_avg - first_avg) ** 2


def analyze_signal(segments):
    entropies = [compute_entropy(seg) for seg in segments]
    anomaly_indices = detect_anomalies(segments)
    primary_weight = len(anomaly_indices)
    secondary_weight = 0
    for i, entropy in enumerate(entropies):
        if i in anomaly_indices:
            secondary_weight += int(entropy * 10)
    
    # Key computation path
    base_score = sum(entropies) * 100
    adjustment = primary_weight * secondary_weight
    final_diagnostic = int(base_score) - adjustment
    
    # Dead code path — misleading
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        flag_recovered = True
    
    return final_diagnostic

# Main execution flow
raw_data = collect_sensor_data()
filtered_data = filter_noise(raw_data)
segmented = segment_signal(filtered_data)
enhanced_segments, scale = enhance_resolution(segmented)

# Unused transformations — red herrings
decimated = [seg[::2] for seg in enhanced_segments]  # every other sample
dithered = [[x + (-1)**i * 0.05 for i, x in enumerate(seg)] for seg in decimated]
checksum_value = calculate_checksum(dithered)  # computed but ignored
correlation_metric = temporal_correlation([seg for seg in segmented])  # unused

# Critical statement
final_diagnostic = analyze_signal(processed_segments=enhanced_segments)

print(f"Result: {final_diagnostic}")