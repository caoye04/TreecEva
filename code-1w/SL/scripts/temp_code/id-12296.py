from collections import defaultdict
import math

# Simulated sensor data with noise and metadata
data_stream = ["85A", "92B", "76C", "101D", "44E", "115F", "67G", "99H", "103I", "88J"]
raw_offsets = [3, -7, 5, 0, -2, 8, -4, 1, 6, -3]
calibration_keys = ['k1', 'k3', 'k2', 'k5', 'k4']

# Irrelevant lookup table (red herring)
symbol_lookup = {'A': 1, 'B': 2, 'C': 3, 'X': 99, 'Y': 100}

# Distractor: unused function
def decrypt_key(key):
    return sum([ord(c) for c in key]) % 17

# Distractor: dead code path
if len(calibration_keys) > 10:
    final_offset = max(raw_offsets)
else:
    final_offset = 0  # Not actually used in main logic

# Real processing begins here
processed_data = []
for i, entry in enumerate(data_stream):
    numeric_part = int(entry[:2])
    flag_char = entry[2]
    
    # Apply offset modulation (real but disguised)
    adjusted_value = numeric_part + raw_offsets[i % len(raw_offsets)]
    
    # Bit manipulation for signal integrity check (relevant)
    binary_rep = bin(adjusted_value)[2:]
    parity_bit = binary_rep.count('1') % 2
    
    # Only include entries where parity is odd (filtering rule)
    if parity_bit == 1:
        processed_data.append(adjusted_value)

# Threshold map using defaultdict (required python feature)
threshold_map = defaultdict(lambda: 100)
threshold_map.update({
    'low': 75,
    'medium': 85,
    'high': 95
})

# Decoy dictionary with misleading thresholds
temp_thresholds = {
    'safe': 70,
    'warning': 90,
    'critical': 110
}

# Unused intermediate calculation (distractor)
avg_temp = sum([x for x in raw_offsets if x > 0]) / len([x for x in raw_offsets if x > 0])

# String-based switch configuration (irrelevant but plausible)
config_mode = "diagnostic_active"
mode_flags = config_mode.split('_')
if 'active' in mode_flags:
    activation_level = len(mode_flags)
else:
    activation_level = 1

# Core analysis function with nested logic
def analyze_signal(data, thresholds):
    count_high = 0
    cumulative_score = 0
    
    for val in data:
        # Multiple comparison layers (boolean logic)
        if val > thresholds['medium']:
            count_high += 1
            
        # Modular arithmetic pattern detection
        mod_group = val % 7
        if mod_group in [2, 3, 5]:
            cumulative_score += int(math.sqrt(val))
        elif mod_group == 0:
            cumulative_score -= val // 10
            
        # Logical short-circuit trap (misleading)
        if val > thresholds['high'] and val < 110 or (val > 120 and val % 2 == 0):
            cumulative_score += 5
    
    # Conditional branch with early exit red herring
    if count_high == 0:
        return -1 * cumulative_score
    
    # Final transformation using string method (required feature)
    tag = f"{count_high}{cumulative_score}".upper().replace("0", "X")
    checksum = sum(ord(c) for c in tag if c != 'X')
    
    # Actual answer computation
    result = (cumulative_score * count_high) - (checksum % 19)
    
    return result

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")