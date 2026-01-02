from collections import defaultdict
import math

# Simulate a signal processing pipeline with noise filtering and data encoding
def generate_noise(length, seed=42):
    # Irrelevant helper function - dead code path
    return [(i * seed) % 7 for i in range(length)]

def decode_checksum(signal):
    # Unused decoding logic - misleading distractor
    return sum(x ** 2 for x in signal if x % 3 == 0)

# System configuration (some values are decoys)
SYSTEM_MODE = "ENCRYPT"
BUFFER_SIZE = 512
THRESHOLD = 95
SCALE_FACTOR = 1.75
OFFSET = -2

# Irrelevant frequency mappings (distractor data structure)
frequency_map = {
    'A': 440.0, 'B': 493.88, 'C': 523.25, 'D': 587.33,
    'X': 1000.0, 'Y': 2000.0, 'Z': 3000.0
}

# Key transformation matrix (used in actual logic)
key_matrix = [
    [2, -1, 0],
    [1, 3, -2],
    [0, 1, 4]
]

# Input sequence - appears random but has deterministic pattern
sequence = [4, -2, 6]

# Noise injection (irrelevant - not actually used)
noise_sequence = [x % 5 for x in generate_noise(10)]

# Data accumulation via list comprehension and filtering (mixed relevance)
filtered_data = [x for x in sequence if abs(x) > 1]
expanded_data = [x + OFFSET for x in filtered_data]  # OFFSET used here

# Matrix-vector multiplication: critical computation hidden among distractors
def matmul(matrix, vector):
    result = []
    for row in matrix:
        total = 0
        for a, b in zip(row, vector):
            total += a * b
        result.append(total)
    return result

# Secondary transformation chain (partially relevant)
intermediate = matmul(key_matrix, sequence)
squared_intermediate = [x ** 2 for x in intermediate if x != 0]

# Signal normalization using modular arithmetic and scaling
normalized = []
for val in intermediate:
    temp = (abs(val) * SCALE_FACTOR) % THRESHOLD
    if val < 0:
        temp = -temp
    normalized.append(round(temp, 4))

# Red herring: string-based encoding (never used)
class Encoder:
    def __init__(self, base):
        self.base = base
    
    def encode(self, data):
        return ''.join([hex(x ^ self.base)[-1] for x in data])

e = Encoder(7)
dummy_encoded = e.encode(sequence)  # Dead end

# Frequency weighting (distractor logic)
weights = []
for k, v in frequency_map.items():
    if v > 500:
        weights.append(int(v / 100))

# Actual signal processing function (core logic)
def process_transmission(data, transform):
    # Step 1: Apply linear transformation
    transformed = matmul(transform, data)
    
    # Step 2: Accumulate absolute values with conditional offset
    accum = 0
    for t in transformed:
        if t > 0:
            accum += t + OFFSET  # Reuse OFFSET
        else:
            accum += abs(t)
    
    # Step 3: Apply bitwise adjustment based on parity
    bit_adjusted = accum
    for t in transformed:
        if t % 2 == 0:
            bit_adjusted ^= 3  # XOR with 3 for even values
    
    # Step 4: Final modulation using min/max stabilization
    stabilized = max(min(bit_adjusted, 888), -888)
    
    return int(stabilized)

# Execute main logic
final_signal = process_transmission(sequence, key_matrix)

# Print result as required
print(f"Target result: {final_signal}")