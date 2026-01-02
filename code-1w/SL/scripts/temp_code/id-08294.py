def analyze_sensor_data(raw_readings, calibration_offset=0.073):
    # Irrelevant pre-processing (distractor)
    normalized = [x * 0.98 + 2 for x in raw_readings]
    filtered = [val for val in normalized if val > 50]
    
    # Decoy transformation with no impact on final result
    temp_log = []
    cumulative_shift = 0
    for i, v in enumerate(filtered):
        shifted = v + (i * 0.01)
        cumulative_shift += shifted
n    # Unused and misleading accumulation
    decoy_accumulator = sum([filtered[j] * (j % 4 + 1) for j in range(len(filtered)) if j % 3 == 0])

    # Real computation path begins here
    base_metrics = [x - calibration_offset for x in raw_readings if x > 60]
    
    # Key data structure: multi-step transformation using zip and enumerate
    indexed_corrections = []
    for idx, val in enumerate(base_metrics):
        adjustment = (idx + 1) * 0.5 if idx % 2 == 0 else -(idx + 1) * 0.2
        indexed_corrections.append((idx, val, adjustment))

    # Destructuring and re-aggregation
    indices, values, adjustments = zip(*indexed_corrections)
    adjusted_values = [v + a for v, a in zip(values, adjustments)]

    # Accumulation with distractor conditionals
    aggregate_metrics = []
    running_total = 0
    for k, adj_val in enumerate(adjusted_values):
        if k < len(adjusted_values):  # Always true, but looks conditional
            if k % 5 != 9:  # Red herring condition (never false in this context)
                running_total += adj_val * (0.95 ** k)
        aggregate_metrics.append(running_total)

    # Dead code path - never reached due to logic above
    if len(aggregate_metrics) > 100:
        running_total *= 0.1

    # Core answer computation
    safety_margin = len(indices) * 0.111
    correction_factor = sum(adjustments) / len(adjustments) if adjustments else 0
    final_diagnostic = aggregate_metrics[-1] + correction_factor * safety_margin

    # Irrelevant secondary analysis (distraction)
    outlier_count = 0
    for reading in raw_readings:
        deviation = abs(reading - sum(raw_readings) / len(raw_readings))
        if deviation > 15:
            outlier_count += 1

    # Only this line matters for output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data with meaningful pattern
sensor_input = [62, 64, 68, 71, 59, 65, 73, 77, 60, 66, 70, 75, 63, 69, 72]
analyze_sensor_data(sensor_input)