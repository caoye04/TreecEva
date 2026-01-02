def preprocess_signal(raw_samples):
    processed = []
    noise_floor = 0.041
    gain_compensation = 1.87
    temp_accum = 0.0

    for idx, sample in enumerate(raw_samples):
        if abs(sample) < noise_floor:
            corrected = 0.0
        else:
            corrected = sample * gain_compensation + (0.002 * idx)
        
        # Distractor: irrelevant smoothing with no effect
        if idx > 0 and idx % 7 == 0:
            window = processed[-3:] if len(processed) >= 3 else [0.0]
            smoothed = sum(window) / len(window)
            temp_accum += smoothed * 0.3

        processed.append(corrected)
    
    return processed


def filter_artifacts(signal):
    cleaned = []
    artifact_flags = []

    for val in signal:
        is_artifact = (val > 10.5) or (val < -10.5)
        artifact_flags.append(is_artifact)
        
        # Distractor: unused transformation
        normalized = (val + 15.0) / 30.0 if val >= 0 else (val - 15.0) / 30.0
        capped = min(1.0, max(-1.0, val / 12.0))
        
        if not is_artifact:
            cleaned.append(val)
    
    # Dead code path — never accessed in logic
    if len(cleaned) == 0 and len(artifact_flags) > 5:
        fallback = [x for x in signal if abs(x) <= 8.0]
        cleaned.extend(fallback[:2])

    return cleaned


def compute_entropy(values):
    from math import log2
    if not values:
        return 0.0
    
    freq_map = {}
    total = len(values)
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p) if p > 0 else 0.0
    
    # Irrelevant precision tracking
    precision_shift = 1 << 4
    scaled_entropy = entropy * precision_shift
    return entropy  # scaled_entropy unused


def recursive_peak_detect(data, index=0, peaks=None):
    if peaks is None:
        peaks = []
    
    if index >= len(data):
        return peaks
    
    # Simulate complex condition with red herring
    left_val = data[index - 1] if index > 0 else data[index]
    right_val = data[index + 1] if index < len(data) - 1 else data[index]
    current = data[index]
    
    is_peak = current > left_val and current > right_val and current > 2.0
    
    # Distractor: secondary unused criterion
    is_saddle = (left_val < current < right_val) or (left_val > current > right_val)
    if is_saddle and index % 3 == 0:
        pass  # dead logic branch
    
    if is_peak:
        peaks.append(index)
    
    return recursive_peak_detect(data, index + 1, peaks)


def analyze_readings(readings, levels):
    baseline = levels.get('base', 1.0)
    sensitivity = levels.get('sens', 0.5)
    diagnostic_score = 0
    
    # Meaningful computation
    avg_reading = sum(readings) / len(readings) if readings else 0
    reading_count = len(readings)
    
    # Decoy metrics
    variance_proxy = sum((x - avg_reading) ** 2 for x in readings) / reading_count if reading_count else 0
    kurtosis_hint = sum((x - avg_reading) ** 4 for x in readings) / (reading_count * (variance_proxy ** 2)) if variance_proxy > 0 else 0
    
    # Critical branching based on thresholds
    if avg_reading > baseline * 2.5:
        diagnostic_score += 150
    elif avg_reading > baseline:
        diagnostic_score += 85
    else:
        diagnostic_score += 40
    
    # Secondary logic with zip and enumerate (required features)
    timestamps = list(range(len(readings)))
    trend_pairs = list(zip(readings, timestamps))
    upward_trend = 0
    for i, (val, ts) in enumerate(trend_pairs):
        if i > 0 and val > trend_pairs[i-1][0]:
            upward_trend += 1
    
    # Conditional expression (required feature)
    trend_modifier = 20 if upward_trend > len(trend_pairs) // 2 else -10
    diagnostic_score += trend_modifier
    
    # Add entropy contribution (real but subtle)
    rounded_vals = [round(x * 2) for x in readings]
    entropy_value = compute_entropy(rounded_vals)
    diagnostic_score += int(entropy_value * 10)
    
    # Unused recursive call (distractor)
    peak_indices = recursive_peak_detect(readings)
    if len(peak_indices) > 3:
        peak_gap_variance = sum(abs(peak_indices[j] - peak_indices[j-1]) for j in range(1, len(peak_indices)))
        # This affects nothing
    
    return diagnostic_score

# Main execution flow
if __name__ == "__main__":
    # Simulated sensor input
    raw_sensor_data = [
        0.012, -0.008, 0.45, 1.23, 2.67, 3.11, 2.89, 1.95, 0.73, -0.015,
        0.52, 1.88, 3.01, 4.12, 3.98, 2.15, 1.03, 0.67, 1.75, 2.88,
        3.05, 2.92, 1.81, 0.94, 0.22, -0.031, 0.19, 1.05, 2.20, 3.15
    ]

    # Irrelevant pre-calculations
    sample_energy = sum(x**2 for x in raw_sensor_data)
    dc_offset = sum(raw_sensor_data) / len(raw_sensor_data)
    shifted_samples = [x - dc_offset for x in raw_sensor_data]

    processed_signal = preprocess_signal(shifted_samples)
    filtered_data = filter_artifacts(processed_signal)
    
    # Real threshold config used in analysis
    threshold_levels = {"base": 1.8, "sens": 0.6}
    
    # Distractor: unused alternate configuration
    alt_configs = [
        {"base": 2.4, "sens": 0.3},
        {"base": 1.2, "sens": 0.7},
        {"base": 3.0, "sens": 0.9}
    ]
    
    # Key statement
    final_diagnostic = analyze_readings(filtered_data, threshold_levels)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")