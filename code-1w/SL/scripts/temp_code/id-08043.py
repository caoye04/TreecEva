import itertools

# Simulated sensor data processing with noise filtering and diagnostic metrics
def analyze_sensor_stream(raw_data, threshold=0.75):
    # Irrelevant diagnostic counters (distractors)
    debug_passes = 0
    anomaly_count = 0
    baseline_offset = 0.0
    temp_cache = []
    
    # Core signal processing variables
    filtered_signals = []
    signal_magnitudes = []
    bit_encoded_flags = 0
    
    for idx, entry in enumerate(raw_data):
        raw_value = entry['value']
        quality_flag = entry['quality']

        # Noise reduction: only process high-quality signals above dynamic threshold
        if quality_flag < threshold:
            anomaly_count += 1
            continue
        
        # Bitwise encoding of positional pattern (every 3rd valid signal sets a flag)
        if (idx + 1) % 3 == 0:
            bit_encoded_flags ^= (1 << (idx % 8))

        # Transform and store valid signals
        adjusted_value = abs(raw_value - baseline_offset)
        transformed = int(adjusted_value * 100) & 0xFF  # Scale and clamp to byte
        
        filtered_signals.append(transformed)
        signal_magnitudes.append(adjusted_value)
        
        # Dead code path: never executed due to fixed condition (red herring)
        if len(filtered_signals) > 1000:
            temp_cache.extend([0] * len(filtered_signals))
            debug_passes += 1  # Unused increment

    # Irrelevant statistical analysis (distractor block)
    mean_magnitude = sum(signal_magnitudes) / (len(signal_magnitudes) or 1)
    variance_proxy = sum((x - mean_magnitude) ** 2 for x in signal_magnitudes) / (len(signal_magnitudes) or 1)
    entropy_approx = 0.0
    for v in set(int(x * 10) for x in signal_magnitudes):
        p = sum(1 for x in signal_magnitudes if int(x * 10) == v) / len(signal_magnitudes)
        if p > 0:
            entropy_approx -= p * __import__('math').log(p)

    # Secondary distraction: unused transformation chain
    reshaped_data = [list(group) for k, group in itertools.groupby(sorted(filtered_signals), key=lambda x: x > 127)]
    compression_ratio = len(raw_data) / (sum(len(r) for r in reshaped_data) or 1) if reshaped_data else 0
    
    # Decoy metric with misleading name
    fidelity_index = bit_encoded_flags % 97

    # Actual target computation path
    magnitude_squares = [m ** 2 for m in signal_magnitudes]
    total_energy = sum(magnitude_squares)
    normalization_factor = max(signal_magnitudes) if signal_magnitudes else 1
    normalized_energy = total_energy / normalization_factor
    
    # Key derived measure before final aggregation
    aggregate_measure = int(normalized_energy) ^ bit_encoded_flags
    
    # Critical statement: answer depends on this
    filtration_score = aggregate_measure // (len(processed_signals) or 1)
    
    # Unrelated logging output (never used)
    log_entry = f"Processed {len(filtered_signals)} signals with {anomaly_count} anomalies."
    
    # Print required result at end
    print(f"Result: {filtration_score}")
    return filtration_score

# Simulated input data (deterministic)
raw_input_stream = [
    {'value': 0.42, 'quality': 0.8},
    {'value': 0.68, 'quality': 0.9},
    {'value': 0.33, 'quality': 0.6},  # filtered out (below threshold)
    {'value': 0.91, 'quality': 0.85},
    {'value': 0.15, 'quality': 0.95},
    {'value': 0.77, 'quality': 0.76},
    {'value': 0.54, 'quality': 0.5},   # filtered out
    {'value': 0.88, 'quality': 0.88},
    {'value': 0.29, 'quality': 0.91}
]

# Dead assignment - looks important but unused later
processed_signals = [x for x in raw_input_stream if x['quality'] >= 0.7]

# Execute function
analyze_sensor_stream(raw_input_stream)