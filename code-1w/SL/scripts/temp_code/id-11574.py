from itertools import compress, count

def analyze_system_performance():
    # Simulated sensor readings (real data)
    base_readings = [2.1, -1.3, 4.5, 0.0, -3.2, 6.7, -5.4, 3.3, 1.8, -0.9]
    
    # Irrelevant auxiliary data (distractor)
    calibration_offsets = [0.1, -0.2, 0.3, -0.1, 0.0, 0.4, -0.3, 0.2, 0.1, -0.4]
    temp_buffer = [x * 1.05 for x in calibration_offsets]
    scaling_factor = 1.0  # Unused in final logic
    
    # Apply meaningless transformation (dead path)
    processed_offsets = []
    for i, val in enumerate(calibration_offsets):
        if val > 0:
            processed_offsets.append(val ** 2)
        else:
            processed_offsets.append(abs(val))

    # Core logic begins: generate thresholds using enumeration
    enumerated_readings = list(enumerate(base_readings))
    threshold_map = []
    for idx, value in enumerated_readings:
        dynamic_threshold = 2.0 if idx % 2 == 0 else 1.5
        adjusted_val = abs(value) - 0.5
        meets_criteria = adjusted_val > dynamic_threshold
        threshold_map.append(meets_criteria)
    
    # Secondary filter based on bit patterns (bit manipulation red herring)
    index_flags = []
    for i in range(len(base_readings)):
        binary_state = bin(i + 3)[2:]  # Shift to avoid trivial cases
        ones_count = binary_state.count('1')
        parity_flag = ones_count % 2 == 1
        index_flags.append(parity_flag)
    
    # Combine filters (only one is actually used later)
    combined_mask = [a and b for a, b in zip(threshold_map, index_flags)]
    primary_mask = [abs(x) > 2.0 for x in base_readings]  # This is the real filter

    # Generate metrics with conditional expressions (core)
    raw_metrics = []
    for val in base_readings:
        metric = val ** 2 if val >= 0 else -(val ** 1.5)
        raw_metrics.append(round(metric, 3))
    
    # Filtering process (key step)
    filtered_metrics = []
    for i in range(len(raw_metrics)):
        if primary_mask[i]:  # Only this mask matters
            filtered_metrics.append(raw_metrics[i])
        else:
            # Dead assignment (misleading)
            dummy_var = raw_metrics[i] * 0.1
    
    # Decoy aggregation function (never called)
    def compute_aggregate(data, mode='standard'):
        if mode == 'weighted':
            return sum(x * 1.1 for x in data)
        return sum(x * 0.9 for x in data)
    
    # Final computation (answer point)
    filtration_score = sum(filtered_metrics)
    
    # Unused branching (distraction)
    if len(filtered_metrics) > 5:
        backup_result = max(filtered_metrics) - min(filtered_metrics)
    else:
        backup_result = len([x for x in filtered_metrics if x < 0])
    
    # Output result
    print(f"Result: {filtration_score}")
    return filtration_score

# Execute
analyze_system_performance()