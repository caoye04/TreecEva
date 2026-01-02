def analyze_system_metrics(data_log):
    base_rating = 0
    efficiency_factor = 1.0
    temp_offset = 0
    calibration_sequence = [x for x in data_log if x > 0]
    
    # Irrelevant string processing (distractor)
    status_flags = ['OK', 'ERROR', 'WARNING']
    system_status = ','.join(status_flags).upper().replace(',', '|')
    temp_flag = system_status.lower().count('k')

    # Real computation begins
    for entry in calibration_sequence:
        if entry % 2 == 0:
            base_rating += entry ** 0.5
        else:
            base_rating -= entry // 3

    # Secondary loop with partial relevance
    adjustment_accumulator = 0
    for i in range(len(calibration_sequence)):
        if i % 3 == 0:
            adjustment_accumulator += len(str(calibration_sequence[i]))
        # Dead code path (misleading)
        if i > 1000:
            adjustment_accumulator *= 0.9

    efficiency_factor = adjustment_accumulator / (len(calibration_sequence) or 1)

    # Tertiary distractor: slicing and string ops with no impact
    log_snippet = data_log[2:8:2]
    reversed_hex = ''.join([hex(n)[2:] for n in log_snippet])[::-1]
    hex_sum_check = sum([int(c, 16) for c in reversed_hex if c in '0123456789abcdef'])

    # Key function call embedded in logic
    def adjust_thermal_rating(rating, factor):
        intermediate = rating * factor
        # Extra step to increase nesting and cognitive load
        if intermediate < 0:
            intermediate = abs(intermediate) + 2
        return int(intermediate) + 5

    thermal_capacity = adjust_thermal_rating(base_rating, efficiency_factor)
    
    # Additional irrelevant state tracking
    metadata_cache = {}
    for idx, val in enumerate(data_log):
        metadata_cache[f"entry_{idx}"] = val * 0.01

    # Final result output
    print(f"Result: {thermal_capacity}")

# Input data
input_log = [16, 3, 25, 7, 36, 11, 49, 13]
analyze_system_metrics(input_log)