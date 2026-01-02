def sensor_network_analysis():
    raw_readings = [145, 273, 98, 412, 68, 305, 221, 167, 89, 344, 266, 123]
    calibration_offset = 17
    sample_timestamps = list(range(1000, 1012))
    location_grid = [(i, j) for i in range(3) for j in range(4)]
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 3) for x in raw_readings]
    
    # Decoy function that's defined but not used in critical path
    def deprecated_filter(data, limit=200):
        return [x for x in data if x > limit]
    
    # Actual processing begins
    adjusted_readings = [x + calibration_offset for x in raw_readings]
    
    # Linear search for first high-value reading (distraction)
    first_high_idx = -1
    for i, val in enumerate(adjusted_readings):
        if val > 300 and first_high_idx == -1:
            first_high_idx = i
            break  # early return inside loop
    
    # Destructuring assignment (tuple unpacking)
    primary, secondary = adjusted_readings[:6], adjusted_readings[6:]
    
    # Red herring: complex but unused bitwise computation
    checksum = 0
    for x in raw_readings:
        checksum ^= (x << 2) | (x >> 3)
    
    # Filtering logic with lambda (used)
    noise_floor = 150
    filtered_data = list(filter(lambda x: x > noise_floor, adjusted_readings))
    
    # Misleading intermediate aggregate
    avg_primary = sum(primary) / len(primary)
    avg_secondary = sum(secondary) / len(secondary)
    
    # Dictionary-based mapping (cross-reference distractor)
    status_codes = {1: 'OK', 2: 'WARN', 3: 'ALERT'}
    reading_status = {r: 2 if r < 250 else 3 for r in filtered_data}
    
    # Higher-order function with closure (relevant)
    def create_threshold(baseline):
        def threshold_check(val):
            return val > baseline * 1.15
        return threshold_check
    
    # Critical function using zip and enumerate
    def process_readings(data, threshold_fn):
        cumulative = 0
        weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.2]  # potential weight mismatch
        
        # Nested logic with enumerate and zip
        for idx, (value, weight) in enumerate(zip(data, weights)):
            if idx % 2 == 0 and threshold_fn(value):
                cumulative += value * weight
            elif value > 300:
                cumulative += value * 0.05
        
        # Dead code path (never reached due to structure)
        if False:
            cumulative = max(data) - min(data)
            
        return int(cumulative)  # ensure integer result
    
    threshold_func = create_threshold(avg_primary)
    final_diagnostic = process_readings(filtered_data, threshold_func)
    
    # Unused but plausible-looking diagnostic
    anomaly_count = sum(1 for x in adjusted_readings if x > 400)
    
    # Output required result
    print(f"Result: {final_diagnostic}")

sensor_network_analysis()