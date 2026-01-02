import math

# Simulated sensor array data from environmental monitoring station
def collect_sensor_data():
    raw_values = [23.4, 19.5, 20.1, 18.8, 25.6, 22.3, 17.9, 20.0]
    calibration_offset = 1.2
    adjusted = [v + calibration_offset for v in raw_values]
    return adjusted

# Signal processing pipeline
def filter_noise(readings):
    threshold = 21.0
    filtered = [r for r in readings if r > threshold]
    normalization_factor = 0.95
    normalized = [f * normalization_factor for f in filtered]
    return normalized

# Legacy function - unused but looks relevant (red herring)
def legacy_calculate_average(data):
    total = 0
    count = 0
    for item in data:
        if item > 0:
            total += item
            count += 1
    if count == 0:
        return 0
    return total / count

# Misleading diagnostic with decoy logic
def false_diagnosis(signal):
    if len(signal) == 0:
        return -999
    peak = max(signal)
    if peak > 25:
        return 1  # Anomalous
    else:
        return 0  # Normal

# Core analysis logic
def process_critical_path(data):
    squared_devs = [(x - 20.5) ** 2 for x in data]
    mean_squared = sum(squared_devs) / len(squared_devs)
    rmse = math.sqrt(mean_squared)
    return int(rmse * 100)

# Secondary transformation with distractor variables
def transform_sequence(arr):
    result = []
    shift_key = 3
    mask = 0b1111
    for i, val in enumerate(arr):
        transformed = (int(val * 10) ^ i) & mask
        result.append(transformed)
    # Distractor: unused computation
    checksum = sum(result) % 17
    extra_calc = [r + 5 for r in result if r < 10]
    return result

# Main processing chain
def analyze_readings(signals):
    if not signals:
        return -1
    
    # Key processing step
    base_score = sum(int(s) for s in signals)
    
    # Red herring conditional (never triggers in this input)
    emergency_override = False
    if base_score < 0:
        emergency_override = True
        return -9999
    
    # Real computation path
    adjustment = 0
    for s in signals:
        if s > 22.0:
            adjustment += 1
    
    # Decoy bit manipulation
    flag_register = 0b1010
    temp_flag = flag_register | 0b0101
    temp_flag = temp_flag ^ 0b1111
    
    # Actual contribution to answer
    adjustment *= 100
    
    # Complex distraction: nested list comprehension with unused result
    grid_analysis = [[(i*j + adjustment) % 2 for j in range(3)] for i in range(4)]
    flat_grid = [item for row in grid_analysis for item in row]
    grid_sum = sum(flat_grid)
    
    # Final determination
    final_value = base_score + adjustment
    return final_value

# Unused helper (distractor)
def validate_checksum(data, expected):
    actual = sum(data) % 256
    return actual == expected

# Execution flow
if __name__ == "__main__":
    # Step 1: Collect data
    raw_sensor_data = collect_sensor_data()  # [24.6, 20.7, 21.3, 20.0, 26.8, 23.5, 19.1, 21.2]
    
    # Step 2: Filter signals
    processed_signals = filter_noise(raw_sensor_data)  # Only values > 21.0: [24.6, 21.3, 26.8, 23.5, 21.2]
    
    # Step 3: Transform (result used indirectly via side-effect on focus)
    transformed = transform_sequence(processed_signals)
    
    # Step 4: Run legacy check (unused result - distraction)
    average_reading = legacy_calculate_average(processed_signals)
    
    # Step 5: Run false diagnosis (ignored result)
    diagnosis_code = false_diagnosis(processed_signals)
    
    # Step 6: Process critical path (contributes to understanding but not direct)
    critical_metric = process_critical_path(processed_signals)
    
    # Step 7: Main analysis
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")