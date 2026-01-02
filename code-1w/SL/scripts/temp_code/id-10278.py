import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
NOISE_FLOOR = 0.0017
REFERENCE_VOLTAGE = 3.3

# Simulated raw sensor cluster readings (some are decoys)
raw_readings = [85, 170, 255, 0, 128, 64, 192, 32]
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
label_map = {k: v for k, v in zip(range(8), dummy_labels)}

# Irrelevant transformation - string manipulation red herring
mapped_names = [f'Sensor_{lbl}_Node' for lbl in dummy_labels]
joined_names = '-'.join(mapped_names).lower()
title_case_names = joined_names.title()

# Real signal processing begins
threshold = 127
categorized = {'strong': [], 'weak': []}

for val in raw_readings:
    if val > threshold:
        categorized['strong'].append(val)
    else:
        categorized['weak'].append(val)

# Bit manipulation stage (only strong signals matter)
processed_signals = []
for s in categorized['strong']:
    # Apply bit flip on lower nibble and scale by 0.5
    flipped = s ^ 0b1111  # XOR with 15
    scaled = flipped / 2
    processed_signals.append(int(scaled))

# Decoy set operations (distraction)
signal_set_a = set(categorized['strong'])
signal_set_b = set(categorized['weak'])
signal_union = signal_set_a | signal_set_b
signal_intersection = signal_set_a & signal_set_b
symmetric_diff = signal_set_a ^ signal_set_b  # unused
excluded_zones = signal_union - signal_intersection

# Unused function - dead code path
def compute_entropy(data):
    total = sum(data)
    probs = [d / total for d in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Another decoy: floating point accumulation with no effect
accumulated_drift = 0.0
for i in range(len(raw_readings)):
    accumulated_drift += NOISE_FLOOR * (i + 1) * CALIBRATION_OFFSET
adjusted_drift = accumulated_drift * REFERENCE_VOLTAGE

# Real analysis function
def analyze_readings(signals):
    # Nested logic with conditional branches
    if len(signals) == 0:
        return -1
    
    base_value = 0
    for s in signals:
        if s % 2 == 0:
            base_value += s ** 2
        else:
            base_value -= s  # rare case, but possible
    
    # Additional transformation: sum of digits in hex representation
    hex_sum = 0
    for s in signals:
        hex_str = hex(s)[2:]  # remove '0x'
        for char in hex_str:
            if char.isdigit():
                hex_sum += int(char)
            else:
                hex_sum += ord(char) - ord('a') + 10
    
    # Combine results using integer division and bitwise OR
    intermediate = abs(base_value) // 10
    combined = (intermediate | hex_sum) & 0xFFFF  # clamp to 16 bits
    
    # Final adjustment based on list length (tuple unpacking used)
    modifiers = (3, 7)
    factor_a, factor_b = modifiers
    if len(signals) > 3:
        final_score = combined * factor_a - factor_b
    else:
        final_score = combined * factor_b + factor_a
    
    return final_score

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")