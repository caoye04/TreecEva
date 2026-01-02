from itertools import compress, cycle

# Simulated sensor data stream with metadata tags
data_stream = [107, 214, 198, 231, 156, 173, 204, 189]
timestamp_flags = [True, False, True, True, False, True, False, True]

# Irrelevant transformation: amplitude normalization (distractor)
normalized = [round(x * 0.95 + 2.1, 1) for x in data_stream]
offset_correction = sum(normalized) / len(normalized)

# Decoy checksum using mean deviation (not used in final result)
mean_val = sum(data_stream) / len(data_stream)
deviation_score = sum(abs(x - mean_val) for x in data_stream) / len(data_stream)
temp_hash = int(deviation_score * 100) ^ 0xAA

# Control flow mask based on timestamp reliability
reliable_mask = list(compress(data_stream, timestamp_flags))
interleaved = list(zip(reliable_mask, cycle([7, -3])))

# Spurious data expansion (dead path)
expanded = []
for val, delta in interleaved:
    expanded.append(val + delta)
    expanded.append(val - delta)

# Real processing path begins here (non-obvious due to prior noise)
filtered = [x for x in data_stream if x > 180]  # Only high-energy readings
rolling_window = [filtered[i] ^ filtered[i+1] for i in range(len(filtered)-1)]
accumulated = 0
for w in rolling_window:
    accumulated = (accumulated << 1) ^ w  # Bit-shifting accumulator

# Secondary parallel computation: position-sensitive adjustment
position_weights = [i * 2 + 1 for i in range(len(data_stream))]
weighted_sum = sum(data_stream[i] * position_weights[i] for i in range(len(data_stream)))
adjustment = (weighted_sum // 100) & 0xFFFF

# Determine valid sequence from bit pattern analysis
bit_density = sum(1 for x in data_stream if bin(x).count('1') % 2 == 0)
parity_state = bit_density >= 4
valid_sequence = accumulated if parity_state else accumulated ^ 0xFFFF

# Final computation buried among distractions
modulus = 98765
checksum = (valid_sequence ^ adjustment) % modulus

# Red herring output (misleading)
fake_checksum = (temp_hash + len(expanded)) % 50000

# Critical output statement
print(f"Result: {checksum}")