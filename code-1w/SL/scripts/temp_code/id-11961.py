def analyze_pattern(sequence):
    return [sequence[i] ^ sequence[-i-1] for i in range(len(sequence)//2)]

transmission_key = [3, 7, 2, 8, 1, 9, 4, 6]
correction_factor = sum(transmission_key) // len(transmission_key)

# Simulate signal chunking and noise filtering
raw_data_stream = [i * (i + correction_factor) for i in range(1, 10)]
filtered_segments = raw_data_stream[::2]  # Take every other segment

# Misleading intermediate processing (distractor)
decoy_signal = [x % correction_factor for x in filtered_segments if x > 15]
buffer_analysis = [x for x in decoy_signal if x in transmission_key]

# Actual relevant processing begins
signal_chunks = filtered_segments[:4]

# Apply transformation using slice reversal and XOR masking
masked_chunks = []
for idx, chunk in enumerate(signal_chunks):
    shifted = chunk >> 1
    masked = shifted ^ transmission_key[idx]
    masked_chunks.append(masked)

# Secondary validation (partially relevant)
validation_check = 0
for val in masked_chunks:
    if val % 2 == 0:
        validation_check += 1

# Core logic: recursive reduction of masked chunks
def reduce_signal(data, acc=0):
    if not data:
        return acc
    return reduce_signal(data[1:], acc + (data[0] & (acc | 1)))

intermediate_sum = reduce_signal(masked_chunks)

# Final adjustment based on correction factor and pattern symmetry
symmetry_test = analyze_pattern(transmission_key)
adjustment = len(symmetry_test) * (correction_factor - validation_check)

final_signal = intermediate_sum + adjustment

# Output result as required
print(f"Result: {final_signal}")