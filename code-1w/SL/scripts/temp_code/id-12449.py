def analyze_metrics(raw_values, threshold=0.75):
    normalized = [x / max(raw_values) for x in raw_values]
    filtered = [x for x in normalized if x > threshold]
    indices = [i for i, x in enumerate(normalized) if x in filtered]

    # Irrelevant transformation (distractor)
    reversed_map = {len(raw_values)-i: val for i, val in enumerate(raw_values)}
    temp_sum = sum(reversed_map[k] for k in reversed_map if k % 2 == 0)

    # Meaningless aggregation (dead path)
    dummy_aggregate = 0
    for i in range(len(normalized)):
        if i % 3 == 0:
            dummy_aggregate += normalized[i] * 1.5

    return filtered, indices, temp_sum


def transform_sequence(seq):
    # Unused helper (decoy function)
    paired = list(zip(seq[::2], seq[1::2]))
    return [a + b for a, b in paired]


def preprocess_input(data_stream):
    # Split and restructure data
    chunks = [data_stream[i:i+4] for i in range(0, len(data_stream), 4)]
    reshaped = [item for chunk in chunks for item in chunk if sum(chunk) > 10]

    # Distractor: irrelevant sorting and zipping
    sorted_reshaped = sorted(reshaped, reverse=True)
    indexed = list(enumerate(sorted_reshaped))
    zipped_pairs = list(zip(sorted_reshaped, sorted_reshaped[1:]))

    # Fake correlation metric (not used later)
    correlation_proxy = sum(a * b for a, b in zipped_pairs) / len(zipped_pairs) if zipped_pairs else 0

    return reshaped


def calculate_efficiency(dataset, overhead):
    base_total = sum(dataset)
    item_count = len(dataset)

    # Complex weighting with bit manipulation distraction
    weights = []
    for i in range(item_count):
        weight = (i + 1) ** 0.5
        # Bitwise red herring
        if i > 0 and (i & (i - 1)) == 0:  # power of two index
            weight *= 1.2
        weights.append(weight)
    
    weighted_total = sum(d * w for d, w in zip(dataset, weights))
    
    # Efficiency formula
    raw_efficiency = weighted_total / (base_total + 1e-8)
    adjusted = raw_efficiency * (1 - overhead / 100)
    
    # Additional misleading calculation (not part of final result)
    entropy_like = 0
    for w in weights:
        if w > 1.0:
            entropy_like -= w * __import__('math').log(w)

    return round(adjusted * 100, 4)

# Main execution flow
sensor_readings = [12, 15, 8, 23, 19, 4, 31, 11, 16, 22]
config_flags = [True, False, True, True, False]

# Step 1: Analyze metrics (produces side results)
metrics, positions, dummy_sum = analyze_metrics(sensor_readings, threshold=0.6)

# Step 2: Preprocess input with distractors
processed_data = preprocess_input(sensor_readings)

# Step 3: Simulate system overhead from flags (irrelevant complexity)
count_enabled = len([f for f in config_flags if f])
temp_overhead = (count_enabled * 17) % 13

# Step 4: Actual critical computation
overhead_factor = 12  # Final overhead used (misleading setup above)
efficiency_score = calculate_efficiency(processed_data, overhead_factor)

# Output result as required
print(f"Target result: {efficiency_score}")