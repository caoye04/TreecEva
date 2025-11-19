import itertools
from functools import reduce

def compute_custom_checksum(packet_ids):
    if len(packet_ids) < 2:
        return 0
    
    # Generate all unique pairs
    pairs = list(itertools.combinations(packet_ids, 2))
    
    # Compute XOR for each pair
    xor_results = [a ^ b for a, b in pairs]
    
    # Reduce using bitwise AND
    checksum = reduce(lambda x, y: x & y, xor_results)
    return checksum

# Packet identifiers in hexadecimal
network_packets = [0x1F, 0x2C, 0x3A, 0x45]
security_checksum = compute_custom_checksum(network_packets)
print(f"Result: {security_checksum}")