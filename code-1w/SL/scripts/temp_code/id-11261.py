from itertools import cycle

# Simulate data stream processing with error detection logic
data_stream = [13, 17, 23, 29, 31]
key_sequence = [7, 11, 5]

# Initialization of state variables
count = 0
running_sum = 0
temp_buffer = []

# Misleading pre-processing: summing unrelated combinations
for i in range(len(data_stream)):
    for j in range(i + 1, len(data_stream)):
        temp_buffer.append((data_stream[i] + data_stream[j]) % 10)

# Actual computation begins here
checksum = 0
mask = 0xF0  # Upper nibble mask
position = 0

# Real processing: interleaving data and key via cyclic pattern
data_and_key = list(zip(data_stream, cycle(key_sequence)))

for value, key in data_and_key:
    # Irrelevant transformation (dead-end calculation)
    shifted = (value << 2) & 0xFF
    inverted = (~shifted) & 0xFF
    
    # Semi-relevant operation (used in running_sum but not final result)
    running_sum += value * key % 13
    
    # Key update step: checksum updated with XOR and mask
    checksum = (checksum + value) ^ mask
    
    # Position tracking (not used in final answer)
    position += 1
    if position == 3:
        backup_checksum = checksum  # Red herring: saved but unused

# Additional distraction: post-loop manipulation that doesn't affect result
final_shift = (checksum >> 4) | (checksum << 4)
parity = bin(checksum).count('1') % 2

# Output the target result
print(f"Result: {checksum}")