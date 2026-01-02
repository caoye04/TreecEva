import itertools

# Simulated sensor data stream with metadata
raw_readings = [187, 205, 193, 211, 179]
metadata_tags = ['A', 'B', 'C', 'D', 'E']

# Irrelevant calibration constants (distractors)
calib_a = 0.987
calib_b = 1.045
temp_offset = -2.3
voltage_ref = 3.3

# Misleading preprocessing path (dead code)
def legacy_normalize(x):
    return (x - min(raw_readings)) / (max(raw_readings) - min(raw_readings))

# Unused auxiliary function (decoy)
def validate_checksum(arr):
    xor_sum = 0
    for val in arr:
        xor_sum ^= val
    return xor_sum == 255

# Real processing begins here — complex pipeline with distractions
data_stream = list(itertools.chain.from_iterable(
    [(val << 1) + (i & 1) for i, val in enumerate(raw_readings)]
))

# Spurious transformation with no effect on final result
dummy_transform = list(map(lambda x: (x * calib_a + temp_offset) % 256, data_stream))

# Red herring: checksum-like computation that looks important but isn't used
decoys = [data_stream[i] ^ data_stream[-i-1] for i in range(len(data_stream))]
checksum_guess = sum(decoys) & 0xFF

# Key intermediate: filter and fold using bitwise logic and integer division
filtered = [x for x in data_stream if x > 200 and (x & 3) == 1]
folded = 0
for val in filtered:
    folded = (folded * 3 + (val ^ 42)) // 2

# Distracting use of tuples and dictionary packing (mostly irrelevant)
sensor_bundle = {
    tag: (raw_readings[i], raw_readings[i] * 2 + 100) 
    for i, tag in enumerate(metadata_tags)
}
summary_stats = {
    'count': len(raw_readings),
    'peak': max(raw_readings),
    'adjusted_peak': (max(raw_readings) << 2) // 3,
    'phantom_metric': checksum_guess
}

# Another decoy function that looks like it's part of the chain
def enhance_signal(seq):
    return [x | 0b1100 for x in seq if x % 4 == 0]

# Actual core logic wrapped in lambda (required feature)
apply_correction = lambda x: (x + 17) & 0xFFFF

# Critical processing pipeline
shifted = [apply_correction(val) for val in filtered]
combined = 0
for i, val in enumerate(shifted):
    combined += val * (i + 1)

# Final computation with multiple concepts: bit ops, integer math, folding
intermediate = (combined ^ 0xAAAA) & 0xFFFF
final_output = (intermediate + (intermediate >> 4)) // 3

# Output the required result
print(f"Result: {final_output}")