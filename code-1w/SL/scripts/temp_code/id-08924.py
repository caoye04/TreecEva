from itertools import cycle, islice

def analyze_pattern(sequence, threshold=3):
    """ Analyzes repeating patterns in a sequence (distractor function). """
    repeated = []
    for i in range(len(sequence)):
        subseq = sequence[i:i+threshold]
        if sequence.count(subseq) > 1 and len(subseq) == threshold:
            repeated.append(subseq)
    return list(set(map(tuple, repeated)))


def bit_scramble(n):
    """ Bit manipulation red herring. """
    if n == 0: return 0
    binary = bin(n)[2:]
    rotated = binary[1:] + binary[0]
    return int(rotated, 2)

# Irrelevant data structures
user_preferences = {'theme': 'dark', 'notifications': True, 'timeout': 30}
config_matrix = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]

# Core input data
raw_signals = [5, -3, 8, 2, -1, 7, 4, 6]
weights = [0.1, 0.3, 0.2, 0.4]

# Distractor: unused transformation
shifted_signals = [x + 2 for x in raw_signals if x > 0]
noise_floor = sum([abs(x) for x in raw_signals]) / len(raw_signals)

# Real processing begins
filtered = [x for x in raw_signals if x >= 0]
padded = filtered + [0] * (len(weights) - (len(filtered) % len(weights))) if len(filtered) % len(weights) != 0 else filtered

# Matrix-like grouping (not actually used later but looks important)
grouped_batches = [padded[i:i+len(weights)] for i in range(0, len(padded), len(weights))]

# Key intermediate computation
averaged_batch = [sum(batch) / len(batch) for batch in grouped_batches]
mean_level = sum(averaged_batch) / len(averaged_batch)

# More distractions: fake control flow
if mean_level > 5:
    adjustment_factor = 1.5
else:
    adjustment_factor = 0.8  # This path is taken

status_flags = {k: (v > 0) for k, v in enumerate(averaged_batch)}
decoy_map = dict(zip(cycle(['A','B','C']), islice(cycle(range(3)), len(averaged_batch))))

# Real signal weighting
weighted_values = []
for idx, val in enumerate(filtered):
    weight_idx = idx % len(weights)
    weighted_values.append(val * weights[weight_idx])

aggregate_power = sum(weighted_values)
baseline_offset = noise_floor * 0.5

# Simulated calibration chain (mostly irrelevant)
calibration_steps = 0
for step in range(3):
    calibration_steps += 1
    temp_adjust = bit_scramble(step)
    if temp_adjust > 2:
        baseline_offset += 0.1

# Final transformation using slicing and zip
paired = list(zip(weighted_values[::2], weighted_values[1::2]))
fluctuation_index = sum(abs(a - b) for a, b in paired)

# Critical statement
final_score = int((aggregate_power - baseline_offset) * adjustment_factor + fluctuation_index // 2)

# Output result
Result: {final_score}