from itertools import combinations, cycle

# Environmental monitoring system for water treatment plant
base_readings = [127, 255, 193, 64, 95, 128, 230]
threshold = 128
temperature_offset = 0.87
pressure_factor = 1.03
calibration_sequence = (17, 23, 19, 29, 31)

# Irrelevant transformation chain 1: spectral analysis red herring
dummy_spectral = [(x >> 2) ^ 15 for x in base_readings if x % 3 != 0]
spectral_weight = sum(dummy_spectral) / len(dummy_spectral) if dummy_spectral else 0
adjusted_weights = [w * spectral_weight for w in [0.1, 0.3, 0.2] * 3]

# Decoy function: looks important but unused
def calculate_turbidity_index(readings):
    return sum(r & 0x0F for r in readings) / len(readings)

# Simulated sensor drift compensation (irrelevant)
corrected_readings = []
for i, val in enumerate(base_readings):
    corrected = val
    if i % 2 == 0:
        corrected = (val + calibration_sequence[i % 5]) % 256
    if corrected > 200:
        corrected = corrected >> 1
    corrected_readings.append(corrected)

# Real processing begins here
high_range = [x for x in base_readings if x >= threshold]
low_range = [x for x in base_readings if x < threshold]

# Bit manipulation for diagnostic signature
signature = 0
for val in high_range:
    signature ^= (val << 1) | (val >> 7)

# Generate all possible two-sensor pairs for redundancy check (unused result)
pair_combinations = list(combinations(base_readings, 2))
redundancy_metric = sum((a & b) for a, b in pair_combinations[:10]) if pair_combinations else 0

# Critical path: filtration efficiency analysis
diagnostic_flag = False
process_efficiency = 0.0
compliance_ratio = 1.0

if len(high_range) > 3:
    raw_efficiency = len(high_range) / len(base_readings)
    adjustment_cycle = cycle([0.95, 1.05, 1.1])
    adjusted_efficiency = raw_efficiency
n    for i, adj in enumerate(adjustment_cycle):
        if i >= 3:
            break
        adjusted_efficiency *= adj
    
    # Early termination based on bit condition
    if signature & 0x01:
        process_efficiency = adjusted_efficiency * 0.88
        diagnostic_flag = True
        break  # Exit loop early - this executes
    else:
        process_efficiency = adjusted_efficiency
else:
    process_efficiency = 0.5

# Compliance calculation with string-based rule encoding (distractor layer)
rules_encoded = 'AABBCAC'
rule_weights = {'A': 1.0, 'B': 0.8, 'C': 0.6}
encoded_value = 0
for char in rules_encoded:
    encoded_value += ord(char.lower()) ^ 3

# Actual compliance logic
active_rules = 5
max_rules = 7
compliance_ratio = active_rules / max_rules

# Key statement
filtration_score = process_efficiency * compliance_ratio

# Post-processing decoy
if filtration_score > 0.5:
    temp_buffer = bytearray(filtration_score.to_bytes(4, 'little'))
    for i in range(len(temp_buffer)):
        temp_buffer[i] ^= 0xAA

# Output target variable
print(f"Result: {filtration_score}")