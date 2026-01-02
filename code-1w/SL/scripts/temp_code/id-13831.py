def sensor_calibrate(data):
    calibrated = []
    offset = 0.1
    for val in data:
        if val < 0:
            val = abs(val) + offset
        calibrated.append(round(val * 1.05, 4))
    return [c for c in calibrated if c > 0.5]


def filter_anomalies(logs):
    anomalies = []
    for i, log in enumerate(logs):
        if i == 0:
            continue
        if abs(log - logs[i-1]) > 2.0:
            anomalies.append(i)
    removal_indices = set(anomalies)
    filtered = [log for i, log in enumerate(logs) if i not in removal_indices]
    return filtered


def accumulate_trend(values):
    trend_sum = 0.0
    for v in values:
        trend_sum += v * 0.9
    return round(trend_sum, 4)


def evaluate_thresholds(seq):
    high_count = 0
    low_count = 0
    for s in seq:
        if s > 3.0:
            high_count += 1
        elif s < 1.0:
            low_count += 1
    ratio = high_count / (low_count + 1)
    return ratio > 1.5


def generate_synthetic_baseline(n):
    # Irrelevant function: generates unused baseline data
    base = []
    x = 1.0
    for i in range(n):
        x = (x * 1.7) % 4.0
        base.append(round(x, 3))
    return base


def normalize_sequence(seq):
    if not seq:
        return []
    m = min(seq)
    mx = max(seq)
    if mx == m:
        return [0.0 for _ in seq]
    return [(s - m) / (mx - m) for s in seq]


def extract_peaks_and_troughs(series):
    peaks = []
    troughs = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            peaks.append(i)
        if series[i] < series[i-1] and series[i] < series[i+1]:
            troughs.append(i)
    return peaks, troughs


def aggregate_metrics(peaks, troughs, raw):
    p_score = len(peaks) * 1.5
    t_score = len(troughs) * 0.7
    base_impact = sum(raw[:len(raw)//2]) if raw else 0
    total = p_score - t_score + (base_impact * 0.1)
    return round(total, 4)


def analyze_readings(logs):
    if not logs:
        return 0.0
    
    # Step 1: Normalize the logs
    normalized = normalize_sequence(logs)
    
    # Step 2: Find peaks and troughs
    peaks, troughs = extract_peaks_and_troughs(normalized)
    
    # Step 3: Compute aggregate metric
    metric_value = aggregate_metrics(peaks, troughs, logs)
    
    # Step 4: Evaluate threshold behavior (boolean flag, distractor)
    threshold_flag = evaluate_thresholds(logs)
    
    # Step 5: Accumulate trend score
    trend_value = accumulate_trend(normalized)
    
    # Step 6: Combine into diagnostic score
    raw_diagnostic = metric_value * 0.6 + trend_value * 0.4
    
    # Irrelevant intermediate calculation (distractor)
    synthetic_data = generate_synthetic_baseline(len(logs))
    comparison_diff = 0.0
    for a, b in zip(normalized, synthetic_data[:len(normalized)]):
        comparison_diff += abs(a - b)
    
    # Unused recursive-like structure (dead path)
    def recurse_noise(level, acc):
        if level <= 0:
            return acc
        return recurse_noise(level - 1, acc + level * 0.01)
    noise_floor = recurse_noise(5, 0.0)  # Computed but not used
    
    # Final computation path
    adjustment = 1.0
    if len(peaks) > len(troughs):
        adjustment = 1.2
    elif len(troughs) > len(peaks):
        adjustment = 0.8
    
    final_diagnostic = round(raw_diagnostic * adjustment, 4)
    
    # Additional red herring variables
    outlier_ratio = len(peaks) / (len(logs) + 1)
    stability_index = (len(peaks) + len(troughs)) / len(logs) if logs else 0
    
    return final_diagnostic

# Main execution sequence
raw_sensor_data = [2.1, 1.8, 3.2, 0.9, 1.1, 3.4, 2.9, 3.5, 1.0, 0.8]

# Irrelevant preprocessing (distractor)
adjusted_data = [x * 1.02 for x in raw_sensor_data]
sorted_data = sorted(adjusted_data)
duplicate_check = list(set(sorted_data))

# Relevant processing pipeline
processed_logs = sensor_calibrate(raw_sensor_data)
processed_logs = filter_anomalies(processed_logs)

# Key statement
final_diagnostic = analyze_readings(processed_logs)

print(f"Result: {final_diagnostic}")