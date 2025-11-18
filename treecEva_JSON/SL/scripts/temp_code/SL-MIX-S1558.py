import math
from functools import reduce

# Packet weight definitions
packet_weights = {f'P{i}': i*3 + 7 for i in range(1, 9)}
transform_map = {k: v**2 % 17 for k, v in packet_weights.items()}

# Apply logarithmic gain adjustment
adjusted_weights = {k: math.log(v + 1) for k, v in transform_map.items()}

# Filter packets with even transformed weights
valid_packets = {k: v for k, v in adjusted_weights.items() if int(transform_map[k]) % 2 == 0}

# Calculate base sync using modular exponentiation
base_sync = reduce(lambda x, y: (x + y) % 13, [int(v) for v in valid_packets.values()], 0)

# Dynamic programming table for cumulative adjustments
dp_table = [0] * (len(valid_packets) + 1)
items = list(valid_packets.values())
for i in range(1, len(dp_table)):
    dp_table[i] = (dp_table[i-1] + int(items[i-1] * 10)) % 7

# Binary search for optimal adjustment factor
arr = [x for x in dp_table if x > 0]
low, high = 0, len(arr) - 1
optimal_index = -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] % 3 == 1:
        optimal_index = mid
        high = mid - 1
    else:
        low = mid + 1

# Compute final synchronization score
sync_score = (base_sync * (optimal_index + 1)) % 11
print(f"Result: {sync_score}")