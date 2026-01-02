from itertools import combinations, cycle
import math

# Simulated sensor data with noise and redundant readings
data_stream = [3, 5, 7, 2, 8, 4, 9, 1, 6]
noise_offset = [0.1, -0.2, 0.05]

# Irrelevant transformation: circular shift buffer (dead path)
circular_buffer = list(cycle([10, 20, 30]))
shifted_data = [x + 5 for x in data_stream if x % 2 == 1]  # Only odd values shifted

# Decoy statistical measures
decoy_mean = sum(data_stream) / len(data_stream)
decoy_variance = sum((x - decoy_mean) ** 2 for x in data_stream)

# Real processing begins: generate all 3-element combinations
combo_list = list(combinations(data_stream, 3))

# Apply complex filtering condition using modular arithmetic and thresholds
processed = []
for combo in combo_list:
    product = combo[0] * combo[1] * combo[2]
    total = sum(combo)
    if product % 7 == 0 and total > 15:
        processed.append(int(math.sqrt(product) + total * 0.5))

# Misleading intermediate: transform via lambda but unused later
unused_transform = list(map(lambda x: x * 2 + 1 if x < 20 else x - 5, processed))

# Critical filtering path: only keep values that pass bit-count check
bit_filtered = [v for v in processed if bin(v).count('1') % 3 == 0]

# Secondary distraction: simulate checksum validation (not used)
temp_checksum = 0
for val in bit_filtered:
    temp_checksum ^= (val * 3) % 255

# Final filter: exclude any number containing digit '3' in decimal form
strict_filtered = [x for x in bit_filtered if '3' not in str(x)]

# Introduce a red herring list comprehension with side effects (no side effects actually)
_ = [data_stream.append(x * 2) for x in strict_filtered if x > 100]  # No effect due to condition

# Core result computation
filtered_results = [x for x in strict_filtered if x % 4 == 2]
filtered_sum = sum(filtered_results)

# Output the target result
print(f"Target result: {filtered_sum}")