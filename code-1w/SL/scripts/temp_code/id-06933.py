from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def analyze_sensor_network():
    raw_readings = [145, 273, 91, 88, 190, 205, 78, 112, 244, 167, 95, 103, 150, 188, 210]
    calibration_offsets = [3, -2, 1, 0, -1, 2, -3, 1, 0, 2, -2, 1, 0, -1, 2]
    sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S1', 'S2', 'S3', 'S4', 'S5', 'S1', 'S2', 'S3', 'S4', 'S5']
    
    # Apply calibration (irrelevant to final result but looks important)
    calibrated_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]
    
    # Misleading statistical summary
    avg_reading = sum(calibrated_readings) / len(calibrated_readings)
    median_reading = sorted(calibrated_readings)[len(calibrated_readings)//2]
    mode_counter = Counter(calibrated_readings)
    
    # Filter logic based on dynamic thresholds (only base_threshold matters)
    base_threshold = 100
    fluctuation_factor = sum(1 for x in calibrated_readings if x > 150) / len(calibrated_readings)
    dynamic_threshold = base_threshold * (1 + fluctuation_factor)  # Distractor: not actually used
    
    # Actual filtering uses base_threshold only
    filtered_data = []
    id_to_readings = defaultdict(list)
    for i, reading in enumerate(raw_readings):
        if reading >= base_threshold:  # Uses raw, not calibrated
            filtered_data.append(reading)
            id_to_readings[sensor_ids[i]].append(reading)
    
    # Dead code path - never called
    def legacy_compatibility_mode(data):
        return [x * 0.95 for x in data if x % 2 == 0]
    
    # Unused transformation chain
    transformed = list(map(lambda x: x ** 0.5, filtered_data))
    indexed = list(enumerate(transformed))
    paired = list(zip(filtered_data, transformed))
    
    # Real processing function
    def process_readings(data, thresh):
        # Compute weighted sum with position-based weights (increasing interference)
        weight_sequence = [(i + 1) * 0.1 for i in range(len(data))]
        weighted_sum = sum(data[i] * weight_sequence[i] for i in range(len(data)))
        
        # Secondary adjustment based on distribution (distractor calculation)
        above_thresh_count = len([x for x in data if x > thresh * 1.5])
        adjustment_factor = above_thresh_count * 0.7
        
        # Tertiary logic with bit manipulation red herring
        binary_flags = [bin(x & 0xFF).count('1') for x in data]  # Bit count per reading
        parity_shift = sum(binary_flags) % 4  # Looks important, unused
        
        # Final computation: modular reduction of weighted sum
        intermediate = int(weighted_sum) + adjustment_factor
        result = (intermediate * 3) % 887  # Deterministic result
        
        # Decoy conditional that doesn't affect output
        if len(data) > 10 and adjustment_factor > 2:
            result ^= 255  # Never executes
        
        return result
    
    # Critical execution point
    final_diagnostic = process_readings(filtered_data, base_threshold)
    
    # Irrelevant logging operations
    log_entries = []
    for sid, readings in id_to_readings.items():
        log_entries.append(f"{sid}: {len(readings)} readings")
    
    # Print required output format
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()