import heapq
import math
from collections import deque

def calculate_base_priority(seq_id, timestamp):
    xor_result = seq_id ^ (timestamp << 2)
    return xor_result & 0xFF

def adjust_with_log(priority):
    if priority <= 0:
        return 0
    return int(math.log2(priority) * 10) & 0x7F

def apply_exponential_mod(value, mod_factor):
    exp_val = min(10, value >> 2)
    return (value ^ mod_factor) & ((1 << exp_val) - 1)

# Initialize components
packet_queue = []
reorder_stack = deque()
sequence_ids = [37, 89, 144, 233]
timestamps = [12, 28, 45, 77]
mod_constants = [0x15, 0x3C, 0x7F, 0xAA]

# Process packets
for i in range(len(sequence_ids)):
    base_pri = calculate_base_priority(sequence_ids[i], timestamps[i])
    adj_pri = adjust_with_log(base_pri)
    mod_pri = apply_exponential_mod(adj_pri, mod_constants[i])
    heapq.heappush(packet_queue, (-mod_pri, i))  # Max heap using negative values

# Reorder using stack
while packet_queue:
    _, idx = heapq.heappop(packet_queue)
    reorder_stack.append((sequence_ids[idx] & 0xF) | ((timestamps[idx] & 0xF) << 4))

# Calculate final signal strength
final_signal_strength = 0
while reorder_stack:
    val = reorder_stack.pop()
    final_signal_strength = (final_signal_strength << 3) ^ val
    final_signal_strength &= 0xFFFF

print(f"Result: {final_signal_strength}")