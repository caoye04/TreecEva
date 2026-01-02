def analyze_sensor_array(raw_readings, threshold, calibration_factor=1.05):
    # Irrelevant pre-processing: Normalize data (unused path)
    normalized = [round(x * 0.98, 3) for x in raw_readings if x > 0]
    temp_log = {idx: val for idx, val in enumerate(normalized)}  # Distractor dictionary

    # Core logic: filter valid sensor readings above threshold
    filtered_data = []
    outlier_count = 0
    for i, reading in enumerate(raw_readings):
        if reading < 0:
            continue
        adjusted = reading * calibration_factor
        if adjusted > threshold:
            if adjusted % 1 == 0 and adjusted > 100:  # Artificial constraint
                adjusted = adjusted ** 0.5  # Distraction: rarely applies
            filtered_data.append(adjusted)
        else:
            outlier_count += 1  # Misleading counter

    # Dead code path: simulated redundancy check (never used)
    def validate_redundancy(arr):
        return all(a <= b for a, b in zip(arr, arr[1:]))

    sorted_diagnostics = sorted(filtered_data, reverse=True)
    peak_metrics = {f'p{i}': v for i, v in enumerate(sorted_diagnostics)}  # Unused diagnostic map

    # Real transformation: apply damping on high-frequency components
    damped = []
    for idx, val in enumerate(filtered_data):
        if idx % 3 == 0:
            damped.append(val * 0.87)
        elif idx % 3 == 1:
            damped.append(val * 0.93)
        else:
            damped.append(val)

    # Secondary filter: remove values below dynamic floor
    dynamic_floor = sum(damped) / len(damped) * 0.65 if damped else 0
    refined = [x for x in damped if x >= dynamic_floor]

    # Final aggregation using weighted harmonic mean (key computation)
    if not refined:
        return 0.0
    
    total_weight = 0
    weight_sum = 0
    for i, val in enumerate(refined):
        weight = 1 / (i + 1)  # Decreasing importance
        total_weight += weight / val
        weight_sum += weight
    
    if total_weight == 0:
        return 0
        
    harmonic_base = weight_sum / total_weight
    
    # Final nonlinear calibration step
    final_diagnostic = int(harmonic_base * 1.08) if harmonic_base < 50 else int(harmonic_base * 1.02)
    
    # Red herring: update unused tracking structure
    summary_report = {
        'count': len(refined),
        'floor': round(dynamic_floor, 4),
        'calibration_used': calibration_factor,
        'damped_length': len(damped)
    }
    
    # Output target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate input data
sensor_input = [89, -5, 102, 45, 111, 73, 198, 67, -12, 134, 88, 95]
threshold_limit = 90
scale_factor = 1.05

# Execute main analysis
result = analyze_sensor_array(sensor_input, threshold_limit, scale_factor)