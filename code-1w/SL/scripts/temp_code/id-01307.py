import itertools

# Simulated sensor data processing with noise filtering and calibration
raw_readings = [248, 153, 991, 442, 677, 38, 511]
offset_table = [7, 13, 19, 23]
noise_floor = 42

def apply_mask(x, mask=0xFF):
    return x & mask

def is_outlier(val, lower=100, upper=900):
    # Misleading: only some values are actually checked in execution
    return val < lower or val > upper

def calibrate(x, index):
    # Complex transformation with modular arithmetic and bit shifts
    return ((x + offset_table[index % len(offset_table)]) ^ 0x5A) % 1000

# Irrelevant preprocessing path - dead code branch
legacy_mode = False
if legacy_mode:
    processed = [x // 2 for x in raw_readings if x % 2 == 0]
else:
    processed = []
    for i, val in enumerate(raw_readings):
        if val > noise_floor:  # Most pass this
            adjusted = calibrate(val, i)
            processed.append(adjusted)

# Decoy statistical summary (not used in final result)
mean_val = sum(processed) / len(processed)
median_val = sorted(processed)[len(processed)//2]
mode_val = max(set(processed), key=processed.count)

# Real computation chain begins here
filtered = [apply_mask(x) for x in processed]  # Truncate to byte range

# Bit manipulation series
shifted_pairs = []
for a, b in itertools.pairwise(filtered):
    combined = ((a << 2) ^ (b >> 1)) & 0xFFFF
    shifted_pairs.append(combined)

# Another layer of transformation
hashed_sequence = []
for idx, num in enumerate(shifted_pairs):
    rotated = ((num << (idx % 7)) | (num >> (8 - (idx % 7)))) & 0xFF
    hashed_sequence.append(rotated)

# Secondary decoy: frequency analysis (unused)
frequency_map = {x: hashed_sequence.count(x) for x in set(hashed_sequence)}
top_freq = max(frequency_map.values())

# Core algorithm variables
base_value = 0
for step in hashed_sequence[::2]:  # Every other element
    base_value += (step * 3) + 7

phase_shift = len([x for x in filtered if x % 3 == 0])  # Count divisible by 3
modulus = 9973  # Large prime modulus

# Key statement — target of the question
checksum = (base_value * phase_shift) % modulus

# Red herring output
debug_info = {
    'raw_count': len(raw_readings),
    'valid_readings': len(processed),
    'checksum_candidate': (sum(hashed_sequence) * 17) % modulus  # Looks plausible but unused
}

# Final output
Result: {checksum}