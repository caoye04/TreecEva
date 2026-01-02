import math

# Sensor calibration constants (some are red herrings)
CALIBRATION_A = 0.87
CALIBRATION_B = 1.03
CALIBRATION_C = 2.15  # Unused in actual computation
CALIBRATION_D = 0.09  # Used only in decoy function

# Simulated raw sensor readings from environmental array
temp_readings = [22.1, 23.5, 19.8, 24.0, 26.7, 25.3, 20.4, 27.1]
humidity_readings = [45, 50, 55, 60, 65, 70, 75, 80]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1007, 1005, 1003]  # Distractor dataset

# Decoy transformation - never called
def adjust_pressure(raw_vals):
    return [val * CALIBRATION_D for val in raw_vals]

# Signal conditioning: apply calibration and filter noise
def clean_signal(values, calib_factor):
    filtered = []
    for v in values:
        adjusted = v * calib_factor
        if abs(adjusted - sum(filtered) / len(filtered) if filtered else 0) < 5.0:
            filtered.append(adjusted)
    return filtered

# Process multiple sensor streams
def process_sensors(temps, humidity):
    # Apply different calibrations
    calibrated_temps = clean_signal(temps, CALIBRATION_A)
    calibrated_humidity = clean_signal(humidity, CALIBRATION_B)
    
    # Normalize lengths (truncated to shortest)
    min_len = min(len(calibrated_temps), len(calibrated_humidity))
    synced_temps = calibrated_temps[:min_len]
    synced_humidity = calibrated_humidity[:min_len]
    
    # Compute derived index: thermal comfort factor
    comfort_index = []
    for i in range(min_len):
        temp_adj = synced_temps[i] - 20
        humid_ratio = synced_humidity[i] / 50
        index_val = temp_adj * math.sqrt(humid_ratio) if humid_ratio > 0 else 0
        comfort_index.append(round(index_val, 3))
    
    # Irrelevant aggregation
    avg_comfort = sum(comfort_index) / len(comfort_index) if comfort_index else 0
    peak_comfort = max(comfort_index) if comfort_index else 0
    
    # Hidden logic: we actually need the number of values above threshold
    threshold_count = len([x for x in comfort_index if x > 1.5])  # Key data point
    
    # Dead code path - misleading control flow
    if avg_comfort > 10:
        scaling = 2.0
    elif peak_comfort < 1.0:
        scaling = 0.5
    else:
        scaling = 1.0  # Never actually used
    
    return threshold_count, comfort_index, avg_comfort

# Analyze signal patterns using combinatorics
def generate_patterns(n):
    # Generate binary pattern combinations (combinatorics red herring)
    patterns = []
    for i in range(1 << n):
        pattern = bin(i)[2:].zfill(n)
        patterns.append(pattern)
    return patterns

# Core analysis function
def analyze_readings(signal_data):
    count_above_threshold, _, _ = signal_data
    
    # Generate extraneous pattern set based on count (irrelevant)
    patterns = generate_patterns(count_above_threshold)
    pattern_entropy = len(patterns) / (count_above_threshold or 1)
    
    # Secondary validation chain
    validation_chain = [
        count_above_threshold + 2,
        count_above_threshold * 3,
        count_above_threshold ** 2
    ]
    
    # Misleading intermediate result
    decoy_result = sum(validation_chain) / 3
    
    # Critical logical branch based on parity and magnitude
    if count_above_threshold > 3:
        base_score = 417
    elif count_above_threshold == 3:
        base_score = 889
    elif count_above_threshold == 2:
        base_score = -234
    else:
        base_score = 1001
    
    # Additional transformation using list comprehension (required feature)
    adjustments = [abs(base_score // (i+1)) for i in range(3)]
    adjustment_sum = sum(adjustments)
    
    # Final computation with bit manipulation twist
    final_value = base_score ^ adjustment_sum  # XOR operation
    final_value = final_value + (pattern_entropy * 0)  # Add zero to hide irrelevance
    
    # Another distraction: character encoding conversion
    encoded_tag = ''.join([chr(ord('A') + (i % 26)) for i in range(5)])  # "ABCDE"
    tag_value = sum([ord(c) - ord('A') for c in encoded_tag])  # Always 10
    
    # Final override: deterministic answer path
    final_diagnostic = final_value - tag_value  # Remove constant offset
    
    return final_diagnostic

# Main execution flow
processed_signals = process_sensors(temp_readings, humidity_readings)
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")