from collections import defaultdict, Counter

# Irrelevant data structures and variables (distractors)
default_config = defaultdict(lambda: 'N/A')
default_config['version'] = '2.1.0'
default_config['mode'] = 'DEBUG'

log_entries = [
    {'type': 'INFO', 'value': 10},
    {'type': 'WARN', 'value': 5},
    {'type': 'ERROR', 'value': 3}
]
error_count = sum(1 for e in log_entries if e['type'] == 'ERROR')

# Unused recursive function (red herring)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Bit manipulation decoy
temp_flag = 0b10101010
toggle_mask = 0b11110000
masked_flag = temp_flag ^ toggle_mask  # Unused result

# Core simulation state
state = [0] * 16
for i in range(16):
    state[i] = (i * i + 3) % 257

# Irrelevant slicing and transformations
slice_a = state[3:10]
slice_b = state[::2]
slice_c = slice_a[::-1]  # Reversed, unused

# Decoy statistical calculation
mean_val = sum(slice_b) / len(slice_b)
variance = sum((x - mean_val) ** 2 for x in slice_b) / len(slice_b)
std_dev = variance ** 0.5  # Not used

# Frequency analysis (partially relevant)
freq = Counter()
for val in state:
    freq[val % 7] += 1

# Misleading accumulation path
dummy_accum = 0
for k, v in freq.items():
    if k % 2 == 0:
        dummy_accum += v * k
    else:
        dummy_accum -= v

# Real computation begins here — complex transformation
shifted = []
for idx, val in enumerate(state):
    shifted.append((val ^ (idx * 3)) + (1 << (idx % 4)))

# Another layer of processing
filtered = [x for x in shifted if x % 3 == 2]

# Hash-like reduction with bitwise operations
digest = 0xCAFEBABE
for num in filtered:
    digest ^= num
    digest = (digest << 3 | digest >> 29) & 0xFFFFFFFF
    digest = (digest + (num * 7)) & 0xFFFFFFFF

# Secondary masking using frequency keys
for key in sorted(freq.keys()):
    digest ^= (key * 17) << 2
    digest = (digest & 0xFFFFFF) ^ ((digest >> 16) & 0xFFFF)

# Finalize logic — critical execution point
mask = 0x7FFF
size_factor = len(state) * 2
correction = (digest >> 10) & 0xFF

# Actual answer computation buried in noise
temp_result = (digest ^ correction) & mask
temp_result = (temp_result + size_factor) % 98765

# Checksum depends on conditional path that is hard to trace
if len(filtered) > 10:
    checksum = temp_result + 500
else:
    checksum = temp_result - 200

# Red herring: another variable with similar name
check_sum_alt = sum(state[i] for i in range(0, len(state), 3))

# Final output
print(f"Result: {checksum}")