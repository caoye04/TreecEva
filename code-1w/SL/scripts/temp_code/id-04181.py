def analyze_sensor_network():
    # Simulated sensor readings (real data)
    raw_readings = [145, 273, 89, 412, 367, 221, 198, 305, 441, 177]
    
    # Irrelevant auxiliary arrays (distractors)
    maintenance_logs = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    location_ids = ['A7', 'B3', 'C9', 'D2', 'E5', 'F1', 'G8', 'H4', 'I6', 'J0']
    temp_cache = {i: val * 0.85 for i, val in enumerate(raw_readings)}

    # Real processing begins: filter out anomalous high values
    threshold = sum(raw_readings) // len(raw_readings) + 50
    filtered_indices = [i for i, v in enumerate(raw_readings) if v < threshold]
    filtered_data = [raw_readings[i] for i in filtered_indices]
    
    # Decoy transformation (never used)
    inverted_map = {v: i for i, v in enumerate(reversed(raw_readings))}
    shadow_copy = [x * 1.1 for x in raw_readings if x % 2 == 0]

    # Calibration logic (critical path)
    base_reference = 1024
    signal_strength = 7
    calibration_factor = (base_reference >> signal_strength) + 3.7
    
    # Fake alternate calibration (dead code path)
    if False:
        calibration_factor = max(filtered_data) / min(filtered_data)
        backup_check = set(shadow_copy) & set(temp_cache.values())

    # Core processing function
    def process_readings(data, factor):
        # Apply non-uniform scaling
        scaled = [d * factor for d in data]
        
        # Bit manipulation for noise correction (key step)
        corrected = []
        for val in scaled:
            int_val = int(val)
            flipped = int_val ^ 0b1101  # XOR with binary pattern
            shifted = (flipped << 1) & 0xFFFF  # Left shift and mask
            normalized = shifted / 100.0
            corrected.append(normalized)
        
        # Secondary filtering
        valid_corrected = [c for c in corrected if c > 5.0]
        
        # Set-based anomaly detection (unused branch)
        unique_set = set(valid_corrected)
        duplicate_flag = len(unique_set) != len(valid_corrected)
        
        # Real aggregation
        aggregate = 0
        for idx, item in enumerate(valid_corrected):
            weight = 1 + (idx * 0.1)
            aggregate += item * weight
        
        # Final adjustment using zip with offset indices
        offsets = list(range(len(valid_corrected)))
        pairs = zip(valid_corrected, offsets)
        adjusted_sum = sum((val + off * 0.25) for val, off in pairs)
        
        return round(adjusted_sum, 6)

    # Misleading secondary analysis (distractor)
    def diagnostic_probe(seq):
        entropy = 0
        freq = {}
        for x in seq:
            freq[x] = freq.get(x, 0) + 1
        total = len(seq)
        for count in freq.values():
            p = count / total
            entropy -= p * p  # Simplified measure
        return entropy

    # Unused recursive helper (red herring)
    def accumulate_recursive(arr, index=0):
        if index >= len(arr):
            return 0
        return arr[index] + 0.9 * accumulate_recursive(arr, index + 1)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Irrelevant final checks
    consistency_check = all(x < 500 for x in raw_readings)
    metadata_summary = dict(zip(['count', 'status'], [len(filtered_data), 'stable']))

    return final_diagnostic

# Execute and output
analyze_sensor_network()