def analyze_sensor_stream(raw_stream, config):
    # Irrelevant preprocessing: character counting in metadata
    metadata_tag = "SENSORv4_DIAGNOSTIC"
    char_count = sum(1 for c in metadata_tag if c in 'AEIOU')

    # Distractor: unused transformation function
    def transform_legacy(x):
        return (x << 2) ^ 0xCAFEBABE

    # Actual relevant data extraction
    readings = [x for x in raw_stream if isinstance(x, int) and x >= 0]

    # Red herring: complex but unused bit manipulation chain
    accumulated_noise = 0
    for i in range(len(readings)):
        if i % 3 == 0:
            accumulated_noise ^= (readings[i] << 1) | 1

    # Decoy statistical analysis with no impact
    mean_guess = sum(readings[:5]) / min(5, len(readings)) if readings else 0
    variance_proxy = sum((x - mean_guess) ** 2 for x in readings[:5]) / min(5, len(readings)) if readings else 0

    # Conditional branch based on config flags (only one path matters)
    if config.get('mode') == 'calibrated':
        scale_factor = config.get('gain', 1.0)
        calibrated = [x * scale_factor for x in readings]
    else:
        # This is the actual path taken
        calibrated = [x + 1 for x in readings]  # Simple shift

    # Another distraction: tuple-based unpacking that goes unused
    stats_summary = (len(calibrated), min(calibrated), max(calibrated))
    sample_size, _, peak_value = stats_summary

    # Real logic begins: filter based on dynamic threshold
    base_threshold = config.get('threshold', 50)
    dynamic_adjustment = 1 if sum(calibrated) > 300 else -1
    threshold = base_threshold * (1 + dynamic_adjustment * 0.1)

    # Filter data above threshold
    filtered_data = [x for x in calibrated if x > threshold]

    # Process filtered readings with zip and enumerate (required features)
    def process_readings(data, limit):
        if not data:
            return -1
        
        # Use of enumerate and zip (required)
        indexed = list(enumerate(data, start=1))
        shifted = data[1:] + [0]
        pairs = zip(indexed, shifted)
        
        total_weight = 0.0
        for (i, value), next_val in pairs:
            # Complex-looking but deterministic weighting
            weight = (value % 7) * (i % 5)
            if next_val & 1:
                weight += 0.5
            total_weight += weight

        # Additional distractor: string method on irrelevant tag
        tag_parts = metadata_tag.lower().split('_')
        extension = len([p for p in tag_parts if 'diag' in p])

        # Final computation
        adjustment = len(tag_parts) - extension
        return int(total_weight + adjustment - len(data))

    # Dead code path: never called but looks important
    def generate_report():
        return ''.join(reversed(metadata_tag))

    # Key statement
    final_diagnostic = process_readings(filtered_data, threshold)
    
    # Ensure output is printed
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data and configuration
sensor_input = [45, 67, 23, 89, 12, 77, 91, 5, 60, 34]
settings = {'mode': 'raw', 'threshold': 65}

# Execute
result = analyze_sensor_stream(sensor_input, settings)