def analyze_pattern(sequence):
    if len(sequence) < 5:
        return False
    sorted_seq = sorted(sequence)
    range_val = sorted_seq[-1] - sorted_seq[0]
    avg = sum(sequence) / len(sequence)
    variance = sum((x - avg) ** 2 for x in sequence) / len(sequence)
    return variance < 100 and range_val > 5

# Irrelevant helper function (decoy)
def validate_checksum(data_str):
    checksum = 0
    for char in data_str.upper():
        if char.isalpha():
            checksum += ord(char) - ord('A') + 1
        elif char.isdigit():
            checksum += int(char)
    return checksum % 17 == 0

# Unused transformation map (distractor)
transformation_rules = {
    'A': lambda x: x * 2,
    'B': lambda x: x + 10,
    'C': lambda x: x ** 1.5
}

# Simulated sensor data with red herring fields
current_readings = [23, 45, 67, 89, 12, 34, 56]
backup_buffer = [x * 1.1 for x in current_readings if x > 30]  # unused path
temp_snapshot = [x for x in current_readings if x % 2 == 0]

# Misleading intermediate calculation (dead code)
aggregated_power = sum(x ** 2 for x in temp_snapshot) // len(temp_snapshot) if temp_snapshot else 0

# Core diagnostic logic
baseline_profile = {k: v * 0.85 for k, v in enumerate([25, 40, 60, 80, 15, 30, 50])}
drift_analysis = [current_readings[i] - baseline_profile[i] for i in range(len(current_readings))]

# Bit manipulation decoy (irrelevant)
bit_flags = 0
for val in drift_analysis:
    if val > 10:
        bit_flags |= (1 << (int(val) % 8))

# String-based control flag (red herring)
diagnostic_mode = "CALIBRATE_HIGH"
if diagnostic_mode.lower().startswith("calibrate"):
    mode_factor = 1.2
else:
    mode_factor = 1.0

# Unused sorting path
sorted_drift = sorted(drift_analysis, key=lambda x: abs(x), reverse=True)
trimmed_values = sorted_drift[2:-2]  # partial usage distraction

# Primary signal extraction
signal_strength = sum(abs(x) for x in drift_analysis if abs(x) > 5) * mode_factor

# Decoy set operations
reference_set = set(range(10, 100, 7))
candidate_pool = set(int(x) for x in backup_buffer)
overlap_score = len(reference_set & candidate_pool)  # calculated but not used directly

# Threshold logic with case conversion red herring
event_flag = "CRITICAL" if signal_strength > 120 else "NORMAL"
flag_code = event_flag.lower().replace("critical", "alert").upper()

# Mapping for actual computation
threshold_map = {
    'low': 30,
    'medium': 65,
    'high': signal_strength * 0.3
}

# Complex data structure (tuple unpacking + distractor)
health_signature = (
    sum(drift_analysis),
    len([x for x in drift_analysis if x > 0]),
    max(drift_analysis),
    min(drift_analysis)
)

primary, active_count, peak, trough = health_signature

# Secondary derived metric (not used in final result)
stability_index = (active_count / len(drift_analysis)) * 100 if drift_analysis else 0

# Main processing function
def process_metrics(signature, thresholds):
    net_drift, count_pos, high_peak, low_trough = signature
    
    # Irrelevant string formatting
    report_id = f"DIAG-{{:04d}}".format(int(signal_strength) % 9999)
    timestamp_tag = "2023-XR".lower().replace("x", "M")
    
    # Distractor: set difference
    dormant_range = set(range(int(low_trough), int(high_peak)))
    prime_band = set(range(0, 50))
    suppression_zone = dormant_range - prime_band
    
    # Real logic masked by noise
    base_score = abs(net_drift)
    if count_pos > 3:
        base_score *= 1.25
    if abs(high_peak - abs(low_trough)) > 40:
        base_score += 15
    
    # Critical dependency on earlier mode_factor
    adjustment = thresholds['high'] - thresholds['low']
    final_score = base_score * (adjustment / 50.0)
    
    # Final obfuscation via string method chain
    config_key = ("mode_" + flag_code.lower() + "_end").strip("_end").upper()
    
    # Actual answer derivation
    if config_key == "MODE_ALERT":
        final_score += 10
    
    return int(final_score)

# Execution point of interest
final_diagnostic = process_metrics(health_signature, threshold_map)
print(f"Result: {final_diagnostic}")