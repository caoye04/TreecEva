from collections import defaultdict
from itertools import cycle

# Simulated network packet analysis with checksum computation

# Real data stream (hex-encoded)
raw_data = 'a3f5c7d2e1b486a9f0cd37be5f8a2c1d'

data_bytes = [int(raw_data[i:i+2], 16) for i in range(0, len(raw_data), 2)]

# Irrelevant: ASCII mapping for unused decoding path
text_map = {i: chr((i + 48) % 128) for i in range(128)}
unused_ascii = ''.join([text_map[b % 128] for b in data_bytes])

# Decoy statistical analysis (never used)
freq_counter = defaultdict(int)
for b in data_bytes:
    freq_counter[b % 16] += 1

modes = [k for k, v in freq_counter.items() if v == max(freq_counter.values())]
mode_val = modes[0] if modes else 0

# Distractor: Base conversion loop with no impact
base_shift = 0
for i, b in enumerate(data_bytes[:8]):
    base_shift += (b % 3) * (7 - i)

# Fake encryption attempt (dead code path)
cipher_seq = []
key_stream = cycle([0x1f, 0x2d, 0x3a, 0x4c])
for b in data_bytes:
    encrypted = b ^ next(key_stream)
    cipher_seq.append((encrypted << 1) | (encrypted >> 7))

# Unused transformation: bit reversal
reversed_bits = []
for b in data_bytes:
    rev = sum(((b >> i) & 1) << (7 - i) for i in range(8))
    reversed_bits.append(rev)

# Begin relevant logic: data integrity verification
offset = sum(b for i, b in enumerate(data_bytes) if i % 3 == 0) % 256
scale = len([b for b in data_bytes if b > 128])
data_sum = sum(data_bytes) + offset * scale

# Bit manipulation mask generated from position patterns
positions = [i for i, b in enumerate(data_bytes) if b % 5 == 2]
mask = 0
for p in positions:
    mask ^= (p * 0x11) & 0xFF

# Prime modulus based on byte diversity
distinct_bytes = set(data_bytes)
prime = 983  # Largest prime less than 1000, close to distinct count influence

# Key statement: actual checksum calculation
checksum = (data_sum ^ mask) % prime

# More red herrings below...

# Fake error correction code (never invoked)
def correct_errors(seq, key):
    return [b ^ key for b in seq]

# Useless string operations
temp_str = ''.join(f'{b:02x}' for b in data_bytes)
shuffled = ''.join(sorted(temp_str, reverse=True))

# Dummy checksum comparison (misleading)
expected_checksum = 42
is_valid = checksum == expected_checksum  # This is false, but irrelevant

# Final output
print(f"Result: {checksum}")