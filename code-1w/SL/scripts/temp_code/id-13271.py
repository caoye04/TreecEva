from itertools import compress, cycle
import math

# Simulated sensor readings with noise
raw_readings = [15, -8, 22, 0, -3, 44, 13, 7, -1, 9, 33, 2, 0, 6]

# Noise thresholds (irrelevant for final result but looks important)
top_threshold = 40
dynamic_floor = lambda x: x // 4

# Filter valid readings above dynamic floor (only values > 0 are kept)
filtered_data = [x for x in raw_readings if x > dynamic_floor(8)]

# Irrelevant transformation chain (dead path)
shadow_buffer = list(map(lambda x: x * 1.5, raw_readings))
scaled_noise = [round(x, 1) for x in shadow_buffer if x < 30]
baseline_shift = sum(scaled_noise[:5]) / len(scaled_noise[:5]) if scaled_noise else 0

# Decoy checksum using irrelevant data
legacy_checksum = 0
for i, val in enumerate(scaled_noise):
    legacy_checksum ^= int(val) % 17

# Control sequence mask (misleading use of itertools)
activation_pattern = list(compress(range(len(raw_readings)), cycle([1, 0, 1])))
trigger_indices = [i for i in activation_pattern if i < len(filtered_data)]

# Unused recursive function (red herring)
def compute_entropy(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0.0
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid+1:]
    return math.log(abs(seq[mid]) + 1) + compute_entropy(left, depth+1)

# Real processing begins: apply modulo wrap on filtered data
wrapped_data = [x % 13 for x in filtered_data]

# Bit manipulation layer (some steps are relevant)
bitwise_stack = 0
for val in wrapped_data:
    bitwise_stack ^= (val << 1) | (val >> 2)

# Finalize function (key component)
definalize(x):
    return (x * 31) ^ 997

# Secondary filter based on parity (redundant but looks critical)
even_emphasis = [x for x in filtered_data if x % 2 == 0]
odd_suppress = [x for x in filtered_data if x % 2 == 1 and x > 5]

# Critical statement: sum filtered_data (positive non-zero), then finalize
checksum = finalize(sum(filtered_data))

# More decoys
audit_trail = []
for idx, val in enumerate(zip(even_emphasis, odd_suppress + [0])):
    audit_trail.append(idx * val[0] - val[1])

# Output the target result
print(f"Result: {checksum}")