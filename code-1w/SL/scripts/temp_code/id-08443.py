def analyze_sensor_network():
    # Simulated sensor readings (temperature in millidegrees C)
    raw_readings = [23450, 25100, 19800, 22750, 24300, 26800, 18900, 21500]
    
    # Irrelevant metadata
    device_ids = ['S1A', 'S1B', 'S2A', 'S3C', 'X9M', 'Y2K', 'Z5P', 'W7Q']
    location_map = {uid: f'Zone-{ord(uid[0]) % 5}' for uid in device_ids}
    deployment_dates = [(2023, 4, 12), (2023, 5, 3), (2023, 4, 28), (2023, 6, 1), 
                        (2023, 3, 15), (2023, 7, 9), (2023, 5, 22), (2023, 6, 14)]
    
    # Decoy processing
    baseline_shifts = [r % 1000 for r in raw_readings]
    normalized_shifts = [abs(s - 500) for s in baseline_shifts if s != 0]
    adjustment_log = []
    for ns in normalized_shifts:
        if ns > 400:
            adjustment_log.append(ns * 0.1)

    # Real preprocessing
    threshold = 20500
    filtered_data = [r for r in raw_readings if r > threshold]
    
    # Distractor: complex but unused validation
    def validate_consistency(data):
        if len(data) < 3:
            return False
        sorted_data = sorted(data)
        median = sorted_data[len(sorted_data)//2]
        return all(abs(x - median) < 5000 for x in data)
    
    is_stable = validate_consistency(raw_readings)  # Unused result
    
    # Bit manipulation red herring
    checksum = 0
    for r in raw_readings:
        checksum ^= r
        checksum = (checksum << 1) & 0xFFFF
    
    # Real calibration logic
    base_reference = 22000
    sample_variance = sum((r - base_reference)**2 for r in filtered_data) // len(filtered_data)
    calibration_offset = (sample_variance // 1000) + 1
    
    # Another decoy function
    def compute_entropy(values):
        from math import log2
        freq = {}
        for v in values:
            key = v // 1000
            freq[key] = freq.get(key, 0) + 1
        total = len(values)
        return -sum((count/total) * log2(count/total) for count in freq.values())
    
    entropy_score = compute_entropy(filtered_data)  # Computed but not used
    
    # Core transformation
    def process_readings(data, offset):
        adjusted = [d + offset * 100 for d in data]
        squared_residuals = [(a - 24000)**2 for a in adjusted]
        mean_square = sum(squared_residuals) / len(squared_residuals)
        rmse = mean_square ** 0.5
        return int(rmse // 10)  # Final diagnostic code
    
    # Key execution point
    final_diagnostic = process_readings(filtered_data, calibration_offset)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()