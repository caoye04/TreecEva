def analyze_pattern_sequence(data_stream):
    temp_buffer = []
    cumulative_shift = 0
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            shifted = val << (i % 5)
            temp_buffer.append(shifted)
        elif i % 4 == 2:
            shifted = val >> (i % 3)
            temp_buffer.append(shifted + 1)
        else:
            temp_buffer.append(val)
    
    # Irrelevant transformation (dead-end analysis)
    dummy_analysis = [x ^ 255 for x in temp_buffer if x < 100]
    aggregate_noise = sum(dummy_analysis) // len(dummy_analysis) if dummy_analysis else 0

    # Real computation path
    base_values = [x for i, x in enumerate(temp_buffer) if i % 2 == 1]
    adjusted = [x + (i * 2) for i, x in enumerate(base_values)]
    return sum(adjusted)


def evaluate_signal_strength(signal):
    magnitude_peaks = []
    avg_magnitude = sum(signal) / len(signal)
    for idx, s in enumerate(signal):
        if s > avg_magnitude:
            magnitude_peaks.append((idx, s ** 0.5))
    
    # Distractor: complex tuple unpacking with unused result
    indexed_peaks = list(enumerate(magnitude_peaks))
    peak_positions, detailed_info = zip(*[(i, p) for i, p in indexed_peaks]) if indexed_peaks else ([], [])
    
    # Unused but plausible-looking metric
    coherence_factor = sum(p[1] for p in magnitude_peaks) / len(magnitude_peaks) if magnitude_peaks else 0.0
    
    return int(avg_magnitude * 10)


def calculate_composite_rating():
    raw_input = [12, 18, 24, 36, 48, 52, 60, 72, 84, 96]
    
    # Step 1: Pattern analysis
    pattern_result = analyze_pattern_sequence(raw_input)
    
    # Step 2: Signal evaluation (produces semi-relevant number)
    signal_metric = evaluate_signal_strength(raw_input)
    
    # Step 3: Auxiliary calculation with character logic
    label_prefix = "SYS_DIAG_"
    char_code_sum = sum(ord(c.lower()) for c in label_prefix if c.isalpha())
    adjustment_key = char_code_sum % 17
    
    # Step 4: Conditional override simulation (never triggers, distractor)
    override_flag = False
    emergency_offset = 0
    if any(c.isdigit() for c in label_prefix):
        override_flag = True
        emergency_offset = 999
    
    # Step 5: Main aggregation
    base_rating = pattern_result // 3
    secondary_boost = signal_metric * 2
    final_score = base_rating + secondary_boost - adjustment_key
    
    # Step 6: Redundant validation check (no effect)
    validation_checksum = sum([base_rating % 10, secondary_boost % 10, adjustment_key])
    if validation_checksum > 20:
        pass  # No-op, misleading control flow
    
    # Output target variable
    print(f"Result: {final_score}")
    return final_score

# Execution entry point
calculate_composite_rating()