import itertools

# Simulated sensor data with noise and metadata
data_packet = [18, 23, 14, 59, 24, 11, 97, 63, 44, 38]
noise_floor = [5, 3, 8, 2, 7, 1, 6, 4, 9, 0]
metadata_flags = [True, False, True, True, False, True, False, True, True, False]

# Irrelevant transformations (distractors)
distorted_signal = [((x + y) ** 2) % 17 for x, y in zip(data_packet, noise_floor)]
accumulated_bias = sum([i * val for i, val in enumerate(noise_floor)])
signal_envelope = max(distorted_signal) - min(distorted_signal)

# Real processing begins: extract valid indices based on metadata
valid_indices = [i for i, flag in enumerate(metadata_flags) if flag]
filtered_readings = [data_packet[i] for i in valid_indices]

# Compute rolling average of length 2 (unused - red herring)
rolling_averages = [(filtered_readings[i] + filtered_readings[i+1]) / 2 
                     for i in range(len(filtered_readings)-1)]

# Key computation: transform valid readings using modular arithmetic
elevated_readings = [(val ** 3) % 97 for val in filtered_readings]

# Bit manipulation layer (some relevant, some not)
bit_stuffed = [v ^ 0b1010 for v in elevated_readings]
popcount_filtered = [bin(v).count('1') for v in bit_stuffed]  # unused

# Core logic chain
shift_register = 0
for val in bit_stuffed:
    shift_register = (shift_register * 3 + val) % 65537

# Prime-based offset generation (depends on iteration count)
prime_lookup = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
prime_offset = prime_lookup[len(valid_indices) % 5]  # cycles every 5

# Decoy structure: complex but unused dictionary aggregation
decoys = {f"level_{i}": {"raw": data_packet[i], "adjusted": (data_packet[i] << 2) % 100, 
                        "status": metadata_flags[i]} for i in range(len(data_packet))}
summary_stats = {"total_packets": len(data_packet), "active_nodes": sum(metadata_flags), "baseline": accumulated_bias}

# Conditional override simulation (never triggers - misleading)
critical_threshold = 12345
if signal_envelope > critical_threshold:
    shift_register = (shift_register + 1000) % 65537  # dead code path

# Actual answer computation
modulus = 10007
valid_sequence_sum = sum(elevated_readings)
checksum = (valid_sequence_sum * prime_offset) % modulus

# Final unrelated transformation (distractor)
final_frame = [c ^ checksum for c in elevated_readings]

print(f"Result: {checksum}")