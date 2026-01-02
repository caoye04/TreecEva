def analyze_signal_strength(readings):
    # Irrelevant transformation: normalize values (not used in final path)
    normalized = [r / max(readings) for r in readings]
    smoothed = list(map(lambda x: round(x, 2), normalized))

    # Distractor: frequency analysis with dead-end logic
    freq_count = {}
    for val in readings:
        freq_count[val] = freq_count.get(val, 0) + 1
    dominant_peak = max(freq_count, key=freq_count.get) if freq_count else 0

    # Real computation begins: filter anomalies using median threshold
    sorted_vals = sorted(readings)
    mid = len(sorted_vals) // 2
    median_val = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    
    # Extract high-confidence samples above median + 15%
    variance_offset = sum(abs(r - median_val) for r in readings) / len(readings)
    cutoff = median_val + 0.15 * variance_offset
    
    # Distractor: attempt clustering (unused)
    clusters = {'low': [], 'high': []}
    for r in readings:
        clusters['high'].append(r) if r > cutoff else clusters['low'].append(r)
    cluster_size_ratio = len(clusters['high']) / len(clusters['low']) if clusters['low'] else 0

    # Core signal: compute weighted importance of high-tier readings
    high_readings = [r for r in readings if r >= cutoff]
    weights = [1 + (r - median_val) / median_val for r in high_readings]
    weighted_sum = sum(w * v for w, v in zip(weights, high_readings))
    base_magnitude = weighted_sum / len(high_readings) if high_readings else 0

    # Secondary adjustment: dynamic scaling based on distribution skew
    deviations = [r - median_val for r in readings]
    signed_skew = sum(d ** 3 for d in deviations) / (len(deviations) * (variance_offset + 1e-6) ** 3)
    adjustment_factor = 0.1 if abs(signed_skew) < 0.5 else 0.25

    # Tertiary red herring: simulate fallback calibration (never triggers due to logic)
    fallback_mode = False
    calibration_table = {i: base_magnitude * (0.9 + i*0.05) for i in range(5)}
    if len(high_readings) < 3 and variance_offset > 10:
        fallback_mode = True  # Dead code path: condition never met

    # Final aggregation chain
    aggregate_metric = base_magnitude * (1 + adjustment_factor)
    outlier_suppression = sum(1 for r in readings if r > 2 * median_val)
    suppression_penalty = 0.05 * outlier_suppression
    final_tally = aggregate_metric * (1 - suppression_penalty)

    # Key statement — target of the question
    threshold_score = final_tally * (1 + adjustment_factor)

    # Print result as required
    print(f"Result: {threshold_score}")
    return threshold_score

# Simulated sensor input (deterministic)
data_stream = [23, 45, 45, 67, 89, 89, 89, 101, 112, 120, 95, 73]

# Entry point
analyze_signal_strength(data_stream)