import itertools

def preprocess_readings(readings):
    # Irrelevant preprocessing function (dead code path)
    return [r * 1.05 for r in readings if r > 20]

def validate_checksum(data):
    # Misleading validation with no actual use
    checksum = sum(data) % 256
    return checksum == 0

def transform_signal(signal_stream):
    # Unused transformation function (distractor)
    return [s ^ 0xAA for s in signal_stream]

def decode_pattern(seq):
    # Decoy logic that looks important but isn't used
    if len(seq) < 5:
        return 0
    return sum(seq[i] * (i + 1) for i in range(len(seq))) // len(seq)

def calculate_entropy(values):
    # Seemingly relevant but unused scientific computation
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 6)

def generate_fibonacci(n):
    # Distractor: looks algorithmically rich but not central
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def calculate_thermal_output(sequence):
    # Core logic buried within distractions
    base_level = sum(x ** 0.5 for x in sequence if x % 2 == 1)  # Only odd numbers contribute
    scaling_factor = len([x for x in sequence if x % 4 == 0])  # Count multiples of 4
    
    # Complex-looking but actually simple transformation
    shifted = [((x >> 2) & 7) for x in sequence]
    mode_val = max(shifted.count(i) for i in range(8))
    
    # Real calculation hidden among red herrings
    adjustment = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            adjustment += 1
    
    # Actual formula: base_level * scaling_factor + adjustment * 10
    result = base_level * scaling_factor + adjustment * 10
    
    # Decoy intermediate outputs
    decoy_entropy = calculate_entropy(sequence)
    decoy_fib = generate_fibonacci(10)
    decoy_signal = transform_signal([1, 2, 3])
    
    return int(result)

# Main data - realistic sensor readings
sensor_readings = [12, 25, 36, 49, 64, 81, 100, 121, 144]

# Irrelevant data structures (distractors)
data_buffer = list(itertools.permutations([1, 2, 3], 3))
lookup_table = {i: chr(65 + i) for i in range(10)}
status_flags = [True, False, True, True]

# Unused processing steps
filtered_readings = preprocess_readings(sensor_readings)
checksum_valid = validate_checksum(sensor_readings)
pattern_score = decode_pattern(sensor_readings)

# Critical execution point
process_sequence = [x + 1 for x in sensor_readings if x >= 36]  # New sequence starting from 36
thermal_capacity = calculate_thermal_output(process_sequence)

# Print final result as required
print(f"Result: {thermal_capacity}")