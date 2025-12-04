def analyze_signal_patterns(raw_data, threshold=10):
    # Initialize data structures for signal processing
    noise_levels = {i: (i * 3) % 7 for i in range(20)}
    active_signals = set([2, 5, 8, 13, 17])
    reference_pattern = set([3, 5, 8, 10, 17, 19])
    
    # Calculate baseline metrics
    baseline = sum(noise_levels.values()) // len(noise_levels)
    significance_factor = 4 if baseline > 10 else 3
    
    # Preliminary filtering - this doesn't affect final result
    filtered_data = []
    for idx, value in enumerate(raw_data):
        if idx in noise_levels and noise_levels[idx] < threshold:
            filtered_data.append(value * 2)
        else:
            filtered_data.append(value)
    
    # Process interference patterns
    interference_detected = False
    potential_matches = set()
    for i in range(len(filtered_data) - 2):
        segment = filtered_data[i:i+3]
        if sum(segment) > threshold * 2:
            interference_detected = True
            potential_matches.add(i % 20)
    
    # Adjust signals based on interference
    if interference_detected and len(potential_matches) > 2:
        # This branch is deliberately misleading
        active_signals = active_signals.union(potential_matches)
        significance_factor = significance_factor - 1
    
    # Calculate signal quality - red herring calculation
    quality_index = 0
    for signal in active_signals:
        if signal in reference_pattern:
            quality_index += 2
        else:
            quality_index -= 1
    
    # Determine optimal sequence - this is the key calculation
    optimal_sequence = len(active_signals & reference_pattern) * significance_factor
    
    # More distraction calculations
    alternative_sequence = significance_factor * sum(1 for s in active_signals if s % 2 == 0)
    sequence_ratio = optimal_sequence / alternative_sequence if alternative_sequence else 0
    
    # This is never true, creating dead code
    if sequence_ratio > 5:
        optimal_sequence = optimal_sequence + int(sequence_ratio)
    
    return optimal_sequence if optimal_sequence > 0 else baseline

# Sample data for processing
raw_data = [5, 12, 8, 3, 15, 7, 2, 9, 11, 4, 6, 13]

# Process the data and get result
result = analyze_signal_patterns(raw_data)
print(f"Result: {result}")