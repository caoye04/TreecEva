from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation
def analyze_sensor_network():
    # Core data
    raw_readings = [104, 95, 112, 98, 103, 119, 97, 110, 105, 108, 114, 99, 101, 117, 107]
    timestamps = list(range(1500, 1515))
    sensor_ids = ['S' + str(i % 5) for i in range(15)]

    # Irrelevant transformation 1: timestamp normalization (unused later)
    normalized_times = [(t - 1500) / 10 for t in timestamps]
    time_categories = ['A' if nt < 0.5 else 'B' if nt < 1.0 else 'C' for nt in normalized_times]

    # Distractor variables
    calibration_factor = 1.03
    baseline_offset = sum(raw_readings[:5]) / 5
    adjusted_baseline = [x * calibration_factor - 0.5 for x in raw_readings]

    # Decoy function (never called)
    def deprecated_analysis(data):
        return sum(x ** 0.5 for x in data if x > 100) // len(data)

    # Red herring computation chain
    outlier_flags = []
    for i, val in enumerate(raw_readings):
        deviation = abs(val - baseline_offset)
        is_outlier = deviation > 15
        confidence = 0.8 if is_outlier else 0.95
        outlier_flags.append((i, val, is_outlier, confidence))

    # Dead code path - looks meaningful but unused
    if len(outlier_flags) > 10:
        correction_matrix = [[i + j for j in range(3)] for i in range(3)]
        smoothed_values = [raw_readings[i] * (0.9 + i*0.01) for i in range(len(raw_readings))]

    # Actual relevant processing begins here
    zipped_data = list(zip(sensor_ids, raw_readings, timestamps))
    
    # Filtering logic: only readings above 100 and from sensors S0, S2, S4
    filtered_data = []
    for sid, reading, ts in zipped_data:
        if reading > 100 and sid in ['S0', 'S2', 'S4']:
            filtered_data.append({'id': sid, 'val': reading, 'ts': ts})
    
    # Create threshold map (S0: 105, S2: 110, S4: 108)
    threshold_map = defaultdict(int)
    for i in range(0, 5, 2):
        sensor_key = f'S{i}'
        base_threshold = 105 + (i // 2) * 5
        threshold_map[sensor_key] = base_threshold
    
    # Another distractor: frequency analysis of sensor IDs (not used in final result)
    id_counter = Counter(sensor_ids)
    freq_weights = {k: 1/v for k, v in id_counter.items()}
    weighted_sum = sum(freq_weights[sid] * val for sid, val, _ in zipped_data)

    # Key function that computes the answer
    def process_readings(data, thresholds):
        total = 0
        counts = defaultdict(int)
        
        # First pass: count per sensor
        for entry in data:
            counts[entry['id']] += 1
        
        # Second pass: apply conditional logic
        for entry in data:
            sensor = entry['id']
            value = entry['val']
            threshold = thresholds[sensor]
            
            # Only consider entries where value exceeds threshold
            if value > threshold:
                # Complex scoring: (value - threshold) * count_weight
                count_weight = counts[sensor]
                bonus = 0
                
                # Additional condition: timestamp-based bonus
                ts = entry['ts']
                if ts % 2 == 0:
                    bonus = 2
                elif ts > 1508:
                    bonus = 1
                
                contribution = (value - threshold) * count_weight + bonus
                total += contribution
                
                # Nested logical trap: looks like it affects result but doesn't
                temp_debug = []
                for _ in range(3):
                    temp_debug.append(contribution * 0.1)

        # Final adjustment based on number of distinct sensors
        distinct_sensors = len(counts)
        if distinct_sensors >= 2:
            total += 5
        
        # Apply bitwise mask (looks complex but deterministic)
        masked_total = total ^ 0b1101
        masked_total = masked_total & 0b111111  # Keep lower 6 bits
        
        return masked_total

    # Execute critical statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # More red herrings: unused statistical computations
    squared_errors = [(x - baseline_offset)**2 for x in raw_readings]
    mse = sum(squared_errors) / len(squared_errors)
    rmse = mse ** 0.5
    
    # Unused correlation attempt
    paired_data = list(zip(adjusted_baseline, raw_readings))
    covariance = sum((a - sum(adjusted_baseline)/len(adjusted_baseline)) * 
                     (b - sum(raw_readings)/len(raw_readings)) for a, b in paired_data)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute and capture result
analyze_sensor_network()