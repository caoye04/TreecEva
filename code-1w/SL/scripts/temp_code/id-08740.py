def process_sensor_data(raw_readings, filter_strength=0.85):
    # Irrelevant signal normalization (dead path)
    normalized = [x * 0.99 for x in raw_readings if x > -100]
    adjusted_readings = []

    for val in raw_readings:
        if val < 0:
            adjusted_readings.append(abs(val) ** 0.5)
        elif val == 0:
            adjusted_readings.append(0.0)
        else:
            adjusted_readings.append(val * filter_strength)

    # Decoy transformation with no downstream use
    inverted = [1.0 / (1 + x) for x in adjusted_readings if x != 0]
    smoothed = []
    for i in range(1, len(adjusted_readings) - 1):
        window_avg = (adjusted_readings[i-1] + adjusted_readings[i] + adjusted_readings[i+1]) / 3
        smoothed.append(window_avg)

    # Critical subset selection based on dynamic threshold
    dynamic_floor = sum(adjusted_readings) / len(adjusted_readings) * 0.6
    collected_signals = {int(x) for x in adjusted_readings if x > dynamic_floor}

    # Unused but misleading set operations
    outlier_set = {x for x in adjusted_readings if x < 2.0}
    common_elements = collected_signals & outlier_set  # Red herring

    baseline_threshold = len([x for x in raw_readings if x % 2 == 1])

    def analyze_pattern(signal_set, threshold):
        # Complex nested logic with multiple distractions
        if not signal_set:
            return -1
        
        # Bit manipulation decoy
        magic_shift = (threshold << 2) ^ 5
        temp_result = 0
        for item in signal_set:
            if item % 3 == 0:
                temp_result += item * 1.5
            elif item % 4 == 0:
                temp_result -= item * 0.75
            else:
                # Nested condition with case conversion distraction
                word_rep = str(item)
                toggled = ''.join(c.upper() if c.islower() else c.lower() for c in word_rep)
                if toggled.isdigit():
                    temp_result += int(toggled) // 2

        # Distractor: unused recursive function
        def recursive_weight(n):
            if n <= 1:
                return 1
            return n + recursive_weight(n - 2)
        
        # Final computation using cross-concept logic
        size_factor = len(signal_set) ** 2
        sum_filter = sum(x for x in signal_set if x > threshold)
        
        # Key calculation path
        intermediate = temp_result + size_factor
        correction = 0
        if len(signal_set) > threshold:
            correction = magic_shift % 9
        
        final_score = intermediate - sum_filter + correction
        
        # Secondary data structure manipulation (decoy)
        history_log = [{'entry': x, 'valid': x > 5} for x in signal_set]
        valid_count = sum(1 for entry in history_log if entry['valid'])
        
        # Actual answer derivation
        return int(final_score + valid_count)

    # Execution point of interest
    final_diagnostic = analyze_pattern(collected_signals, baseline_threshold)
    
    # Additional irrelevant post-processing
    diagnostic_chain = []
    for _ in range(3):
        diagnostic_chain.append({'level': 'deep', 'status': 'nominal'})
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

# Simulated sensor input (deterministic)
input_data = [12, -6, 0, 18, 7, 4, 9, 11]
process_sensor_data(input_data)