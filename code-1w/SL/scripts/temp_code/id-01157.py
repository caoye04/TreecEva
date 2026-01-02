def analyze_sensor_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count_peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count_peaks += 1
    return count_peaks

# Simulated environmental sensor readings
temperature_readings = [23.5, 24.1, 25.6, 25.2, 26.8, 27.3, 27.1, 26.9, 28.0, 28.2, 27.9]
humidity_readings = [45, 47, 52, 55, 53, 50, 48, 49, 54, 56, 55]
pressure_readings = [1013, 1015, 1014, 1016, 1018, 1017, 1015, 1014, 1013, 1012, 1011]

# Irrelevant transformation - red herring
decoded_signal = ''.join([chr(int(x) % 127) for x in pressure_readings])
checksum = sum(ord(c) for c in decoded_signal) % 1000

# Misleading peak detection on wrong data
false_peak_count = analyze_sensor_pattern(humidity_readings)

# Data alignment and filtering based on temperature thresholds
operational_threshold = 25.0
filtered_data = [temp for temp in temperature_readings if temp >= operational_threshold]

# Dummy sorting with no effect (distractor)
sorted_copy = sorted(filtered_data)
sorted_copy.reverse()  # Unused reversed list

# Auxiliary calculation: average rate of change (not used in final result)
rate_of_change = []
for i in range(1, len(filtered_data)):
    rate_of_change.append(round(filtered_data[i] - filtered_data[i-1], 2))

# Simulate diagnostic code from string signature (string method usage)
diag_code = "ERR_TEMP_FLUCT_01"
if diag_code.startswith("ERR") and "TEMP" in diag_code:
    error_severity = len(diag_code.split('_'))
    correction_factor = error_severity * 0.5
else:
    correction_factor = 1.0

# Real processing function
def process_readings(data, base_threshold):
    if not data:
        return 0
    
    # Compute moving average of window size 2
    moving_avg = []
    for i in range(len(data) - 1):
        moving_avg.append((data[i] + data[i+1]) / 2)
    
    # Count how many averages are above threshold + dynamic offset
    adaptive_offset = 0.8 if len(moving_avg) > 5 else 0.3
    trigger_level = base_threshold + adaptive_offset
    
    triggered = 0
    for avg in moving_avg:
        if avg > trigger_level:
            triggered += 1
    
    # Apply spurious correction based on string length (decoy logic)
    tag = "CALIBRATED"
    adjustment = len(tag.lower().replace('a', ''))  # Returns 7, irrelevant
    
    # Final computation independent of adjustment
    raw_score = triggered * 100
    penalty = abs(len(data) - len(moving_avg)) * 10  # Always 10
    return raw_score - penalty

# Dead code path - never executed but looks important
def legacy_diagnosis(arr):
    total = 0
    for x in arr:
        total += x ** 0.5
    return int(total) // 3

# Unused intermediate variables to distract
baseline_shift = sum(filtered_data) / len(filtered_data) - min(temperature_readings)
outlier_count = sum(1 for x in temperature_readings if abs(x - baseline_shift) > 3)

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold=operational_threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")