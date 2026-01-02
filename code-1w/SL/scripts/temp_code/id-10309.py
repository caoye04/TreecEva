import math

def analyze_sensor_network():
    # Simulated sensor data with metadata (real and decoy)
    raw_readings = [14.2, 18.7, 9.1, 22.5, 15.3, 11.8, 25.6, 13.4, 16.9, 19.2]
    timestamps = [1623456000, 1623456060, 1623456120, 1623456180, 1623456240,
                  1623456300, 1623456360, 1623456420, 1623456480, 1623456540]
    locations = ['A1', 'A2', 'B1', 'A1', 'B2', 'C1', 'B2', 'A2', 'C1', 'A1']

    # Irrelevant processing: location frequency analysis (distractor)
    loc_count = {}
    for loc in locations:
        loc_count[loc] = loc_count.get(loc, 0) + 1
    
    # Decoy transformation: meaningless scaling
    scaled_locs = [ord(loc[0]) * 100 + int(loc[1]) for loc in locations]

    # Real data path begins: filter readings above threshold
    threshold = 12.0
    filtered_indices = [i for i, val in enumerate(raw_readings) if val > threshold]
    filtered_data = [raw_readings[i] for i in filtered_indices]
    filtered_times = [timestamps[i] for i in filtered_indices]

    # Misleading intermediate: time delta analysis (unused later)
    time_deltas = [filtered_times[i+1] - filtered_times[i] for i in range(len(filtered_times)-1)]
    avg_delta = sum(time_deltas) / len(time_deltas) if time_deltas else 0

    # Red herring function: never called in critical path
    def compute_entropy(data):
        from collections import Counter
        counts = Counter(data)
        total = len(data)
        return -sum((c/total) * math.log2(c/total) for c in counts.values())

    # Another red herring: complex but unused transformation
    zipped_meta = list(zip(filtered_data, filtered_times, [f'Node_{i}' for i in range(len(filtered_data))]))
    node_summary = {node: [] for _, _, node in zipped_meta}
    for val, _, node in zipped_meta:
        node_summary[node].append(val)

    # Actual calibration factor derived from bit manipulation distraction
    seed_value = 0b101101  # Arbitrary seed
    bit_shifted = (seed_value << 3) | 0b101
    magic_constant = (bit_shifted ^ 0b11001101) % 17
    calibration_factor = round(math.sin(magic_constant) * 100, 4)

    # Core processing function (uses lambda and string methods as required)
    def process_readings(data, calib):
        # Normalize using calibration
        calibrated = [x * calib for x in data]
        
        # Use of lambda for threshold classification
        classify = lambda x: 'high' if x > 1000 else 'normal'
        categories = [classify(x) for x in calibrated]
        
        # String method distraction: counting 'h' in classifications
        total_h_chars = sum(s.count('h') for s in categories)
        
        # Actual computation path: variance adjustment with character count side effect
        mean_val = sum(calibrated) / len(calibrated)
        variance = sum((x - mean_val) ** 2 for x in calibrated) / len(calibrated)
        adjusted_variance = variance - total_h_chars * 0.5  # Minor correction
        
        # Final nonlinear transformation
        return int(abs(adjusted_variance ** 0.5 * 100)) + total_h_chars

    # Dead code path: entropy analysis not used
    if len(filtered_data) > 5:
        excess_entropy = 0
        for i, val in enumerate(filtered_data):
            if i % 2 == 0:
                excess_entropy += math.log(val) if val > 0 else 0

    # Key statement
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()