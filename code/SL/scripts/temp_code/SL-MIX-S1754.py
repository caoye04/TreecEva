from collections import deque

def verify_packet_chain(signatures):
    mask = 0b10101010
    valid_packets = deque()
    max_chain_length = 0
    
    for i, sig in enumerate(signatures):
        # Apply bitwise transformations
        transformed_sig = ((sig << 2) & 0xFF) ^ mask
        
        # Greedy validation: only add if improves chain
        if not valid_packets or (transformed_sig & valid_packets[-1]) == 0:
            valid_packets.append(transformed_sig)
        else:
            # Replace last element if current creates better chain potential
            if len(valid_packets) > 1 and (transformed_sig & valid_packets[-2]) == 0:
                valid_packets.pop()
                valid_packets.append(transformed_sig)
        
        # Update maximum chain length
        max_chain_length = max(max_chain_length, len(valid_packets))
    
    return max_chain_length

# Packet signatures to process
packet_signatures = [0x15, 0x2A, 0x3C, 0x4D, 0x5E, 0x6F]
max_chain_length = verify_packet_chain(packet_signatures)
print(f"Result: {max_chain_length}")