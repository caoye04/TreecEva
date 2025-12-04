from collections import Counter, defaultdict

def process_network_packets(packets, security_level=3):
    # Initialize packet processing variables
    packet_buffer = []
    noise_threshold = 42
    security_constant = 0x5A3C
    
    # Track packet statistics (not relevant to final result)
    packet_stats = defaultdict(int)
    protocol_counter = Counter()
    
    # Process each packet in the sequence
    accumulated_hash = 0
    for i, packet in enumerate(packets):
        # Extract packet data (source, destination, payload)
        src, dest, payload = packet
        
        # Track protocol usage (distraction)
        protocol = src & 0xFF
        protocol_counter[protocol] += 1
        
        # Calculate noise level (distraction)
        noise_level = (dest * 17) % 256
        if noise_level > noise_threshold:
            packet_stats['noisy'] += 1
            continue  # Skip noisy packets (dead path - never happens with our input)
        
        # Process payload with shifting algorithm
        encoded_value = 0
        for j, byte in enumerate(payload):
            # Alternate between left and right shifts
            if j % 2 == 0:
                encoded_value = (encoded_value << 3) | (byte & 0x7)
            else:
                encoded_value = (encoded_value >> 2) ^ (byte & 0xF)
        
        # Accumulate hash with bitwise operations
        if i % 3 == 0:
            accumulated_hash = accumulated_hash ^ encoded_value
        elif i % 3 == 1:
            accumulated_hash = (accumulated_hash + encoded_value) & 0xFFFF
        else:
            accumulated_hash = (accumulated_hash * 7 + encoded_value) & 0xFFFF
    
    # Apply security transformations
    potential_threats = sum(1 for p in packets if p[0] > 1000)  # Distraction
    mask = 0xFFFF >> (4 - security_level)  # Only lower bits based on security level
    
    # Generate final signature
    checksum = sum(p[2][0] if p[2] else 0 for p in packets)  # Distraction
    final_signature = (accumulated_hash & mask) ^ security_constant
    
    # Calculate alternative signatures (distractions)
    alt_signature1 = checksum ^ security_constant
    alt_signature2 = (accumulated_hash + checksum) & 0xFFFF
    
    # Print results for verification
    print(f"Processed {len(packets)} packets with {potential_threats} potential threats")
    print(f"Protocol distribution: {dict(protocol_counter)}")
    print(f"Alternative signature options: {alt_signature1}, {alt_signature2}")
    print(f"Result: {final_signature}")
    
    return final_signature

# Network packet data: [(source, destination, payload)]
network_data = [
    (145, 8080, [18, 52, 86]),
    (892, 443, [67, 23, 81]),
    (512, 22, [90, 43, 16]),
    (1024, 80, [37, 48, 92]),
    (768, 8443, [12, 29, 55])
]

# Process packets with medium security level
result = process_network_packets(network_data, security_level=3)