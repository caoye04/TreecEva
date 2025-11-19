from collections import deque
import math

def process_packets(packet_ids):
    # Layer 1: Apply XOR with a shifting key
    layer1 = [pid ^ (pid << 2) for pid in packet_ids]
    
    # Layer 2: Exponentiate and normalize
    layer2 = [int(math.log(pid + 1)) if pid > 0 else 0 for pid in layer1]
    
    # Layer 3: Sort and apply deque-based transformation
    sorted_packets = sorted(layer2)
    packet_queue = deque(sorted_packets)
    
    # Simulate stack-like processing with bitwise AND reduction
    stack_reduction = 0
    while packet_queue:
        left = packet_queue.popleft()
        if packet_queue:
            right = packet_queue.pop()
            stack_reduction ^= (left & right)
        else:
            stack_reduction ^= left
    
    # Final checksum: Combine with lambda-based accumulator
    accumulator = lambda a, b: a + (b << 1) if b % 2 == 0 else a - (b >> 1)
    final_checksum = 0
    for val in sorted_packets:
        final_checksum = accumulator(final_checksum, val)
    
    # Adjust with stack reduction
    final_checksum ^= stack_reduction
    return final_checksum

# Simulate packet flow
network_packets = [12, 7, 23, 8, 15, 4]
final_checksum = process_packets(network_packets)
print(f"Result: {final_checksum}")