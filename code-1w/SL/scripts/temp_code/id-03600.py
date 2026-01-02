from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def preprocess_sensor_readings(raw_readings):
    processed = []
    for val in raw_readings:
        if val < -100 or val > 100:
            continue  # Invalid readings
        processed.append(abs(val) * 0.9 + 5)
    return processed

# Irrelevant helper (red herring)
def compute_entropy(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Signal filter that removes noise below variance threshold
def filter_anomalies(dataset, window_size=3):
    if len(dataset) < window_size:
        return dataset[:]
    smoothed = []
    for i in range(len(dataset)):
        start = max(0, i - window_size // 2)
        end = min(len(dataset), i + window_size // 2 + 1)
        window = dataset[start:end]
        mean_val = sum(window) / len(window)
        variance = sum((x - mean_val) ** 2 for x in window) / len(window)
        if variance >= 1.5 or i % 5 == 0:  # Keep high-variance or periodic samples
            smoothed.append(round(mean_val, 2))
    return smoothed

# Unused decoy function (dead code path)
def legacy_calibration(data):
    adjusted = [x * 0.98 + 1.2 for x in data]
    return [max(0, x) for x in adjusted]

# Core analysis logic — key function
def build_threshold_map(metrics, base_offset=3.14):
    mapping = defaultdict(float)
    sorted_keys = sorted(metrics.keys())
    for idx, k in enumerate(sorted_keys):
        factor = math.cos(idx * 0.5)
        mapping[k] = metrics[k] * factor + base_offset
    return mapping

# Signal analyzer using complex conditional logic
def analyze_signal(signal_sequence, thresholds):
    if not signal_sequence:
        return 0
    
    # Distractor variables
    temp_buffer = [math.tanh(x) for x in signal_sequence if x > 4]
    spike_count = sum(1 for x in signal_sequence if x > 7.5)
    rolling_avg = sum(signal_sequence[-5:]) / min(5, len(signal_sequence))
    
    # Critical logic path
    score_accum = 0.0
    for i, val in enumerate(signal_sequence):
        key = f"seg_{i // 4}"
        thresh = thresholds.get(key, 2.0)
        if val > thresh * 2.1 and i % 3 != 0:
            score_accum += math.log(val + 1) * 0.7
        elif val > thresh and i % 2 == 0:
            score_accum += 0.3
    
    # Secondary adjustment based on distribution
    quartile_75 = sorted(signal_sequence)[len(signal_sequence) * 3 // 4]
    if quartile_75 > 6.0:
        score_accum *= 1.25
    
    return int(score_accum * 100) / 100.0

# --- Main execution ---
if __name__ == "__main__":
    # Raw sensor input (simulated)
    raw_sensor_data = [
        -150, 12, 45, 67, 23, 89, 34, 12, 5, 67, 89, 101, 45, 23, 67, 89, 90, 12, 45, 67
    ]
    
    # Step 1: Preprocess valid readings
    cleaned_data = preprocess_sensor_readings(raw_sensor_data)
    
    # Distractor computation (irrelevant to final result)
    entropy_value = compute_entropy([int(x) for x in cleaned_data])
    normalized_data = [x / max(cleaned_data) for x in cleaned_data]
    
    # Step 2: Filter anomalies using sliding window
    filtered_data = filter_anomalies(cleaned_data)
    
    # Fake calibration call (unused path)
    calibrated_copy = legacy_calibration(filtered_data)  # Not used
    
    # Step 3: Construct dynamic threshold map from statistical segments
    segment_stats = {}
    for i in range(0, len(filtered_data), 4):
        segment = filtered_data[i:i+4]
        if segment:
            avg_seg = sum(segment) / len(segment)
            segment_stats[f"seg_{i//4}"] = avg_seg
    
    # Create threshold mapping
    threshold_map = build_threshold_map(segment_stats)
    
    # Introduce more red herrings
    outlier_flags = [x for x in filtered_data if x > 8]
    compression_ratio = len(filtered_data) / len(cleaned_data) if cleaned_data else 0
    
    # Key statement: final diagnostic analysis
    final_diagnostic = analyze_signal(filtered_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")