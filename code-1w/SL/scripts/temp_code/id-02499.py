from collections import defaultdict

# Simulate a data integrity tracker with redundant computations
data_stream = [183, 92, 47, 155, 212, 68, 134, 77]
weights = [0.1, 0.3, 0.1, 0.2, 0.05, 0.15, 0.02, 0.03]

# Irrelevant weighted average calculation (distractor)
weighted_avg = sum(data_stream[i] * weights[i] for i in range(len(data_stream)))

# State tracking variables
state_log = defaultdict(int)
running_xor = 0
buffer_sum = 0

# Primary processing cycle with slicing and modular arithmetic
for i in range(0, len(data_stream), 2):
    chunk = data_stream[i:i+2]  # Slice into pairs
    if len(chunk) == 2:
        # Meaningful XOR chain
        running_xor ^= (chunk[0] ^ chunk[1])

        # Buffer sum accumulates sum of chunks (semi-relevant)
        buffer_sum += sum(chunk)

    # Update state log (some distraction)
    for val in chunk:
        state_log[val] += 1

# Secondary transformation: cyclic sum with bit manipulation
cycle_sum = 0
for _ in range(3):
    for val in data_stream[::3]:  # Stride slicing
        cycle_sum += (val >> 2) & 15  # Shift and mask

cycle_sum = cycle_sum ** 2  # Nonlinear boost (moderately relevant)

# Red herring: unused recursive function
def recursive_checksum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] ^ recursive_checksum(arr, idx + 1)

# Unused but plausible-looking call
unused_result = recursive_checksum(data_stream[:4])

# Final checksum computation combining XOR and modular state
temp_factor = buffer_sum // 8
final_xor = running_xor ^ temp_factor

# Key statement — answer depends on this
checksum = final_xor ^ (cycle_sum % 256)

# Irrelevant dead-end branch
if len(state_log) > 10:
    checksum *= 2

print(f"Result: {checksum}")