import itertools

def generate_wave(harmonics, base_freq):
    # Irrelevant function: simulates a signal wave (dead code path)
    return [base_freq * (i % harmonics) for i in range(10)]

def filter_noise(data, level):
    # Misleading function: appears useful but unused
    return [x for x in data if x > level]

def compute_checksum(seq):
    # Decoy computation: looks important but not part of final result
    return sum(x ^ (i * 3) for i, x in enumerate(seq)) % 1000

def analyze_pattern(seq, limit):
    # Core logic hidden among distractions
    seq = [x for x in seq if x % 2 == 1]  # Keep only odd values
    seq = [x for x in seq if x > limit]   # Filter by threshold
    
    # Simulate rolling window comparisons
    shifts = []
    for i in range(3):
        shifted = list(itertools.islice(itertools.cycle(seq), i, i + len(seq)))
        comparison = [a - b for a, b in zip(seq, shifted)]
        shifts.append(sum(comparison))
    
    # Complex transformation with modular arithmetic and recursion
    def recursive_dampen(value, depth):
        if depth <= 0 or value < 5:
            return value
        return recursive_dampen((value // 2) + (value % 7), depth - 1)
    
    base = sum(shifts) // 3
    adjusted = recursive_dampen(abs(base), 4)
    
    # Final scoring with red herring intermediate steps
    temp_score = adjusted * 17
    correction = 0
    for i in range(2, 5):
        if temp_score % i == 0:
            correction += i
    
    # Actual answer computation
    equilibrium_score = temp_score - correction
    
    # Distractor: fake normalization
    normalized = equilibrium_score / (1 + abs(equilibrium_score) * 0.01)
    
    return equilibrium_score  # Only this matters

# Irrelevant global variables
harmonic_data = generate_wave(7, 440)
current_mode = "diagnostic"
debug_log = []

# Input setup with plausible decoys
raw_sequence = list(range(15, 35))
processed_buffer = [x * 2 for x in raw_sequence]  # Unused
threshold = 20
sequence = [x + (x % 4) for x in raw_sequence]  # Main input

# Hidden critical operation
checksum = compute_checksum(sequence)  # Dead end

# Key statement
equilibrium_score = analyze_pattern(sequence, threshold)

# Print required output
print(f"Result: {equilibrium_score}")