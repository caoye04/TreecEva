import math

# System telemetry (irrelevant to final result but plausible)
telemetry_log = {'voltage': 3.3, 'temp_c': 42.1, 'cycle_count': 157}
last_known_state = [0] * 16
diagnostic_trace = set()

# Core data structures
quantum_buffer = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

calibration_map = {
    'gain': 1.75,
    'offset': -0.25,
    'thresholds': [0.1, 0.35, 0.7, 1.0],
    'weights': [0.2, 0.3, 0.4, 0.1]
}

# Decoy function - looks important but never called
def legacy_recalibrate(data, factor=1.1):
    for i in range(len(data)):
        data[i] = [round(x * factor) % 2 for x in data[i]]
    return data

# Unused transformation matrix
transform_kernel = [[-1, 2], [3, -1]]
scratch_matrix = [[0 for _ in range(4)] for _ in range(4)]

# Simulated noise injection (distractor)
noise_profile = []
for i in range(4):
    noise_val = (math.sin(i * 0.5) + 1) / 2
    noise_profile.append(round(noise_val, 2))

# Phantom checksum calculation (dead code path)
temp_checksum = 0
for row in quantum_buffer:
    for val in row:
        temp_checksum = (temp_checksum + val * 113) % 257

def extract_bit_patterns(matrix):
    # Extracts diagonal bit patterns - actually used
    pattern_sum = 0
    for i in range(len(matrix)):
        bit = matrix[i][i]
        pattern_sum += bit * (2 ** i)
    return pattern_sum

# Auxiliary state processor (partial red herring)
def compute_entropy(vector, weights):
    entropy = 0.0
    for i, w in enumerate(weights):
        if vector[i] > 0:
            p = vector[i] / sum(vector)
            entropy -= p * w * math.log(p + 1e-9)
    return round(entropy, 4)

# Real computation begins here
buffer_size = len(quantum_buffer)
working_copy = [row[:] for row in quantum_buffer]

# Apply dummy gain adjustment (only modifies copy, original untouched)
for i in range(buffer_size):
    for j in range(buffer_size):
        working_copy[i][j] = int((working_copy[i][j] + calibration_map['offset']) \
                              * calibration_map['gain'] + 0.5)

# Track visited positions (mostly unused)
visited = set()
for i in range(buffer_size):
    for j in range(buffer_size):
        visited.add((i, j))

# Critical diagnostic logic
primary_pattern = extract_bit_patterns(quantum_buffer)
secondary_score = 0
for i, row in enumerate(quantum_buffer):
    secondary_score += sum(row) * (i + 1)

# Weighted combination using calibration weights
fusion_factor = 0
for idx, threshold in enumerate(calibration_map['thresholds']):
    if primary_pattern > threshold * 10:  # Scale threshold for integer comparison
        fusion_factor += calibration_map['weights'][idx]

# Hidden accumulator - key to final result
accumulator = 0
sequence = [primary_pattern, secondary_score, buffer_size]
for val in sequence:
    while val > 0:
        accumulator += val & 1
        val >>= 1

# Decoy: Attempt to correlate with noise (no effect)
correlation_peak = 0
for n in noise_profile:
    test_corr = abs(n - calibration_map['offset'])
    if test_corr > correlation_peak:
        correlation_peak = test_corr

# Final analysis function
def analyze_system_state(buffer, config):
    # Actual answer derivation
    diag_1 = extract_bit_patterns(buffer)
    diag_2 = 0
    for r in buffer:
        diag_2 += sum(r)
    
    # Secret rule: combine bit count of diagonals and total sum
    bit_count = bin(diag_1).count('1') + bin(diag_2).count('1')
    size_factor = len(buffer)
    
    # True computation
    result = bit_count * size_factor
    
    # Irrelevant smoothing
    smoothed = result * config['gain'] + config['offset']
    return int(smoothed)  # Deterministic conversion

# Execute critical statement
final_diagnostic = analyze_system_state(quantum_buffer, calibration_map)
print(f"Result: {final_diagnostic}")