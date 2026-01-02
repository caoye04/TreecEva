from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant channels
data_stream = [
    [1, 0, 1, 2, 3, 1, 0],
    [2, 1, 0, 1, 2, 2, 1],
    [1, 1, 1, 0, 0, 3, 2],
    [0, 2, 1, 1, 1, 0, 1],
    [3, 3, 2, 2, 1, 1, 0]
]

# Irrelevant statistical moment calculations (distractor)
mean_vals = []
for row in data_stream:
    mean_vals.append(sum(row) / len(row))

# Misleading entropy computation on flattened data (dead path)
flattened = [val for row in data_stream for val in row]
entropy = 0
freq_dist = defaultdict(int)
for v in flattened:
    freq_dist[v] += 1
import math
for count in freq_dist.values():
    p = count / len(flattened)
    entropy -= p * math.log2(p) if p > 0 else 0

# Decoy signal processing function (never called)
def analyze_wavelet(signal):
    transformed = []
    for i in range(len(signal) - 1):
        transformed.append(signal[i] ^ signal[i+1])
    return [x & 7 for x in transformed]

# Begin relevant diagnostic logic
active_sensors = 0
valid_windows = 0
consistency_flags = []

for idx, reading in enumerate(data_stream):
    # Slice middle portion to simulate windowed analysis
    window = reading[1:6]
    
    # Count transitions (edge detection)
    transitions = 0
    for j in range(len(window) - 1):
        if window[j] != window[j+1]:
            transitions += 1
    
    # Flag stable readings (low transition)
    consistency_flags.append(transitions <= 2)
    
    # Update active sensors based on non-zero burst
    if sum(window) > 4:
        active_sensors += 1
    
    # Validate temporal continuity
    if idx > 0:
        prev_mid = data_stream[idx-1][1:6]
        if all((window[i] + prev_mid[i]) % 2 == 0 for i in range(5)):
            valid_windows += 1

# Secondary validation using bit patterns (relevant)
bit_stability = 0
for row in data_stream:
    packed = 0
    for val in row[:4]:
        packed = (packed << 2) | (val & 3)
    # Check if upper bits show repeating pattern
    if (packed ^ (packed >> 4)) & 0xF0F == 0:
        bit_stability += 1

# Compute base aggregate score
raw_consistency = sum(consistency_flags)
aggregate_score = raw_consistency * active_sensors + valid_windows

# Red herring: complex but unused transformation chain
decoy_matrix = [[i*j % 7 for j in range(5)] for i in range(5)]
transform_stack = []
for r in decoy_matrix:
    transform_stack.extend([x ^ 5 for x in r if x % 3 == 0])
residual = sum(transform_stack) % 19

# Unused recursive validator (distractor)
def validate_chain(depth, acc):
    if depth == 0:
        return acc
    return validate_chain(depth - 1, acc ^ (depth * 3))

# Correction factor derived from bit stability and system state
correction_factor = 0
if bit_stability >= 2:
    if raw_consistency > 2:
        correction_factor = (bit_stability * 17) // (raw_consistency - 1)
    else:
        correction_factor = bit_stability * 5
else:
    correction_factor = -10

# Critical assignment point
final_diagnostic = aggregate_score + correction_factor

# Final output
print(f"Result: {final_diagnostic}")