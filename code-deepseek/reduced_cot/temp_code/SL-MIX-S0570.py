def compute_system_adjustment(measurements, thresholds):
    # Initialize tracking variables (some are distractors)
    baseline_offset = 42
    temp_variance = 0
    cumulative_error = 0
    
    # Process measurements with set operations
    valid_measurements = set(measurements)
    threshold_range = range(thresholds['min'], thresholds['max'] + 1)
    
    # Distractor: irrelevant calculation
    max_possible = max(measurements) * 2 - min(measurements)
    
    # Main logic: filter and process valid measurements
    filtered_vals = []
    for idx, val in enumerate(measurements):
        if val in threshold_range:
            filtered_vals.append(val)
            cumulative_error += (val - baseline_offset) * 0.5  # Distractor
        else:
            temp_variance += val  # Dead code path
    
    # Secondary processing with tuple operations
    if filtered_vals:
        value_pairs = list(zip(filtered_vals, filtered_vals[1:]))
        adjustments = []
        for pair in value_pairs:
            adjustment = (pair[0] + pair[1]) // 2
            adjustments.append(adjustment)
            
        # Calculate final adjustment with early termination
        if len(adjustments) >= 3:
            core_adjustment = sum(adjustments[:3]) - adjustments[2]
        else:
            core_adjustment = sum(adjustments) - baseline_offset
            
        # Final computation (this is the relevant path)
        valid_count = len(valid_measurements & set(threshold_range))
        final_value = core_adjustment + valid_count * 7
        return final_value
    else:
        return baseline_offset  # Unused branch

# Main execution
measurements = [45, 52, 38, 61, 47, 55, 42, 58]
thresholds = {'min': 40, 'max': 60}

# Additional distractor variables
system_load = sum(measurements) // len(measurements)
calibration_offset = system_load * 3 - 100

# Key computation
final_calibration = compute_system_adjustment(measurements, thresholds)

# More distractors
backup_calibration = final_calibration + calibration_offset
secondary_check = backup_calibration % 13

print(f"Target result: {final_calibration}")