import math

# Simulated sensor network diagnostics with noise filtering and anomaly detection
def collect_diagnostics():
    raw_readings = [127, 255, 64, 89, 191, 32, 45, 110, 73, 200]
    calibration_offset = 17
    scaling_factor = 0.88
    noise_floor = 30
    temp_buffer = []
    processed = []
    
    for val in raw_readings:
        adjusted = (val + calibration_offset) * scaling_factor
        if adjusted > noise_floor:
            processed.append(int(adjusted))
    
    # Irrelevant transformation chain (dead path)
    inverted_map = [255 - x for x in raw_readings]
    squared_norms = [x**2 for x in inverted_map]
    avg_inverted = sum(inverted_map) / len(inverted_map)
    deviation_score = sum(abs(x - avg_inverted) for x in inverted_map)

    # Core logic: filter based on dynamic criteria
    high_freq_peaks = [x for x in processed if x > 100]
    low_freq_peaks = [x for x in processed if x <= 100]
    peak_variance = sum((x - sum(processed)/len(processed))**2 for x in processed) / len(processed)
    entropy_estimate = -sum((x/sum(processed)) * math.log(x/sum(processed)) for x in processed if x > 0)

    # Distractor: unused statistical bundle
    stats_bundle = {
        'range': max(processed) - min(processed),
        'skew': (3 * (sum(processed)/len(processed) - statistics.median(processed))) / math.sqrt(peak_variance) if 'statistics' in globals() else 0,
        'kurtosis_hint': len([x for x in processed if x > 150])
    }

    # Set-based interference: irrelevant diagnostic modes
    active_modes = {'thermal', 'vibration', 'acoustic', 'pressure'}
    failed_sensors = {'current', 'vibration'}
    operational = active_modes - failed_sensors
    diagnostic_flags = {mode[0] for mode in operational}
    
    # Real signal path begins here
    baseline_ref = 95
    threshold_set = {x for x in range(baseline_ref - 10, baseline_ref + 15)}
    filtered_data = [x for x in processed if x in threshold_set]

    # Decoy recursive function (never called in critical path)
    def trace_anomaly(path, depth):
        if depth == 0:
            return path
        return trace_anomaly(path + [(depth, 'null')], depth - 1)

    # Key analysis function with embedded logic chain
    def analyze_readings(data, thresholds):
        if not data:
            return 0
            
        # Step 1: count occurrences within extended threshold margin
        extended_bounds = {t + 5 for t in thresholds}
        enriched_count = sum(1 for x in data if x + 5 in extended_bounds)
        
        # Step 2: compute weighted impact score
        weights = [1.5 if x > 100 else 0.7 for x in data]
        impact_score = sum(x * w for x, w in zip(data, weights))
        
        # Step 3: apply decay factor based on sequence position
        decayed = [data[i] / (i + 1) for i in range(len(data)) if i < 4]
        decay_sum = sum(decayed)
        
        # Step 4: boolean logic cascade
        is_stable = len(data) >= 3 and impact_score < 300
        has_spike = any(x > max(thresholds) for x in data)
        requires_attention = not is_stable or has_spike
        
        # Step 5: set interaction effect
        mirror_set = {abs(200 - t) for t in thresholds}
        overlap = len(threshold_set & mirror_set)
        
        # Step 6: composite calculation
        base = impact_score * 0.1
        adjustment = (decay_sum * overlap) / (1 + requires_attention)
        intermediate = base + adjustment
        
        # Step 7: final nonlinear transformation
        normalized = intermediate / (entropy_estimate + 1)
        
        # Step 8: rounding to nearest integer under condition
        final_value = int(normalized) if normalized > 50 else round(normalized, 2)
        
        return final_value

    # Execution point of interest
    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    
    # Red herring: unrelated time-series mockup
    timeline = [{'t': i, 'val': x} for i, x in enumerate(raw_readings)]
    cumulative = 0
    for entry in timeline:
        cumulative += entry['val']
        entry['cum'] = cumulative
    
    # Final output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Unused helper that adds distraction
def generate_synthetic(count):
    return [((i * 137) % 256) for i in range(count)]

# Execute main logic
collect_diagnostics()