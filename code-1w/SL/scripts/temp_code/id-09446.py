from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings and complex logic
raw_signals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
noise_floor = 2
calibration_offset = 0.7
sample_rate = 100  # Hz, unused but plausible

# Irrelevant transformation 1: frequency domain mockup
frequencies = [math.sin(x * 0.5) for x in range(len(raw_signals))]
dummy_fft = [abs(f + 0.1j) for f in frequencies]  # Distractor

# Relevant preprocessing path
filtered_signal = [x for x in raw_signals if x > noise_floor]
scaled_signal = [x + calibration_offset for x in filtered_signal]

# Decoy statistical analysis (never used)
mean_val = sum(raw_signals) / len(raw_signals)
variance = sum((x - mean_val) ** 2 for x in raw_signals) / len(raw_signals)
entropy_proxy = -sum(p * math.log(p) for p in Counter(raw_signals).values())  # Nonsensical but plausible

# Real transformation begins here
shift_register = lambda seq, shift: [(x << 1) ^ shift for x in seq]
transformed_data = shift_register(scaled_signal, 3)

# Hash mapping with decoy entries
hash_lookup = defaultdict(lambda: 100)
for i, val in enumerate(transformed_data):
    hash_lookup[f'node_{i}'] = val % 7

# Unused recursive structure (dead path)
def recursive_denoise(data, depth=0):
    if depth >= 3 or len(data) < 2:
        return data
    mid = len(data) // 2
    return recursive_denoise(data[:mid], depth + 1) + recursive_denoise(data[mid:], depth + 1)

# Control flow with misleading branches
def analyze_pattern(data, threshold):
    size = len(data)
    if size == 0:
        return -1
    
    # Real computation starts
    accumulator = 0
    for i in range(size):
        if i % 2 == 0:
            accumulator += data[i] * (i + 1)
        else:
            accumulator -= (data[i] // 2) * (i - 1)
    
    # Secondary modulation via bit manipulation
    temp_result = accumulator ^ 0b1101
    temp_result = (temp_result & 0xFF) | ((temp_result >> 8) & 0xFF)
    
    # Final adjustment using modular arithmetic
    adjusted = (temp_result + 7) % 1000
    
    # Decoy branch that looks important but is unreachable due to logic
    if all(x < threshold for x in data) and False:  # Short-circuit dead branch
        backup = sum(math.ceil(math.log(abs(x) + 1)) for x in data)
        return backup % 500
    
    return adjusted

# More irrelevant variables
correlation_matrix = [[i * j for j in range(5)] for i in range(5)]  # Unused
baseline_correction = list(map(lambda x: x * 0.95, dummy_fft))  # Dead code

key_threshold = 5
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Critical output
print(f"Result: {final_diagnostic}")