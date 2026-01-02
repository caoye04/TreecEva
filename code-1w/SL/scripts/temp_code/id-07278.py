def analyze_system_stability(readings, thresholds):
    cumulative_shift = 0
    volatility_index = 0
    transient_peaks = []
    baseline_adjustment = sum(thresholds) / len(thresholds)
    
    for i, (value, limit) in enumerate(zip(readings, thresholds)):
        deviation = value - limit
        if deviation > 0:
            volatility_index += 1
            transient_peaks.append((i, deviation))
        cumulative_shift += abs(deviation)
    
    # Distractor: irrelevant frequency analysis
    frequency_map = {}
    for val in readings:
        frequency_map[val] = frequency_map.get(val, 0) + 1
    dominant_frequency = max(frequency_map.values(), default=0)
    
    # Distractor: unused transformation
    transformed_readings = [x * 0.95 + 2.1 for x in readings]
    smoothed_avg = sum(transformed_readings) / len(transformed_readings)
    
    # Core logic begins
    peak_count = len(transient_peaks)
    stability_factor = 0
    if peak_count == 0:
        stability_factor = 100
    elif peak_count <= 3:
        stability_factor = 50
    else:
        stability_factor = 10

    # Secondary computation chain
    adjustment_ratio = baseline_adjustment / (volatility_index + 1)
    weighted_deviation = cumulative_shift * adjustment_ratio
    
    # Tertiary path: conditional expression with distractor variables
    status_flag = 'STABLE' if stability_factor > 40 else 'UNSTABLE'
    debug_trace = [status_flag, smoothed_avg, dominant_frequency]
    
    # Key computation path
    intermediate_score = weighted_deviation + stability_factor
    final_tally = int(intermediate_score)
    equilibrium_score = final_tally // 2
    
    # Redundant state logging (irrelevant to result)
    log_entry = f"System {status_flag}: score={equilibrium_score}"
    temp_buffer = [f"Index {t[0]}: +{t[1]:.1f}" for t in transient_peaks]
    
    # Output required result
    print(f"Result: {equilibrium_score}")

# Inputs
sensor_data = [85, 90, 95, 88, 105]
threshold_levels = [80, 88, 90, 92, 100]

# Execution
analyze_system_stability(sensor_data, threshold_levels)