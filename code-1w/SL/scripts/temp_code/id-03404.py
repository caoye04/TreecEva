from collections import defaultdict, Counter
import math

# Simulated sensor array data (irrelevant to final result but adds complexity)
sensor_readings = [0.78, 0.65, 0.92, 0.41, 0.58, 0.99, 0.12]
noise_floor = sum([math.sin(x * 0.5) for x in range(100)]) / 100
calibration_offset = math.log(1 + math.exp(-0.1))

# Irrelevant function: processes unused data path
def compute_entropy(sequence):
    freqs = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Dead code - never called but looks important
def deprecated_calibration(data):
    return [x * calibration_offset for x in data]

# Unused transformation matrix
tf_matrix = [[1, 0], [0, 1]]
for i in range(2):
    for j in range(2):
        tf_matrix[i][j] = math.cos(i + j) * noise_floor

# Core logic disguised among distractions
system_flags = [True, False, True]
activation_threshold = 0.7

# Simulated quantum signature (key input)
quantum_signature = [3, 1, 4, 1, 5, 9, 2, 6]

# Decoy calculation using irrelevant modular arithmetic
checksum = 0
for x in quantum_signature:
    checksum = (checksum + x * 3) % 11

# Primary analysis function with nested logic
flag_state = any(system_flags)
inversion_count = 0
for i in range(len(quantum_signature) - 1):
    if quantum_signature[i] > quantum_signature[i+1]:
        inversion_count += 1

# Secondary pattern detection (distraction)
doubled_pairs = 0
for i in range(0, len(quantum_signature) - 1, 2):
    if quantum_signature[i] == quantum_signature[i+1]:
        doubled_pairs += 1

# Red herring variable - looks like it contributes but doesn't
aggregated_weight = (inversion_count * 2 + doubled_pairs) / (len(quantum_signature) // 2)

# Real computation path begins here (hidden among noise)
def bit_flip_energy(seq):
    energy = 0
    for val in seq:
        binary = bin(val)[2:]
        for b in binary:
            energy += 1 if b == '1' else -1
    return energy

# Recursive reduction (core concept)
def recursive_reduce(arr):
    if len(arr) <= 1:
        return arr[0] if arr else 0
    mid = len(arr) // 2
    left = recursive_reduce(arr[:mid])
    right = recursive_reduce(arr[mid:])
    return (left * 3 + right * 2) % 7

# Misleading normalization factor (unused)
normalization_factor = math.sqrt(sum([x**2 for x in sensor_readings]))

# Main analyzer - only function that matters
modular_base = 13
def analyze_system_state(signal):
    # Step 1: Apply modular transform
    transformed = [x % modular_base for x in signal]
    
    # Step 2: Count primes in transformed (red herring)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    prime_count = sum(1 for x in transformed if is_prime(x))
    
    # Step 3: Bit-flip energy (actually used)
    energy_level = bit_flip_energy(transformed)
    
    # Step 4: Recursive reduction on every third element
    reduced_sequence = [transformed[i] for i in range(0, len(transformed), 3)]
    recursive_result = recursive_reduce(reduced_sequence)
    
    # Step 5: Conditional adjustment based on flag state (always true)
    adjustment = 5 if flag_state else -5
    
    # Step 6: Final composition (only energy_level and recursive_result matter)
    # All other variables are distractions
    diagnostic_score = energy_level + recursive_result + adjustment
    
    # Dead branch - never executed due to constant condition
    if calibration_offset > 1.0:
        diagnostic_score *= 2
    
    return diagnostic_score

# Execute main logic
final_diagnostic = analyze_system_state(quantum_signature)

# Print result as required
print(f"Target result: {final_diagnostic}")