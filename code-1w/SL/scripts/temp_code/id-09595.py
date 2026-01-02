import itertools

# Simulated sensor data with noise and calibration flags
data_stream = [107, -53, 214, 89, 156, -12, 77, 223, 64, 198, 45, 111]
calibration_sequence = [True, False, True, True, False, True]
noise_threshold = 65
drift_compensation_factor = 0.92

# Irrelevant transformation: phase shift emulation (dead logic)
phase_shifted = [((x >> 3) ^ 17) & 0xF for x in data_stream]

# Decoy accumulator - looks important but unused later
total_drift = 0.0
for i, val in enumerate(data_stream):
    if i % 2 == 0:
        total_drift += abs(val) * drift_compensation_factor

# Simulate packet loss using cycle (itertools usage)
packet_mask = list(itertools.islice(itertools.cycle([True, True, False]), len(data_stream)))
masked_data = [val for i, val in enumerate(data_stream) if packet_mask[i]]

# Apply calibration filter using false pattern matching
valid_entries = []
calibration_cycle = itertools.cycle(calibration_sequence)
for val in masked_data:
    is_calibrated = next(calibration_cycle)
    magnitude = abs(val)
    if not is_calibrated:
        magnitude = abs(magnitude - 10)  # fake correction
    
    # Core filtering logic: only values above threshold and odd-indexed in masked set
    if magnitude > noise_threshold:
        if len(valid_entries) % 2 != 0:  # Every other valid addition
            valid_entries.append(magnitude)
        else:
            # Distraction: alternate path that modifies nothing
            temp_offset = magnitude // 10
            temp_offset -= temp_offset  # cancels out

# Critical statement
filtered_sum = sum(valid_entries)

# Red herring: bitwise obfuscation attempt (unused)
final_hash = 0
for x in valid_entries:
    final_hash ^= (x << 2) | (x >> 1)

# Output the target result
print(f"Result: {filtered_sum}")