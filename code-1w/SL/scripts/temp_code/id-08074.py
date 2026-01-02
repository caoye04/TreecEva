import math

# Simulated sensor data preprocessing with heavy distractions
def analyze_pattern(sequence):
    if len(sequence) == 0:
        return 0
    
    # Irrelevant transformation (red herring)
    temp_result = [x ** 2 + 3 for x in sequence if x % 2 == 0]
    temp_sum = sum(temp_result) * 0.1

    # Decoy statistical measure
    avg_val = sum(sequence) / len(sequence) if sequence else 0
    variance = sum((x - avg_val) ** 2 for x in sequence) / len(sequence) if sequence else 0

    # Real but obscured logic: count peaks above dynamic baseline
    baseline = avg_val * 0.75
    peak_count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1] and sequence[i] > baseline:
            peak_count += 1

    return peak_count

# Unused decoy function (dead code path)
def encrypt_data(data):
    encrypted = ''
    for d in data:
        encrypted += chr((d + 7) % 256)
    return encrypted

# Bit manipulation red herring
def obscure_value(n):
    shifted = (n << 3) & 0xFF
    toggled = shifted ^ 0xAA
    wrapped = (toggled + 17) % 200
    return wrapped

# Core signal processing chain
initial_data = [12, 45, 23, 67, 34, 89, 23, 56, 78, 33]

# Distractor: multiple irrelevant transformations
scaled_data = [round(x * 1.07, 2) for x in initial_data]
decay_weights = [math.exp(-i * 0.2) for i in range(len(initial_data))]
applied_weights = [scaled_data[i] * decay_weights[i] for i in range(len(scaled_data))]

# Real preprocessing step buried in noise
filtered_data = [x for x in initial_data if x > 20]

# String-based distraction using real data
status_flags = ''.join(['H' if x > 50 else 'L' for x in initial_data])
count_high = status_flags.count('H')

# More decoys: unused intermediate values
checksum = sum(obscure_value(int(x)) for x in scaled_data) % 1000
normalization_factor = math.log(sum(applied_weights) + 1)
adjusted_data = [x / normalization_factor for x in applied_weights]

# Key transformation (non-obvious due to context)
transformed_data = []
for val in filtered_data:
    if val < 50:
        transformed_data.append(val * 1.5)
    else:
        transformed_data.append(val * 0.8 + 10)

# Threshold derived from misleading statistics
threshold = int(variance * 0.5) if 'variance' in locals() else 5  # Uses earlier computed variance

# Another decoy structure: tuple unpacking with unused vars
dynamic_a, dynamic_b = (len(initial_data), sum(initial_data))
size_metric, _ = (dynamic_a * 2, dynamic_b // 10)

# Real processing function interlaced with noise
def process_signal(signal, limit):
    # Complex conditional expression (actual logic)
    processed = [math.ceil(x) if i % 2 == 0 else int(x * 0.95) for i, x in enumerate(signal)]
    
    # Red herring: sorting and reversing
    sorted_rev = sorted(processed, reverse=True)
    midpoint = len(sorted_rev) // 2
    left_half = sorted_rev[:midpoint]
    right_half = sorted_rev[midpoint:]
    
    # Actual key computation
    accumulator = 0
    for idx, num in enumerate(processed):
        if num > limit:
            accumulator += num * (idx + 1)  # Weighted by position
    
    # Distractor: bit operations on sum
    acc_bin = bin(accumulator)
    bit_count = acc_bin.count('1')
    final_shift = (accumulator >> 1) ^ bit_count
    
    # This line determines the actual answer despite distractions
    final_shift += analyze_pattern(initial_data) * 100  # Injects peak count
    
    return final_shift

# Execution point of interest
final_output = process_signal(transformed_data, threshold)

# Output must follow required format
print(f"Target result: {final_output}")