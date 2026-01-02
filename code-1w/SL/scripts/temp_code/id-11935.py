def analyze_sensor_data(raw_readings, threshold=0.75):
    # Simulate preprocessing: normalize and filter anomalies
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [val for val in normalized if val > 0.1]

    # Irrelevant transformation: frequency domain mock (dead logic)
    dummy_fft = [abs((i - len(filtered)//2)) for i in range(len(filtered))]
    peak_frequency = len(dummy_fft) // 4  # Misleading value

    # Core metric: compute rolling window variance (signal stability)
    window_size = 3
    stability_scores = []
    for i in range(len(filtered) - window_size + 1):
        window = filtered[i:i+window_size]
        mean_val = sum(window) / window_size
        variance = sum((x - mean_val)**2 for x in window) / window_size
        stability_scores.append(variance)

    # Distractor: unused recursive function for entropy (never called)
    def calculate_entropy(data, base=2):
        from math import log
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        return -sum((count/len(data)) * log(count/len(data), base) for count in freq.values())

    # Unused path: hypothetical phase shift analysis
    phase_shifts = []
    for j in range(1, len(stability_scores)):
        delta = stability_scores[j] - stability_scores[j-1]
        if delta > 0.01:
            phase_shifts.append(j)

    # Real processing: detect significant drops in signal magnitude
    magnitude_drops = 0
    for k in range(1, len(normalized)):
        if normalized[k] < normalized[k-1] * 0.5 and normalized[k] < threshold:
            magnitude_drops += 1

    # Compute risk score based on drop frequency and instability
    instability_index = sum(1 for s in stability_scores if s > 0.02)
    risk_score = magnitude_drops * 3 + instability_index

    # Decoy metrics: look important but unused
    avg_normalized = sum(normalized) / len(normalized)
    peak_value = max(normalized)
    decay_rate = (normalized[-1] - normalized[0]) / len(normalized) if len(normalized) > 1 else 0

    # Aggregate metrics with red herring components
    aggregate_metrics = [
        len(phase_shifts) * 2,
        int(avg_normalized * 100),
        instability_index ** 2,
        risk_score + peak_frequency,  # includes misleading peak_frequency
        magnitude_drops * len(stability_scores)
    ]

    # Critical distraction: multiple similar correction factors
    temp_correction = 1.5
    base_correction = 2.0
    correction_factor = 3.0  # Only this one is used
    fallback_correction = 4.0

    # Safety margin derived from obscure condition
    reference_point = normalized[0] if len(normalized) > 0 else 0.5
    safety_margin = 10 if reference_point < 0.3 else 7

    # UNUSED: alternate logic branches (dead code)
    if risk_score > 20:
        backup_adjustment = 5
        secondary_scale = 1.2
    elif instability_index > 5:
        backup_adjustment = 3
        secondary_scale = 0.8

    final_diagnostic = aggregate_metrics[-1] + correction_factor * safety_margin
    return final_diagnostic

# Execute with fixed input
sensor_input = [120, 115, 90, 25, 20, 180, 175, 160, 30, 28, 27, 400, 390]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")