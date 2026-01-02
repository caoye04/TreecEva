import math

# Simulated environmental sensor data processing pipeline
def analyze_readings(raw_data):
    # Core signal extraction (relevant)
    filtered_signals = [x for x in raw_data if 10 < x < 95]
    baseline_shift = sum(filtered_signals) / len(filtered_signals) if filtered_signals else 0

    # Irrelevant noise profile analysis (distractor)
    noise_peaks = []
    for val in raw_data:
        if val > 100 or val < 5:
            noise_peaks.append(val)
    peak_variance = (sum((x - sum(noise_peaks)/len(noise_peaks))**2 for x in noise_peaks) / len(noise_peaks)) if noise_peaks else 0

    # Data normalization chain (partially relevant)
    normalized = list(map(lambda x: (x - baseline_shift) * 0.87, filtered_signals))
    
    # Decoy statistical analysis (dead path)
    def compute_entropy(data):
        from collections import Counter
        counts = Counter(data)
        total = len(data)
        return -sum((count/total) * math.log2(count/total) for count in counts.values())
    entropy_value = compute_entropy([int(x) for x in raw_data[:10]]) if len(raw_data) >= 10 else 0.0

    # Critical transformation sequence (core logic)
    windowed_sums = []
    for i in range(0, len(normalized) - 2, 3):
        windowed_sums.append(sum(normalized[i:i+3]))

    # Advanced filtering with set operations (relevant)
    unique_windows = list(set(windowed_sums))
    valid_segments = {i for i, w in enumerate(unique_windows) if w > 15.0}

    # Misleading intermediate metric (red herring)
    coherence_index = 0.0
    if len(unique_windows) > 1:
        coherence_index = abs(unique_windows[-1] - unique_windows[0]) / max(unique_windows)

    # Key computational branch
    adjustment_set = {1, 3, 5, 7}
    scaling_factor = 1.0
    if valid_segments & adjustment_set:
        scaling_factor = 1.75
    elif len(valid_segments) > 4:
        scaling_factor = 0.95
    else:
        scaling_factor = 1.2

    # Composite aggregation with distractor influence
    aggregate_result = 0
    temp_cache = {}
    for idx, segment in enumerate(unique_windows):
        if idx % 2 == 0:
            temp_cache[idx] = segment * scaling_factor
            aggregate_result += temp_cache[idx]
        else:
            # Unused computation (distractor)
            squared_contrib = segment ** 2
            normalized_contrib = math.sqrt(squared_contrib + 1e-6)

    # Final correction using trigonometric decoy function (irrelevant but plausible)
    def temporal_correction(hour):
        return 0.98 + 0.02 * math.cos(math.pi * hour / 12)
    time_influence = temporal_correction(14)  # Hardcoded time

    # Critical assignment point
    correction_factor = 1.0
    if baseline_shift > 40:
        correction_factor = 1.15
    else:
        correction_factor = 0.85

    filtration_score = aggregate_result * correction_factor

    # Dead code path (unused result)
    final_report = {
        'status': 'processed',
        'segments_analyzed': len(windowed_sums),
        'noise_ratio': len(noise_peaks) / len(raw_data),
        'score_debug': aggregate_result  # Not used
    }

    return filtration_score

# Simulated input data
sensor_input = [12, 45, 67, 34, 89, 23, 56, 78, 91, 11, 43, 66, 29, 73, 84, 18]

result = analyze_readings(sensor_input)
print(f"Result: {result}")