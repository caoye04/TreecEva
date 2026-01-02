import itertools

# Simulated sensor array data with noise and redundancy
data_stream = [18, 23, 17, 45, 22, 38, 41, 16, 27, 33, 29, 44, 19, 21, 37]
noise_floor = 15
calibration_factor = 0.87
redundant_flags = [False, True, False, True, False, False, True, False, True, False, True]
temp_buffer = [x ** 0.5 for x in data_stream if x > 20]

# Irrelevant transformation: circular shift (dead logic)
def shift_array(arr, n):
    return arr[-n:] + arr[:-n]
shifted = shift_array(data_stream, 3)

# Misleading intermediate: normalized but unused
def normalize(values):
    m = min(values)
    r = max(values) - m
    return [(v - m) / r for v in values if v != 27]  # excludes one arbitrarily
normalized_data = normalize(data_stream)

# Decoy function that looks important but isn't called correctly
def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Real processing begins here — filtering based on threshold and index parity
valid_indices = [i for i in range(len(data_stream)) if data_stream[i] > noise_floor]
filtered_data = [data_stream[i] for i in valid_indices if i % 2 == 0]

# Side computation: grouping by magnitude (distractor)
grouped = {k: list(g) for k, g in itertools.groupby(sorted(filtered_data), key=lambda x: x // 10)}
size_distribution = {k: len(v) for k, v in grouped.items()}

# Another red herring: string-based checksum of numbers (never used)
str_checksum = sum([sum(map(ord, str(x))) for x in filtered_data])

# Core logic hidden among distractions
def process_readings(readings, calib):
    adjusted = [r * calib for r in readings]
    
    # Apply non-linear correction based on position
    corrected = []
    for idx, val in enumerate(adjusted):
        if idx == 0:
            corrected.append(val)
        elif idx % 3 == 0:
            corrected.append(val * 0.95)
        elif idx % 2 == 0:
            corrected.append(val * 1.05)
        else:
            corrected.append(val * 1.02)
    
    # Aggregate with weighted average
    weights = [1.0, 1.2, 1.1, 1.3, 1.05]  # assume max 5 elements
    weighted_sum = sum(corrected[i] * weights[i] for i in range(len(corrected)))
    weight_total = sum(weights[:len(corrected)])
    return round(weighted_sum / weight_total, 6)

# Critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output result as required
print(f"Target result: {final_diagnostic}")