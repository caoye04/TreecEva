import math

# Irrelevant helper function (decoy)
def dummy_transform(data):
    return [x ** 0.5 for x in data if x > 5]

# Unused but plausible-looking diagnostic function
def diagnose_system_health(logs):
    severity = 0
    for log in logs:
        if 'ERROR' in log:
            severity += 3
        elif 'WARN' in log:
            severity += 1
    return severity

# Core calculation with distractors
network_load = [12, 8, 15, 22, 7, 11]
phase_shift = 0.67
baseline_offset = 9.81  # Red herring: looks scientific but unused

# Distractor variables
temp_cache = {i: val ** 2 for i, val in enumerate(network_load)}
scaling_matrix = [[1.1, 0.9], [0.8, 1.2]]

# Another decoy: complex but unused computation
aggregated_diagnostic = sum((val - 10) ** 2 for val in network_load if val % 2 == 0)

# Real logic begins — linear search for threshold breach
breach_index = -1
for i, load in enumerate(network_load):
    if load > 20:
        breach_index = i
        break

# Bit manipulation red herring
obfuscation_key = 0b1101 ^ 0b1011
encoded_phase = phase_shift * (obfuscation_key << 2)

# Conditional branch with misleading intermediate
if breach_index >= 0:
    adjustment_factor = 1.75
else:
    adjustment_factor = 1.25  # Dead path — not taken

# Lambda-based transformation (core concept)
calculate_efficiency = lambda loads, shift: (
    sum(math.sin(shift * x) for x in loads) / len(loads)
)

# Scalar derived from bit count (distractor but used)
bit_population = bin(obfuscation_key).count('1')
scalar_factor = bit_population * 10  # = 3 * 10 = 30

# Key statement — target of question
thermal_capacity = calculate_efficiency(network_load, phase_shift) * scalar_factor

# Unrelated logging output (misleading)
system_log = "CALC_COMPLETE" if thermal_capacity > 0 else "CALC_FAILED"

# Final result print (required format)
print(f"Result: {thermal_capacity}")