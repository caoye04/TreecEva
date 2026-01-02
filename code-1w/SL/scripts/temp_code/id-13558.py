def process_sensor_array():
    # Simulated environmental sensor readings (temperature in tenths of °C)
    raw_readings = [234, 251, 198, 302, 276, 205, 244, 289, 263, 217, 234, 277, 258, 241, 229]
    
    # Calibration offset and noise floor (irrelevant for final result)
    calibration_factor = 1.02
    noise_floor = [x * calibration_factor for x in raw_readings]  # unused distraction
    adjusted_readings = [int(x * 0.98) for x in raw_readings]  # minor adjustment, some used later

    # Define critical thresholds as sets
    warning_thresholds = {250, 260, 270, 280, 290}
    error_thresholds = {300, 310, 320}
    combined_limits = warning_thresholds | error_thresholds | {245, 265}  # red herring set
    threshold_set = {t for t in warning_thresholds if t > 255}  # actual relevant set: {260, 270, 280, 290}

    # Historical anomaly log (distractor data structure)
    historical_anomalies = {
        '2023-04-01': [198],
        '2023-05-12': [302, 276],
        '2023-06-03': []
    }
    anomaly_count = sum(len(v) for v in historical_anomalies.values())  # irrelevant computation

    # Filter readings above dynamic baseline
    dynamic_baseline = 200 + len([x for x in raw_readings if x > 250]) * 3  # evaluates to 200 + 7*3 = 221
    filtered_data = [x for x in adjusted_readings if x > dynamic_baseline]

    # Secondary filter based on divisibility (misleading path)
    divisible_by_three = [x for x in filtered_data if x % 3 == 0]
    spike_magnitude = max(raw_readings) - min(raw_readings)  # 302 - 198 = 104, unused

    # Decoy function that's defined but not called
    def compute_variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)
    
    # Another decoy: complex transformation with no effect
    transformed = []
    for i, val in enumerate(adjusted_readings):
        if i % 4 == 0:
            transformed.append(val >> 2)
        elif i % 3 == 0:
            transformed.append(val << 1)
        else:
            transformed.append(val ^ 15)
    
    # Real analysis begins
    def analyze_readings(data, limits):
        count_in_limits = 0
        total_deviation = 0
        
        for reading in data:
            # Check proximity to threshold set
            for limit in limits:
                if abs(reading - limit) <= 5:
                    count_in_limits += 1
                    total_deviation += abs(reading - limit)
                    break  # only count once
            
        if count_in_limits == 0:
            return 0
            
        average_deviation = total_deviation / count_in_limits
        score = (count_in_limits * 100) - (average_deviation * 10)
        return int(score)

    # Misleading early exit check (never triggers due to data)
    if len(divisible_by_three) > 10:
        final_diagnostic = -1
        return final_diagnostic

    # Key statement
    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    
    # Additional red herring: bit manipulation chain
    checksum = 0
    for r in raw_readings:
        checksum ^= r
        checksum = (checksum << 1) & 0xFFFF
    # Checksum ends up being irrelevant
    
    # Final result output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture result
def main():
    return process_sensor_array()

result = main()