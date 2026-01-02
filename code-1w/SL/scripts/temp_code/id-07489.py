import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 3) + sum([i * 2 for i in range(5)])

# Misleading precomputed values (distractors)
baseline_offset = 187
legacy_threshold = 4.67
placeholder_cache = {i: i * 1.5 for i in range(10)}

# Core system parameters
scaling_factor = 2.5
tolerance_band = 0.01

# Simulated sensor inputs (mixed data types)
sensor_a = [12, 15, 14, 18, 20]
sensor_b = [8, 10, 13, 11, 9]

# Red herring: complex-looking but unused transformation
decoyness = list(map(lambda x: (x + scaling_factor) ** 2 % 7, range(6)))

# Activation sequence with embedded logic flags
activation_sequence = [
    {'flag': True, 'power': 3, 'mode': 'A'},
    {'flag': False, 'power': 5, 'mode': 'B'},
    {'flag': True, 'power': 2, 'mode': 'A'},
    {'flag': True, 'power': 4, 'mode': 'C'}
]

# Kernel logic with conditional weightings
logic_kernel = lambda x, y: (x + y) * scaling_factor if x > y else (x - y) * tolerance_band

# Auxiliary calculation (unused but plausible)
intermediate_fusion = sum([a * b for a, b in zip(sensor_a, sensor_b)]) / len(sensor_a)

# Conditional bitmask simulation (irrelevant)
bitmask_probe = 0
for i in range(3):
    bitmask_probe |= (1 << i)

# Real processing begins here — nested logic with distractors
aggregated_weights = 0
valid_modes = set()

for entry in activation_sequence:
    if entry['flag']:
        # Weighted contribution based on power and mode
        weight = entry['power']
        if entry['mode'] == 'A':
            weight *= 1.2
        elif entry['mode'] == 'B':
            weight *= 0.8
        else:
            weight *= 1.5  # Mode C or others
        aggregated_weights += weight
        valid_modes.add(entry['mode'])

# Decoy list comprehension with side effect-like appearance
echo_buffer = [math.log(w + 1) for w in sensor_a if w > 14]

# Simulated historical context (misleading)
historical_bias = 0
for _ in range(2):
    historical_bias += legacy_threshold * 0.5

# Key computation: entropy adjustment based on unique modes
mode_entropy = len(valid_modes) * 3.7

# Secondary adjustment: use lambda kernel on two fixed derived values
adjusted_metric = logic_kernel(aggregated_weights, len(activation_sequence))

# Final diagnostic computed from multiple reasoning steps
final_diagnostic = int(round((adjusted_metric + mode_entropy) * 1.1))

# Dead code: looks important but unused
consistency_check = final_diagnostic % 2 == 0

# Print result as required
print(f"Target result: {final_diagnostic}")