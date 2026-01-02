def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append('up')
            count += 1
        elif sequence[i] < sequence[i-1]:
            trend.append('down')
    # Irrelevant transformation
    reversed_trend = [x[::-1] for x in trend]
    return count

# Simulate sensor data drift (distractor)
def apply_calibration(data, factor=1.03):
    calibrated = []
    for val in data:
        adjusted = val * factor
        if adjusted > 100:
            adjusted = 95  # artificial cap
        calibrated.append(adjusted)
    return calibrated

# Main processing function
def process_temperatures(raw_data, threshold):
    # Step 1: Filter out temperatures below threshold
    high_temps = [t for t in raw_data if t >= threshold]
    
    # Step 2: Track state with auxiliary variables
    temp_stats = {
        'sum': 0,
        'count': 0,
        'peaks': []
    }
    
    # Step 3: Accumulate stats and detect peaks
    for i, temp in enumerate(high_temps):
        temp_stats['sum'] += temp
        temp_stats['count'] += 1
        if i > 0 and i < len(high_temps) - 1:
            if high_temps[i] > high_temps[i-1] and high_temps[i] > high_temps[i+1]:
                temp_stats['peaks'].append(temp)
    
    # Step 4: Compute average (used later)
    avg_high_temp = temp_stats['sum'] / temp_stats['count'] if temp_stats['count'] > 0 else 0
    
    # Distractor: unused peak analysis
    peak_set = set(temp_stats['peaks'])
    unique_peak_count = len(peak_set)
    sorted_peaks = sorted(peak_set, reverse=True)
    
    # Step 5: Analyze original sequence pattern (partial red herring)
    dummy_sequence = [10, 15, 13, 18, 16]
    pattern_score = analyze_pattern(dummy_sequence)
    
    # Step 6: Apply fake calibration to unrelated copy (dead computation)
    calibrated_copy = apply_calibration(raw_data)
    avg_calibrated = sum(calibrated_copy) / len(calibrated_copy)
    
    # Step 7: Final output depends only on average of high temps and fixed offset
    adjustment = 5 if avg_calibrated > 30 else 2  # never triggered due to data
    final_output = int(avg_high_temp + adjustment - 10)
    
    return final_output

# Input data
sensor_readings = [20, 23, 27, 24, 30, 28, 26, 33, 31, 29, 22]

# Execute main logic
temperature_data = sensor_readings.copy()
final_output = process_temperatures(temperature_data, threshold=25)
print(f"Result: {final_output}")