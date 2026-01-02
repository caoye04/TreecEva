def sensor_network_analysis():
    raw_readings = [145, 256, 98, 412, 333, 199, 521, 304]
    calibration_factor = 0.97
    adjustment_matrix = [1.02, 0.98, 1.01, 0.99, 1.03]
    baseline_offset = 23
    temp_buffer = [0] * 5
    
    # Irrelevant temperature simulation (dead path)
    for i in range(len(temp_buffer)):
        temp_buffer[i] = (i * 17 + 4) % 103
    
    # Actual signal processing begins
    filtered_readings = []
    for val in raw_readings:
        adjusted = val * calibration_factor + baseline_offset
        if adjusted > 100 and adjusted < 500:
            filtered_readings.append(int(adjusted))
    
    # Decoy statistical analysis (distractor)
    mean_guess = sum(filtered_readings[:3]) / 3
    variance_clue = (mean_guess - filtered_readings[0]) ** 2
    entropy_approx = 0
    for x in filtered_readings:
        if x > 0:
            entropy_approx += x * len(str(x))
    
    # Real data transformation using lambda
    processed_data = list(map(lambda x: (x >> 2) ^ 15, filtered_readings))
    
    # Set operations as red herring
    unique_shifts = set()
    shift_frequencies = {}
    for x in processed_data:
        shift_val = x & 15
        unique_shifts.add(shift_val)
        shift_frequencies[shift_val] = shift_frequencies.get(shift_val, 0) + 1
    
    high_freq_shifts = {k for k, v in shift_frequencies.items() if v > 1}
    rare_shifts = unique_shifts - high_freq_shifts

    # Threshold logic with short-circuiting and nested conditions
    def threshold_func(x):
        return x > 25 and (x % 3 == 0 or x % 5 == 0) and not (x in rare_shifts)

    # Core recursive validation (simple recursion)
    def validate_sequence(seq, idx=0, count=0):
        if idx >= len(seq):
            return count
        if seq[idx] > 30 and threshold_func(seq[idx]):
            return validate_sequence(seq, idx + 1, count + 1)
        else:
            return validate_sequence(seq, idx + 1, count)

    # Unused recursive call (misleading)
    dummy_count = validate_sequence(list(rare_shifts) + [0]*3)

    # Critical function with distractors
    def analyze_readings(data, condition):
        result_set = set()
        for item in data:
            if condition(item):
                result_set.add(item)
        
        # Additional irrelevant computation
        cumulative_xor = 0
        for item in data:
            cumulative_xor ^= (item * 3) % 257
        
        # Final diagnostic based on set size and modular sum
        base_score = len(result_set) * 100
        mod_sum = sum(result_set) % 89
        final_score = base_score + mod_sum
        
        # Dead branch
        if len(result_set) > 10:
            fallback = 0
            for _ in range(10):
                fallback = (fallback * 7 + 1) % 1000
            final_score -= fallback  # never executed

        return final_score

    final_diagnostic = analyze_readings(processed_data, threshold_func)
    print(f"Result: {final_diagnostic}")

sensor_network_analysis()