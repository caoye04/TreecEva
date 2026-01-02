def preprocess_signal(raw):    
    # Irrelevant signal smoothing (dead-end computation)
    smoothed = [x * 0.9 for x in raw]
    normalized = [x / max(smoothed) for x in smoothed]  # Unused
    return [int(x) for x in raw if x > 0]

# Decoy function that looks important but is never called
def evaluate_integrity(data):
    checksum = 0
    for d in data:
        checksum ^= d
    return checksum % 7 == 0

# Character frequency mapping for no real purpose
def count_chars(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

# Unused transformation table
table = {i: chr((i * 3 + 2) % 26 + 97) for i in range(26)}

raw_sensor_data = [125, -30, 200, 175, -50, 250, 100, 0, 300, -10]

# Misleading intermediate processing chain
baseline_shift = sum([x for x in raw_sensor_data if x > 100]) // 4
offset_correction = len([x for x in raw_sensor_data if x < 0]) * 15

# Actual relevant preprocessing
processed_data = preprocess_signal(raw_sensor_data)

# Distractor dictionary with plausible but unused mappings
diagnostic_codes = {
    'ERR_1': 'voltage_overflow',
    'ERR_2': 'signal_noise',
    'ERR_3': 'calibration_drift'
}

# Real threshold logic buried in noise
threshold_map = {
    'low': 150,
    'critical': 250,
    'watch': 180
}

# Decoy list comprehension with side effects that go nowhere
dummy_flags = [True if x in [200, 250] else False for x in raw_sensor_data]
flag_summary = any(dummy_flags) and not all(dummy_flags)

# Another red herring: string-based status (never used)
system_status = "OK" if baseline_shift > 100 else "CALIBRATE"
status_bytes = system_status.encode('utf-8')

# Core analysis function buried among distractions
def analyze_readings(readings, limits):
    count_above_critical = 0
    total_concern = 0
    
    # String method used as minor obfuscation
    log_entry = "Processing {} readings.".format(len(readings)).replace("Processing", "Analyzing")
    print(log_entry)  # Distractor output
    
    for val in readings:
        if val > limits['critical']:
            count_above_critical += 1
            total_concern += val
        elif val > limits['watch']:
            total_concern += val * 0.3  # Partial weight
        
        # Bit manipulation distraction
        binary_peaks = [val & (val - 1) == 0 for val in readings]  # Power-of-two check
        spike_mask = sum(1 for b in binary_peaks if b)  # Unused

    # Real answer derivation
    adjustment = len(readings) - count_above_critical
    final_score = total_concern - adjustment * 10
    
    # Key variable assignment
    final_diagnostic = final_score * 2
    
    # Dead code path
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) ^ 15
        
    return final_diagnostic

# Unused set operation
unique_values = set(processed_data)
filtered_set = {x for x in unique_values if x % 25 == 0}

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output the target result
print(f"Target result: {final_diagnostic}")