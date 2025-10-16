import heapq
from collections import defaultdict

def decode_layer(encoded, shift):
    return ''.join(chr(ord(c) - shift) for c in encoded)

def encode_layer(decoded, shift):
    return ''.join(chr(ord(c) + shift) for c in decoded)

def is_balanced_signature(sig):
    if not sig:
        return True
    stack = []
    for char in sig:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def filter_valid_signatures(signatures):
    return {sig for sig in signatures if is_balanced_signature(sig)}

def process_packets(packet_data):
    registry = frozenset(['abc', 'def', 'ghi'])
    heap = []
    
    for packet in packet_data:
        decoded = decode_layer(packet['sig'], packet['shift'])
        if decoded in registry:
            priority = sum(ord(c) for c in decoded)
            heapq.heappush(heap, (priority, decoded))
    
    validated = set()
    while heap:
        _, sig = heapq.heappop(heap)
        encoded = encode_layer(sig, 1)
        validated.add(encoded)
    
    return validated

# Packet transformation pipeline
packets = [
    {'sig': 'cde', 'shift': 2},
    {'sig': 'efg', 'shift': 3},
    {'sig': 'ijk', 'shift': 1},
    {'sig': 'bcd', 'shift': 1}
]

# Process all packets through security layers
processed_signatures = process_packets(packets)

# Apply final validation filter
final_validated = filter_valid_signatures(processed_signatures)

# What is the size of the final validated signatures?
result = len(final_validated)
print(f"Result: {result}")