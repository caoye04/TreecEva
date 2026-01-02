def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.0, 25.3, 20.1, 30.2, 18.7, 27.8, 22.4, 19.5, 24.6]
    threshold = 20.5
    calibration_factor = 0.97
    outlier_buffer = []
    processed = []
    temp_sum = 0.0

    # Irrelevant transformation: convert to Fahrenheit and back (distraction)
    fahrenheit_map = [(t * 9/5) + 32 for t in raw_readings]
    converted_back = [(f - 32) * 5/9 for f in fahrenheit_map]

    # Actual filtering logic: only temperatures above threshold are valid
    filtered_data = [temp for temp in raw_readings if temp > threshold]

    # Distractor: unused statistical calculations
    mean_raw = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_raw) / std_dev for x in raw_readings]

    # Another red herring: simulate network latency compensation (unused)
    latency_shift = 0.0
    for i in range(len(raw_readings)):
        if i % 3 == 0:
            latency_shift += 0.01 * raw_readings[i]

    # Real processing function (nested logic with dictionary use)
    def process_readings(data, calib):
        result_log = {}
        adjusted = []
        for idx, val in enumerate(data):
            corrected = val * calib
            category = 'high' if corrected > 25.0 else 'medium'
            result_log[idx] = {'raw': val, 'corrected': round(corrected, 3), 'class': category}
            adjusted.append(corrected)
        
        # Bitwise manipulation on index keys (unnecessary but plausible)
        hash_key = 0
        for k in result_log.keys():
            hash_key ^= (k << 2) | (k >> 1)
        
        # Real aggregation: sum of adjusted values
        total_adjusted = sum(adjusted)
        
        # Decoy reduction using zip and enumerate (not used in final result)
        pairs = list(zip(adjusted[:-1], adjusted[1:]))
        trends = []
        for i, (a, b) in enumerate(pairs):
            trends.append(1 if b > a else 0)
        
        return total_adjusted  # This is the actual result

    # Secondary distractor: simulate redundant system check
    system_health = True
    health_flags = {}
    for i, temp in enumerate(raw_readings):
        flag = (temp < 15.0) or (temp > 35.0)
        health_flags[f'sensor_{i}'] = not flag
        if not health_flags[f'sensor_{i}']:
            system_health = False

    # Unused data structure transformation (set operations)
    unique_categories = set()
    for temp in raw_readings:
        if temp < 20:
            unique_categories.add('cold')
        elif temp < 25:
            unique_categories.add('warm')
        else:
            unique_categories.add('hot')

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()