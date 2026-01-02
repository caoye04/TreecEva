def analyze_signal_strength(raw_readings, threshold=0.75):
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [val for val in normalized if val > threshold]
    inverted = [round(1 - v, 4) for v in normalized]
    segment_a = normalized[:len(normalized)//2]
    segment_b = normalized[len(normalized)//2:]
    
    # Misleading intermediate computations
    baseline_shift = len(inverted) * 0.01
    temp_correction = sum(inverted) * baseline_shift
    adjustment_cycle = 0
    
    while adjustment_cycle < 3:
        temp_correction *= 0.95
        adjustment_cycle += 1
    
    # Distractor: unused path
    if len(segment_a) > len(segment_b):
        pivot_value = segment_a[len(segment_a)//2]
    else:
        pivot_value = segment_b[0] if segment_b else 0
    
    # Core logic disguised among distractions
    binary_flags = [1 if x > 0.85 else 0 for x in normalized]
    run_lengths = []
    current_run = 0
    for bit in binary_flags:
        if bit == 1:
            current_run += 1
        else:
            if current_run > 0:
                run_lengths.append(current_run)
                current_run = 0
    if current_run > 0:
        run_lengths.append(current_run)
    
    # Simulate multi-stage processing
    processed_segments = []
    for seg in [segment_a, segment_b]:
        weighted = sum(x * (i + 1) for i, x in enumerate(seg))
        if len(seg) > 0:
            processed_segments.append(round(weighted / len(seg), 4))
        else:
            processed_segments.append(0.0)
    
    # Efficiency depends on pattern consistency
    pattern_consistency = len(run_lengths) / len(normalized) if normalized else 0
    efficiency_factor = pattern_consistency * 1.75 if pattern_consistency > 0.1 else 0.5
    
    # Key statement
    filtration_yield = sum(processed_segments) * efficiency_factor
    
    # Red herring calculations
    diagnostic_score = (sum(binary_flags) + temp_correction) * baseline_shift
    audit_trail = ''.join(['1' if f else '0' for f in binary_flags])
    snapshot = audit_trail[::2]  # slicing operation used
    
    # Conditional expression (python idiom)
    final_status = 'PASS' if filtration_yield > 0.5 else 'FAIL'
    
    # Output required result
    print(f"Result: {filtration_yield}")
    return filtration_yield

# Input data
readings = [120, 180, 230, 250, 130, 90, 260, 240]
analyze_signal_strength(readings)