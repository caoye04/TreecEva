from itertools import compress, count

# Simulate sensor data quality assessment with noise filtering
def analyze_sensor_array(raw_readings, thresholds):
    base_weights = [1.1, 0.9, 1.0, 1.2, 0.8]
    adjusted_readings = [r * w for r, w in zip(raw_readings, base_weights)]
    
    # Misleading normalization (not used in final logic)
    total_adjusted = sum(adjusted_readings)
    normalized = [val / total_adjusted for val in adjusted_readings]  # Dead weight

    # Determine valid sensors based on dynamic threshold
    activity_flags = [reading > thresh for reading, thresh in zip(raw_readings, thresholds)]
    
    # Use itertools.compress to extract active sensor readings
    active_readings = list(compress(adjusted_readings, activity_flags))
    
    # Secondary filter: only keep readings above local mean
    if active_readings:
        mean_active = sum(active_readings) / len(active_readings)
        variance_proxy = sum((x - mean_active) ** 2 for x in active_readings) / len(active_readings)
        consistency_mask = [abs(x - mean_active) <= variance_proxy for x in active_readings]
        refined_readings = list(compress(active_readings, consistency_mask))
    else:
        refined_readings = []

    # Compute diagnostic metrics (some are red herrings)
    peak_value = max(refined_readings) if refined_readings else 0
    stability_index = len(refined_readings) / len(raw_readings) if raw_readings else 0
    entropy_approx = 0.0
    if refined_readings:
        entropy_approx = sum(-x * math.log(x + 1e-9) for x in normalized)  # Uses normalized, not relevant

    # Key metric pipeline
    trend_scores = []
    counter = count(1)
    for val in refined_readings:
        score = val * next(counter)
        if score > 5:  # Arbitrary heuristic
            trend_scores.append(int(score) ^ 3)  # Bitwise twist

    # Filtering final metrics below adaptive floor
    avg_trend = sum(trend_scores) / len(trend_scores) if trend_scores else 10
    filtered_metrics = [s for s in trend_scores if s >= avg_trend * 0.75]

    # ———— Critical Statement ————
    threshold_score = max(filtered_metrics) if filtered_metrics else 0
    
    # Irrelevant post-processing
    checksum = sum(threshold_score.to_bytes(4, 'little')) & 0xFF
    final_report = {'score': threshold_score, 'valid': checksum > 0}
    
    print(f"Result: {threshold_score}")
    return final_report

import math

# Input data
sensor_inputs = [12, 8, 15, 6, 10]
threshold_levels = [10, 7, 14, 5, 9]

# Execute
result = analyze_sensor_array(sensor_inputs, threshold_levels)