from collections import defaultdict, Counter

# Irrelevant helper that's never called
def analyze_pattern(seq):
    freq = Counter(seq)
    return sorted(freq.values())

# Dead function - looks useful but unused
def compute_entropy(data):
    total = sum(data)
    probs = [v / total for v in data]
    return -sum(p * p for p in probs)

# Decoy transformation chain
temperatures_celsius = [0, 37, 100, -40]
humidity_levels = list(map(lambda x: (x * 1.8) + 32, temperatures_celsius))
adjusted_humidity = [h // 2 for h in humidity_levels if h > 50]

# Core signal processing simulation with distractions
raw_signal = [12, 45, 67, 23, 89, 34, 56, 78, 91, 11]
noise_floor = 25
amplitude_correction = 1.05

# Apply gain and filter noise (only some steps are relevant)
gained_signal = [int(x * amplitude_correction) for x in raw_signal]
filtered_signal = [x for x in gained_signal if x > noise_floor]

# Distractor: complex frequency analysis (unused)
frequencies = defaultdict(int)
for val in raw_signal:
    frequencies[val % 7] += 1
harmonic_peaks = [k for k, v in frequencies.items() if v >= 2]

# Signal slicing: only middle segment used in final computation
segment_a = filtered_signal[:3]
segment_b = filtered_signal[3:6]
segment_c = filtered_signal[6:]  # unused decoy

working_buffer = segment_a + [x ^ 17 for x in segment_b]  # XOR manipulation

# Red herring: statistical summary (not used)
mean_val = sum(working_buffer) // len(working_buffer)
variance_proxy = sum((x - mean_val) ** 2 for x in working_buffer) // len(working_buffer)

# Key transformations leading to answer
rotated = working_buffer[1:] + working_buffer[:1]  # left rotate
summed_pairs = [rotated[i] + rotated[i+1] for i in range(0, len(rotated)-1, 2)]
doubled = [x * 2 for x in summed_pairs]

# Hash-like reduction
aggregated = 0
for val in doubled:
    aggregated ^= val
    aggregated = (aggregated * 3) % 101

# Bit manipulation decoys
shift_sequence = [aggregated >> i for i in range(3)]
masked_out = [x & 0b1111 for x in shift_sequence]  # distraction

# Actual critical path starts from here (obscured by prior code)
baseline = 987
offsets = [33, 12, 8]
scaling_factor = 7

sum_filtered = sum(filtered_signal)  # depends on earlier filter

# Complex masking with irrelevant alternatives
mask_options = [
    0xFFFF ^ 0xAA,   # plausible but unused
    0xFF,
    0xF0 | 0x0F     # identity mask
]
mask = mask_options[1]  # selected via distraction index

# Finalization function with red herring operations
def finalize(value):
    temp = value
    temp ^= 0x55
    temp = (temp + 17) * 2
    temp %= 9973
    # Multiple unused transforms below
    temp = (temp << 1) | (temp >> 7)
    temp ^= sum(masked_out)  # uses decoy var
    temp += variance_proxy   # pulls in dead code branch
    temp %= 100000
    return temp

# Critical execution point
checksum = finalize(sum_filtered & mask)

# Output requirement
print(f"Result: {checksum}")