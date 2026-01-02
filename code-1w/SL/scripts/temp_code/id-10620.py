def analyze_sensor_data(raw_readings, threshold=0.75):
    # Simulate preprocessing pipeline with red herrings
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in normalized if x > 0.1]
    
    # Irrelevant transformation chain (distractor)
    inverted_map = list(map(lambda x: 1 - x, filtered))
    squared_residuals = [x**2 for x in inverted_map if x < 0.9]
    noise_floor = sum(squared_residuals) / len(squared_residuals) if squared_residuals else 0.0

    # Critical data path begins here
    binary_flags = [int(x >= threshold) for x in normalized]
    run_lengths = []
    current_run = 0
    
    for flag in binary_flags:
        if flag == 1:
            current_run += 1
        else:
            if current_run > 0:
                run_lengths.append(current_run)
                current_run = 0
    if current_run > 0:
        run_lengths.append(current_run)

    # Compute diagnostic metrics (only some are used later)
    avg_run_length = sum(run_lengths) / len(run_lengths) if run_lengths else 0
    max_consecutive = max(run_lengths) if run_lengths else 0
    total_active = sum(binary_flags)
    
    # Decoy statistical analysis (dead code path)
    def compute_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        probabilities = [f / len(data) for f in freq.values()]
        return -sum(p * log(p) for p in probabilities)
    
    entropy_value = compute_entropy(normalized[:len(normalized)//2]) if len(normalized) > 1 else 0.0

    # Real computation interleaved with distractions
    cumulative_energy = 0
    energy_curve = []
    for i, val in enumerate(raw_readings):
        if i % 3 == 0:
            cumulative_energy += val ** 1.5
        elif i % 4 == 0:
            cumulative_energy += val * 0.5
        energy_curve.append(cumulative_energy)
    
    # Key slicing operation (required Python feature)
    recent_energy = energy_curve[-5:]
    baseline = sum(recent_energy) / len(recent_energy)
    
    # Introduce conditional expression (required Python feature)
    adjustment = 2 if len(run_lengths) > 3 else (1 if max_consecutive > 4 else 0.5)
    
    # Multiple irrelevant variables (distractors)
    calibration_offset = (noise_floor * 1000) // 1
    stability_index = (total_active * avg_run_length) / (max_consecutive + 1e-8)
    anomaly_score = abs(calibration_offset - stability_index) * entropy_value

    # Core logic embedded in noise
    tolerance_sequence = [0.1 * (i + 1) for i in range(len(raw_readings))]
    tolerance_band = tolerance_sequence[len(raw_readings)//2] if raw_readings else 0.1
    
    # Aggregation with decoy elements
    aggregate_metrics = [
        avg_run_length * 10,
        max_consecutive * 5.5,
        baseline / 100,
        anomaly_score * 100,  # misleading but unused ultimately
        total_active * adjustment
    ]
    
    # Final distraction: unused complex structure
    diagnostic_report = {
        'readings_count': len(raw_readings),
        'peaks': [i for i, x in enumerate(normalized) if x > 0.9],
        'flags': binary_flags,
        'energy_snapshot': energy_curve[::2],
        'metadata_checksum': len(raw_readings) ^ 255
    }

    # CRITICAL STATEMENT - target of the question
    final_diagnostic = aggregate_metrics[-1] + correction_factor * tolerance_band

    # Print result as required
    print(f"Result: {final_diagnostic}")

# Hidden setup: values must be defined before function call
raw_readings_data = [12, 8, 15, 3, 9, 14, 7, 11]
correction_factor = 3

# Execute
analyze_sensor_data(raw_readings_data)
