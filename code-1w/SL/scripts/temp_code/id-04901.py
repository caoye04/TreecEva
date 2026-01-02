def analyze_sensor_data(raw_readings, thresholds):
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100) for x in raw_readings]
    
    # Irrelevant transformation: frequency analysis (not used later)
    freq_analysis = {}
    for val in raw_readings:
        freq_analysis[val] = freq_analysis.get(val, 0) + 1
    spectral_peak = max(freq_analysis, key=freq_analysis.get)

    # Distractor: unused conditional path
    if len(raw_readings) > 50:
        rolling_avg = [sum(raw_readings[i:i+5])/5 for i in range(len(raw_readings)-4)]
    else:
        magnitude_profile = [abs(raw_readings[i] - raw_readings[i-1]) for i in range(1, len(raw_readings))]
        spike_count = sum(1 for m in magnitude_profile if m > 3 * sum(magnitude_profile)/len(magnitude_profile))

    # Real computation begins: categorize readings
    categories = []
    for nr in normalized:
        if nr < thresholds[0]:
            categories.append('low')
        elif nr < thresholds[1]:
            categories.append('moderate')
        else:
            categories.append('high')
    
    # Misleading intermediate: entropy calculation (unused)
    from math import log2
    cat_freq = {c: categories.count(c) for c in set(categories)}
    entropy = -sum((count / len(categories)) * log2(count / len(categories)) for count in cat_freq.values())
    
    # Critical data transformation chain
    encoded = [0 if c == 'low' else 1 if c == 'moderate' else 2 for c in categories]
    deltas = [encoded[i] - encoded[i-1] for i in range(1, len(encoded))]
    trend_score = sum(deltas) * len([d for d in deltas if d > 0])
    
    # Decoy function call with red herring result
    def calculate_robustness_index(seq):
        return sum(abs(seq[i] - seq[i-2]) for i in range(2, len(seq))) // (len(seq) + 1)
    
    robustness = calculate_robustness_index(normalized)  # Not used
    
    # Key processing with list comprehension and zip
    baseline_shift = [normalized[i] - normalized[i-1] for i in range(1, len(normalized))]
    paired_analysis = list(zip(baseline_shift, encoded[1:]))
    response_curve = [shift * weight for shift, weight in paired_analysis]
    
    # Another distraction: character counting in synthetic labels
    state_labels = ['S_' + c[0].upper() for c in categories]
    total_chars = sum(len(label) for label in state_labels)  # Unused
    
    # Core metric accumulation (uses enumerate)
    aggregate_metrics = []
    for i, val in enumerate(response_curve):
        if i % 3 == 0:
            aggregate_metrics.append(val * 2)
        elif i % 3 == 1:
            aggregate_metrics.append(val + trend_score // 10)
        else:
            aggregate_metrics.append(abs(val - entropy * 2))
    
    # Final correction based on system calibration (red herring variables above are distractions)
    calibration_log = [1.2, 0.8, 1.5, 0.9, 1.1]
    correction_factor = int(sum(calibration_log) / len(calibration_log))
    
    # CRITICAL STATEMENT
    final_diagnostic = aggregate_metrics[-1] + correction_factor
    
    # Output required
    print(f"Result: {final_diagnostic}")

# Execution with deterministic input
data_stream = [23, 45, 67, 89, 12, 34, 56, 78, 91, 11, 22, 33, 44, 55, 66]
config_thresholds = [30, 70]
analyze_sensor_data(data_stream, config_thresholds)