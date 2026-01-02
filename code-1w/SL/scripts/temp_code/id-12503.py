def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize values (not used in final path)
    normalized = [x * 0.98 for x in raw_readings if x > 0]
    stats_summary = {
        'peak': max(normalized) if normalized else 0,
        'baseline': sum(normalized) / len(normalized) if normalized else 0
    }

    # Core data transformation with slicing and filtering
    shifted_window = raw_readings[3:] + raw_readings[:3]  # Circular shift
    processed = []
    for i, val in enumerate(shifted_window):
        if i % 2 == 0:
            processed.append(val ** 0.5 * calibration_factor)
        else:
            processed.append(val / (calibration_factor + 1))

    # Decoy branching: complex but unused logic
    if len(processed) > 10:
        smoothed = []
        for j in range(2, len(processed)):
            smoothed.append(sum(processed[j-2:j+1]) / 3)
        anomaly_score = sum(1 for s in smoothed if s > 50)
    else:
        anomaly_score = -1  # Dead end

    # Real signal extraction using zip and enumerate
    paired_metrics = []
    for idx, (a, b) in enumerate(zip(processed[::2], processed[1::2])):
        metric = (a + b) / 2
        adjustment = (idx % 4) * 0.1
        paired_metrics.append(metric - adjustment)

    # Filtering based on dynamic conditions
    threshold_map = {i: 15 + (i * 0.5) for i in range(len(paired_metrics))}
    filtered_data = []
    for i, m in enumerate(paired_metrics):
        if m > threshold_map[i]:
            filtered_data.append(m * 0.85)

    # Distractor: set operations with no impact
    unique_flags = set([int(f) % 7 for f in filtered_data])
    flag_combinations = set()
    for f1 in unique_flags:
        for f2 in unique_flags:
            flag_combinations.add((f1 ^ f2) % 5)

    # Final computation chain
    cumulative_weight = 0
    for i, val in enumerate(filtered_data):
        weight = 1 + (i * 0.05)
        cumulative_weight += val * weight

    # Critical statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic

def process_readings(data, thresholds):
    base = sum(data)
    penalty = 0
    for i in range(len(data)):
        if data[i] > thresholds.get(i, 999):
            penalty += data[i] * 0.1
    adjusted = base - penalty
    
    # Red herring: unused recursive helper
    def integrate_noise(level, depth):
        if depth <= 0 or level < 1:
            return 0
        return level + integrate_noise(level // 2, depth - 1)
    
    noise_injection = integrate_noise(len(data), 3)  # Always 6 for len=8
    
    # Final transformation
    result = adjusted * 0.97 + noise_injection * 0.3
    return int(result)  # Deterministic integer output

# Main execution
sensor_input = [120, 45, 98, 67, 110, 53, 88, 72, 95, 130, 44, 61]
calib = 1.2

# Entry point
result_value = analyze_sensor_array(sensor_input, calib)
print(f"Target result: {result_value}")