from itertools import compress, count

# Simulated sensor readings with noise and metadata
data_stream = [101, 104, 105, 110, 99, 108, 117, 115, 101, 100, 68, 97, 116, 97]
noise_floor = 100
activation_threshold = 103

# Irrelevant transformation: ASCII decoding (distractor)
decoded = ''.join(chr(b) for b in data_stream if 32 <= b <= 126)

# Relevant: Extract values above noise floor but below threshold (signal envelope)
signal_mask = [(x > noise_floor and x < activation_threshold) for x in data_stream]
filtered_signal = list(compress(data_stream, signal_mask))

# Dead path: Unused alternative filtering
alt_filter = list(filter(lambda x: x % 2 == 0, data_stream))

# Simulate time-series gaps (decoy structure)
timestamps = list(zip(count(start=1000, step=5), data_stream))
gap_analysis = [t2 - t1 for t1, t2 in zip(timestamps, timestamps[1:])]

# Key processing: sum of filtered signal
sum_filtered = sum(filtered_signal)

# Red herring: checksum variant using alt data
pseudo_checksum = sum(alt_filter) ^ 255

# Critical operation: finalize via bit manipulation and scaling
def finalize(value):
    shifted = (value << 3) & 0xFFFF
    rotated = ((shifted >> 4) | (shifted << 12)) & 0xFFFF
    return rotated ^ 0xAA55

counterfeit = finalize(sum_filtered) & 0xFF  # Misleading partial use

# Main result computation
checksum = finalize(sum_filtered) // 10

# Print target result
print(f"Result: {checksum}")