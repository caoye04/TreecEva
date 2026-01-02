def analyze_sensor_data(data_stream):
    # Simulate preprocessing steps with distractions
    baseline_offset = 23
    calibration_map = {i: (i * 1.05) for i in range(100)}
    adjusted_values = [int(x * 1.02 + baseline_offset) for x in data_stream]

    # Irrelevant transformation - dead path
    inverted_map = {v: k for k, v in calibration_map.items()}
    temp_result = [x for x in adjusted_values if x in inverted_map]  # Unused

    # Core logic embedded in noise
    thresholds = [x for x in adjusted_values if x > 30]
    paired_indices = [(i, j) for i in range(3) for j in range(4) if i != j]
    index_product = [i * j for i, j in paired_indices]
    aggregate_marker = sum(index_product) // 4  # Misleading intermediate

    # Actual signal extraction
    raw_signals = [x for x in adjusted_values if x % 2 == 1]  # Only odd values are valid signals
    signal_pairs = [(raw_signals[i], raw_signals[i+1]) for i in range(0, len(raw_signals)-1, 2)]
    
    # Compute products but only retain those matching a hidden pattern
    products = [a * b for a, b in signal_pairs]
    
    # Decoy filtering path
    invalid_mask = [p for p in products if p < 500]  # Distractor list
    if len(invalid_mask) > 10:
        fallback = sum(invalid_mask)
    else:
        fallback = 0  # Never used

    # Real filter based on bit properties
    relevant_products = [p for p in products if (p & (p - 1)) == 0]  # Powers of two

    # Secondary irrelevant structure
    histogram = {}
    for p in products:
        bin_key = p // 50
        histogram[bin_key] = histogram.get(bin_key, 0) + 1

    # Critical execution point
    filtered_sum = sum(relevant_products)

    # Final red herring operation
    checksum = 0
    for i, v in enumerate(relevant_products):
        checksum ^= (v + i) * 3

    return filtered_sum

# Input data - deterministic sensor readings
data_stream = [18, 27, 33, 15, 42, 13, 29, 16, 24, 11, 37, 19, 26, 21, 31, 14]

result = analyze_sensor_data(data_stream)
print(f"Result: {result}")