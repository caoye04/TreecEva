from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor data with noise and metadata
data_stream = [18, 23, 14, 14, 27, 31, 20, 25, 36, 12, 19, 22]
noise_profile = [1, -2, 1, 0, 3, -1, 0, 2]
decoy_data = [[i**2 for i in range(8)], [j * 3 for j in range(5)]]

# Irrelevant transformation chain (dead path)
temp_buffer = []
for x in range(len(decoy_data[0])):
    temp_buffer.append(decoy_data[0][x] + sum(noise_profile[:x+1]) if x < len(noise_profile) else 0)

# Misleading checksum calculation (distractor)
pseudo_checksum = 0
for idx, val in enumerate(data_stream):
    pseudo_checksum += val * (idx % 4 + 1)
pseudo_checksum = pseudo_checksum % 1000

# Real processing begins: extract indices where value > 20
candidate_indices = [i for i, v in enumerate(data_stream) if v > 20]

# Generate all pairs of candidate indices (red herring)
index_pairs = list(combinations(candidate_indices, 2))
pair_sums = [p[0] + p[1] for p in index_pairs]

# Apply shift correction using noise profile (irrelevant for final result)
shifted_values = []
for i, val in enumerate(data_stream):
    corrected = val - noise_profile[i % len(noise_profile)]
    shifted_values.append(corrected)

# Core logic disguised among distractions
status_map = defaultdict(str)
for i, val in enumerate(shifted_values):
    if val > 20:
        status_map[i] = 'HIGH'
    elif val > 15:
        status_map[i] = 'MEDIUM'
    else:
        status_map[i] = 'LOW'

# Decoy dictionary aggregation
stats_summary = Counter()
for val in data_stream:
    if val > 25:
        stats_summary['extreme'] += 1
    elif val > 15:
        stats_summary['normal'] += 1
    else:
        stats_summary['low'] += 1

# Critical real operation: filter original data based on transformed conditions
working_flags = []
for i, original_val in enumerate(data_stream):
    shifted_val = shifted_values[i]
    if shifted_val >= 20 and original_val % 2 == 0:
        working_flags.append(True)
    else:
        working_flags.append(False)

# Mask application using zip and enumerate (actual relevant step)
final_mask = []
for i, (flag, orig) in enumerate(zip(working_flags, data_stream)):
    override = False
    # Spurious cycle-based override check (mostly false)
    for _, c in zip(range(3), cycle([0, 1])):
        if i % 5 == c and orig < 30:
            override = True
            break
    final_mask.append(flag and not override)

# Actual filtering step
filtered_values = []
for include, val in zip(final_mask, data_stream):
    if include:
        filtered_values.append(val)

# Key assignment statement
filtered_sum = sum(filtered_values)

print(f"Result: {filtered_sum}")