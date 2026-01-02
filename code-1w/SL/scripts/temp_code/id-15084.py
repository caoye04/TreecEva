import itertools

def sensor_analysis():
    raw_readings = [145, 273, 91, 88, 192, 44, 73, 108, 65, 201]
    thresholds = {'low': 60, 'high': 180}
    calibration_factor = 0.87
    
    # Irrelevant transformation (distractor)
    normalized = list(map(lambda x: (x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), raw_readings))
    
    # Decoy function that's defined but not used directly
    def analyze_trend(data):
        return sum(1 for a, b in zip(data, data[1:]) if b > a)
    
    # Actual relevant filtering
    valid_range = lambda x: thresholds['low'] <= x <= thresholds['high']
    filtered_data = [x for x in raw_readings if valid_range(x)]
    
    # Red herring: complex unused data structure
    history_log = {
        'session_1': {'start': 140, 'end': 195, 'anomaly': False},
        'session_2': {'start': 90, 'end': 110, 'anomaly': True},
        'session_3': {'start': 60, 'end': 210, 'anomaly': False}
    }
    
    # Dead code path (never executed)
    if len(raw_readings) > 50:
        fallback_value = sum(raw_readings) / len(raw_readings)
        return fallback_value

    # Unused statistical calculations (misleading intermediate results)
    avg_reading = sum(raw_readings) / len(raw_readings)
    variance = sum((x - avg_reading) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = variance ** 0.5

    # Simulated noise correction (unused)
    corrected_noise = [x - 5 if x % 2 == 0 else x + 3 for x in raw_readings]

    # Core logic buried among distractions
    def process_readings(data, factor):
        adjusted = [int(x * factor) for x in data]
        # Further filter after adjustment
        adjusted_filtered = [x for x in adjusted if x % 2 == 1]  # Keep only odd values
        
        # Character counting distraction (string method use)
        status_msg = "Processing {} valid sensors".format(len(data))
        char_count = len(status_msg.replace(' ', ''))
        
        # Use of itertools to create artificial complexity
        repeated_adjusted = list(itertools.chain.from_iterable(itertools.repeat(x, 2) for x in adjusted_filtered[:3]))
        
        # Final computation
        base_score = sum(adjusted_filtered)
        penalty = len([x for x in adjusted if x < 50])
        bonus = char_count // 10
        
        # Critical result
        return base_score - (penalty * 10) + bonus

    # Another decoy: unused recursive function
    def recursive_smooth(arr, depth=0):
        if depth >= 2 or len(arr) < 2:
            return arr
        smoothed = [(arr[i] + arr[i+1]) // 2 for i in range(len(arr)-1)]
        return recursive_smooth(smoothed, depth + 1)

    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Multiple print statements (only one matters)
    print(f"Raw count: {len(raw_readings)}")
    print(f"Filtered count: {len(filtered_data)}")
    print(f"Calibration multiplier: {calibration_factor}")
    Target result: {final_diagnostic}

sensor_analysis()