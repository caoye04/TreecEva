def analyze_pattern(seq):
    # Irrelevant transformation
    reversed_seq = [x * 1.5 for x in seq[::-1]]
    norm = sum(x**2 for x in seq) ** 0.5
    normalized = [x / norm for x in seq]
    return [int(x * 100) for x in normalized]

# Decoy data structures
decoys = {
    'phantom_score': [0.1, 0.3, 0.5],
    'ghost_weights': (999, 888, 777),
    'fake_flags': True
}

# Real input sequence - disguised as a health metric log
health_log = [
    64, 32, 16, 8, 4, 2, 1  # Powers of 2 descending
]

# Unused but plausible-looking processing function
def deprecated_filter(data):
    return [x for x in data if x > 10]

# Threshold configuration with red herring entries
threshold_map = {
    'alert_level': 25,
    'caution_floor': 8,
    'ignore_below': 0,  # Distractor: not used in logic
    'overclock_penalty': 1.7  # Misleading parameter
}

# Bit manipulation decoy - looks important but unused
bitmask = 0b11110000 & 0b10101010
bitmask |= 0b01000000

# String method used per requirement - processes dummy ID
device_id = "sensor-array-X25"
encoded_tag = device_id.upper().replace("-", "_").split('_')
version_code = int(encoded_tag[-1][1:])  # Extracts 25 from X25

# Auxiliary counting function with plausible but irrelevant logic
def count_transitions(data):
    count = 0
    for i in range(1, len(data)):
        if (data[i] - data[i-1]) > 0:
            count += 1
    return count

# Primary data transformation chain
base_shift = [x << 1 for x in health_log]  # Left shift all by 1 (×2)
filtered_data = [x for x in base_shift if x > 10]  # Filter post-shift

# Simulate diagnostic flags using XOR on positional bits
diag_flags = 0
for i, val in enumerate(filtered_data):
    if val % 16 == 0:
        diag_flags ^= (i + 1)  # XOR position+1 when divisible by 16

# Create tuple unpacking scenario (partially relevant)
primary_metric, *secondary_slice = filtered_data

# Secondary analysis - average of high-magnitude values
high_vals = [x for x in filtered_data if x >= 32]
avg_high = sum(high_vals) / len(high_vals) if high_vals else 0

# Control flow with short-circuit evaluation
critical_alert = False
if avg_high > 40 and diag_flags & 1 and (len(secondary_slice) > 2 or True):
    critical_alert = (diag_flags % 3) == 0

# Real processing function - answer path
def process_metrics(seq, thresholds):
    temp_result = 0
    alert_trigger = thresholds['alert_level']
    caution_trigger = thresholds['caution_floor']
    
    for i, val in enumerate(seq):
        if val >= alert_trigger:
            temp_result += val >> 2  # Divide by 4 using bit shift
        elif val >= caution_trigger:
            temp_result += val // 3
        else:
            temp_result -= val  # Penalty
    
    # Final adjustment based on pattern length parity
    if len(seq) % 2 == 1:
        temp_result = (temp_result ^ 0xFF) + 10  # Bitwise obfuscation
    
    return temp_result

# Execute main computation
intermediate_signal = analyze_pattern(health_log)

# Key statement
final_diagnostic = process_metrics(health_sequence=filtered_data, threshold_map=threshold_map)

print(f"Result: {final_diagnostic}")