import itertools

# Simulate a network packet validation and transformation pipeline
packet_data = [17, 23, 45, 67, 89, 12, 34, 56, 78, 90]
key_offset = 13
modulus = 1009
scramble_mask = 0b110101
noise_floor = 42

# Irrelevant noise: frequency drift simulation (unused)
frequency_drift = []
for i in range(len(packet_data)):
    frequency_drift.append((i * 7 + 11) % 19)

# Distractor: signal strength estimation (not used in final result)
signal_strength = sum([x ** 0.5 for x in packet_data if x > 30])
avg_signal = signal_strength / len(packet_data)

# Step 1: Apply offset shift with modular arithmetic
temp_shifted = [(x + key_offset) % modulus for x in packet_data]

# Step 2: Filter out values above threshold (simulating signal clipping)
clipped = [x for x in temp_shifted if x < 85]

# Step 3: Generate all possible 3-element subsequences to simulate pattern sniffing
subsequences = list(itertools.combinations(clipped, 3))
pattern_count = len(subsequences)

# Step 4: Compute XOR fingerprint of clipped data
fingerprint = 0
for val in clipped:
    fingerprint ^= (val * 3) & 0xFF

# Step 5: Find symmetric pairs (mirrored values around center)
symmetric_pairs = []
center = len(clipped) // 2
for i in range(center):
    symmetric_pairs.append(clipped[i] + clipped[-(i+1)])

# Step 6: Accumulate valid sequence sum using only even-indexed clipped values
valid_sequence_sum = sum(clipped[i] for i in range(0, len(clipped), 2))

# Step 7: Derive adjustment factor using bitwise manipulation of fingerprint
adjustment = (fingerprint << 1) ^ scramble_mask
adjustment = (adjustment + pattern_count) % modulus

# Step 8: Final checksum computation — THIS IS THE KEY STATEMENT
checksum = (valid_sequence_sum + adjustment) % modulus

# Red herring: attempt to decode as ASCII (irrelevant)
decoded_chars = []
for x in clipped:
    if 32 <= x <= 126:
        decoded_chars.append(chr(x))
message_guess = ''.join(decoded_chars)

# Another decoy: entropy approximation (unused)
from math import log2
if pattern_count > 0:
    entropy = log2(pattern_count)

# Misleading intermediate: weighted average with arbitrary coefficients (unused)
weights = [0.1, 0.2, 0.4, 0.2, 0.1]
weighted_avg = sum(w * x for w, x in zip(weights, clipped[:5])) if len(clipped) >= 5 else 0

# Final output
Result: {checksum}