from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing pipeline for aerospace telemetry
base_readings = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140]
diagnostic_map = defaultdict(lambda: 0)
fault_flags = [False, True, False, True, True, False, True]

# Irrelevant transformation: frequency harmonics (dead path)
harmonic_series = []
for i in range(len(base_readings)):
    harmonic_series.append(base_readings[i] * (i % 3 + 1) // max(1, i % 7))

# Real data path: filter anomalies using bit mask
effective_mask = 0b101010101010101
masked_indices = []
for i in range(len(base_readings)):
    if (i + 1) & effective_mask:
        masked_indices.append(i)

timing_buffer = [base_readings[i] for i in masked_indices]  # Critical data subset

# Distractor: spectral analysis (no impact on result)
spectral_weights = []
for x in timing_buffer:
    weight = 0
    for bit in range(8):
        weight += (x >> bit) & 1
    spectral_weights.append(weight)

# Fake fault propagation (misleading intermediate)
simulated_faults = []
current_state = 1
for flag in fault_flags:
    current_state = (current_state * 1103515245 + 12345) & 0x7FFFFFFF
    if flag:
        simulated_faults.append(current_state % 100)

# Red herring: unused sorting operation
sorted_diagnostics = sorted([sum(base_readings[i:i+3]) for i in range(0, len(base_readings), 3)])

# Meaningless counter accumulation (distraction)
stat_counter = Counter()
for val in base_readings:
    stat_counter[f'group_{val % 7}'] += val // 10

# Decoy function: never called but looks important
def compute_reliability_score(data, threshold=0.85):
    total = sum(data)
    valid = sum(1 for x in data if x > threshold * total / len(data))
    return valid / len(data)

# Conditional expression chain with slicing distraction
offset = len(timing_buffer) // 2
slice_a = timing_buffer[:offset]
slice_b = timing_buffer[offset:][::-1]

# Real logic: cross-correlation of slices with fault overlay
overlap_sum = 0
for a, b in itertools.zip_longest(slice_a, slice_b, fillvalue=0):
    overlap_sum += a * 2 - b

# Inject fault flag influence (only odd-indexed flags matter)
flag_correction = 0
for i, flag in enumerate(fault_flags):
    if i % 2 == 1 and flag:
        flag_correction += i * 3

# Core metric computation (uses overlap_sum and flag_correction)
raw_metric = overlap_sum + flag_correction

# Secondary distractor: recursive checksum (unused)
def recursive_checksum(seq):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    return seq[0] + recursive_checksum(seq[1:]) // 2

# Final aggregation function
def aggregate_metrics(buffer, flags):
    temp_result = 0
    # Use slice-based pattern matching
    for i in range(0, len(buffer) - 1, 2):
        temp_result += buffer[i] ^ buffer[i+1]  # XOR adjacent pairs
    
    # Incorporate fault flags through bit counting
    active_faults = sum(1 for f in flags if f)
    temp_result -= active_faults ** 2
    
    # Add constant derived from buffer properties
    pivot = buffer[len(buffer)//2]
    temp_result += pivot // 7
    
    return temp_result

# Execute critical statement
final_diagnostic = aggregate_metrics(timing_buffer, fault_flags)
print(f"Target result: {final_diagnostic}")