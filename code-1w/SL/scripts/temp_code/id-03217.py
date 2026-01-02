import itertools

# Simulated sensor data with noise and redundant metrics
data_stream = [7, 2, 11, 5, 3, 9, 13, 8, 6, 4, 10, 1, 12]

# Irrelevant auxiliary data (distractor)
weights = [0.1, 0.5, 0.3, 0.8, 0.7, 0.2, 0.9, 0.4, 0.6]
baseline_offset = 42
scaling_factor = 1.7
offset_cache = []

# Misleading pre-processing (dead path)
def apply_filter(x):
    return (x * scaling_factor + baseline_offset) % 11

# Unused transformation chain (red herring)
transformed = list(map(apply_filter, data_stream))
smoothed = [sum(transformed[i:i+3]) / 3 for i in range(len(transformed) - 2)]

# Relevant signal detection: extract primes (actual logic start)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Extract prime numbers from data stream
prime_indices = [i for i, x in enumerate(data_stream) if is_prime(x)]
filtered_data = [data_stream[i] for i in prime_indices if i % 2 == 0]  # Only even-indexed primes

# Decoy function that is never called
def analyze_trend(seq):
    return sum(seq[i] > seq[i-1] for i in range(1, len(seq)))

def compute_moment(sequence, order=2):
    mean_val = sum(sequence) / len(sequence)
    return sum((x - mean_val) ** order for x in sequence) / len(sequence)

# Real processing begins here — complex transformation with distractors
signal_power = compute_moment(filtered_data, order=2)

# Bit manipulation red herring
bit_accumulator = 0
for x in filtered_data:
    bit_accumulator ^= (x << 1) | 1
    bit_accumulator &= 0xFF  # Clamp to 8 bits (irrelevant)

# Core logic hidden among distractions
shift_key = len(prime_indices) % 5 or 1
decoded = [x >> shift_key for x in filtered_data]  # Right-shift by dynamic amount

# Use itertools to generate pairwise differences (legitimate use)
pairs = list(itertools.pairwise(decoded))
gradient_sum = sum(b - a for a, b in pairs if b > a)

# Another decoy: unused statistical check
reversed_check = list(itertools.accumulate(decoded[::-1]))

# Final non-linear transformation (critical step)
intermediate = 0
for i, val in enumerate(decoded):
    if i % 2 == 0:
        intermediate += val ** 1.5
    else:
        intermediate -= pow(val, 0.7)

# Key assignment statement
final_output = int(intermediate + gradient_sum) // 2

# Output result as required
print(f"Result: {final_output}")