import itertools

def analyze_packets(packet_sequence):
    security_flag = 0b1010
    mask_pattern = 0b1100
    
    for idx, packet_size in enumerate(packet_sequence):
        # Apply XOR transformation with rotating mask
        transformed_size = packet_size ^ (mask_pattern << (idx % 4))
        
        # Check if transformed size meets suspicious criteria
        if (transformed_size > 50) and (transformed_size < 200):
            security_flag |= (1 << (idx % 8))
        elif not (transformed_size & 0b1111 == 0):
            security_flag &= ~(1 << (idx % 8))
        else:
            security_flag ^= (1 << (idx % 4))
    
    return security_flag

# Generate test packet sequences using list comprehension
network_traffic = [size for size in range(45, 75, 3)]
suspicious_packets = [p for p in network_traffic if p % 2 == 1]

# Process packets through multiple analytical layers
initial_flag = analyze_packets(suspicious_packets)

# Additional security layer processing
enhanced_flag = initial_flag
for i, pkt in enumerate(suspicious_packets[:4]):
    if (pkt & 0b11) == 0b10:
        enhanced_flag ^= (pkt >> 2)
    elif pkt > 55 or (enhanced_flag & (1 << i)):
        enhanced_flag |= (1 << (i + 4))
    else:
        enhanced_flag &= ~(1 << i)

# Final signature matching using itertools
signature_patterns = list(itertools.combinations([1, 2, 4, 8], 2))
match_count = 0
for pattern in signature_patterns:
    if (enhanced_flag & pattern[0]) and not (enhanced_flag & pattern[1]):
        match_count += 1

security_flag = enhanced_flag ^ (match_count << 3)
print(f"Result: {security_flag}")