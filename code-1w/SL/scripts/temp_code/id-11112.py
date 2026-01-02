def analyze_sensor_array(raw_readings, calibration_factor, noise_floor):
    # Irrelevant preprocessing: normalize using unused method
    normalized = [x * calibration_factor for x in raw_readings if x > noise_floor]
    inverted = [1 / (x + 1e-5) for x in normalized]

    # Distractor: complex but unused transformation chain
    transformed = []
    accumulator = 0
    for idx, val in enumerate(inverted):
        if idx % 2 == 0:
            accumulator += val ** 0.5
        else:
            accumulator -= val ** 0.3
        transformed.append(accumulator)

    # Actual relevant data extraction
    readings_with_index = list(enumerate(raw_readings))
    valid_pairs = [(i, v) for i, v in readings_with_index if v > 50 and i % 3 != 0]

    # Decoy aggregation
    decoy_stats = {
        'max_val': max(inverted) if inverted else 0,
        'min_inv': min(inverted) if inverted else 0,
        'total_entries': len(inverted)
    }

    # Real filtering begins here — only this matters
    filtered_data = [v for i, v in valid_pairs if v < 500]

    # Threshold map built from conditional logic
    base_threshold = 75
    threshold_map = {}
    for value in filtered_data:
        if value < 100:
            category = 'low'
            adjustment = 0.9
        elif value < 200:
            category = 'medium'
            adjustment = 1.1
        else:
            category = 'high'
            adjustment = 1.3
        
        # Only last assignment per category sticks (overwriting)
        threshold_map[category] = int(value * adjustment)

    # Dead code path: never called
    def legacy_compensate(x):
        return x * 0.8 + 10

    # Actual processing function (defined inline to obscure)
    def process_readings(data, thresholds):
        count_low = sum(1 for x in data if x < 100)
        count_medium = sum(1 for x in data if 100 <= x < 200)
        count_high = sum(1 for x in data if x >= 200)
        
        # Weighted diagnostic score
        weights = {'low': 1, 'medium': 2, 'high': 3}
        total_score = (
            count_low * weights['low'] +
            count_medium * weights['medium'] +
            count_high * weights['high']
        )
        
        # Use only the 'medium' threshold as offset, if exists
        offset = thresholds.get('medium', 50)
        
        # Diagnostic also depends on zip-based alignment check
        shifted = [x + 10 for x in data]
        matches = 0
        for a, b in zip(data, shifted):
            if a < b and (a + b) % 2 == 0:
                matches += 1
        
        # Final formula: score + offset - matches
        result = total_score + offset - matches
        return int(result)

    # Key statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Unused cleanup
    cleaned = [x for x in raw_readings if x not in filtered_data]
    
    # Output target variable
    print(f"Result: {final_diagnostic}")

# Simulate sensor input
sensor_input = [45, 88, 105, 167, 250, 92, 198, 505, 73, 210]
calibration = 1.05
floor = 40

# Execute main analysis
analyze_sensor_array(sensor_input, calibration, floor)