import itertools

# Irrelevant helper that's never called
def obsolete_transform(data):
    return [x ^ 255 for x in data if x % 3 != 0]

# Decoy function with misleading logic
def compute_legacy_hash(seq):
    acc = 0
    for i, val in enumerate(seq):
        acc += val * (i + 1) ^ 17
    return acc % 997

# Unused transformation path
temporary_buffer = [n * 3 + 2 for n in range(15) if n % 4 != 3]
shadow_map = {k: k * k - 1 for k in temporary_buffer[:10]}

# Real computation begins
raw_signal = [126, 83, 142, 91, 77, 135, 68, 99]
filtered = list(filter(lambda x: x > 70, raw_signal))

# Apply phase shift using bitwise rotation emulation
def rotate_left(val, n):
    return ((val << n) | (val >> (8 - n))) & 255

rotated = [rotate_left(x, 3) for x in filtered]

# Misleading normalization branch (dead end)
normalized = [round(x / 255.0, 4) for x in rotated]
avg_normalized = sum(normalized) / len(normalized)

# Real processing chain
segment_a = rotated[::2]
segment_b = rotated[1::2]

# XOR fusion with offset
fused = [a ^ b ^ (i * 7) for i, (a, b) in enumerate(itertools.zip_longest(segment_a, segment_b, fillvalue=17))]

# Check for parity anomalies (irrelevant count)
parity_errors = sum(1 for x in fused if bin(x).count('1') % 2 == 0)

# Critical transformation pipeline
interim = [(x + 13) * 2 for x in fused]
masked = [x & 0x7F for x in interim]  # Strip high bit
extended = [x for pair in zip(masked, [x ^ 0x55 for x in masked]) for x in pair]

# Dummy statistical analysis
median_like = sorted(extended)[len(extended)//2]
variance_proxy = sum((x - avg_normalized*100)**2 for x in extended[:4])  # Red herring

# Final block construction
final_block = [extended[i] + i//8 for i in range(len(extended))]

# Core checksum algorithm (non-trivial)
def process_segment(block):
    result = 0
    for idx, val in enumerate(block):
        if idx % 3 == 0:
            result += val * 3
        elif idx % 5 == 0:
            result -= val
        else:
            result ^= val * 2
    return result % 100000

# Dead code: simulate alternate checksum (never used)
def alt_checksum(block):
    return sum(block[i] * (i+1) for i in range(len(block))) % 8888

# Execution point of interest
current_mode = 'primary'
if current_mode == 'primary':
    temp_result = sum(final_block) / len(final_block)
    metadata_log = f'Mode: {current_mode}, Size: {len(final_block)}, Avg: {temp_result:.2f}'
    # Actual answer calculation
    checksum = process_segment(final_block)

print(f'Result: {checksum}')