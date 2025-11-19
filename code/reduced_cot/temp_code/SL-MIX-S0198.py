def process_network_packet():
    # Initial packet data as hex values
    raw_packets = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
    
    # Step 1: Apply XOR chaining with rotating key
    xor_key = 0x7F
    chained_values = []
    for i, packet in enumerate(raw_packets):
        rotated_key = ((xor_key << (i % 5)) | (xor_key >> (8 - (i % 5)))) & 0xFF
        chained_value = packet ^ rotated_key
        chained_values.append(chained_value)
    
    # Step 2: Filter unique values using set operations
    unique_packets = list(set(chained_values))
    
    # Step 3: Apply arithmetic transformation with lambda
    transform = lambda x: (x * 3 + 7) % 256
    transformed_packets = [transform(p) for p in unique_packets]
    
    # Step 4: Compute hash-based identifier for the packet group
    packet_string = ''.join([hex(p)[2:] for p in transformed_packets])
    hash_id = sum(ord(c) for c in packet_string) & 0xFF
    
    # Step 5: Final checksum calculation using bitwise operations
    checksum_components = [p ^ hash_id for p in transformed_packets]
    intermediate_sum = sum(checksum_components) & 0xFFFF
    
    # Step 6: Apply final transformation mixing arithmetic and bitwise ops
    final_checksum = ((intermediate_sum >> 8) & 0xFF) | ((intermediate_sum & 0xFF) << 8)
    
    return final_checksum

# Execute the packet processing pipeline
final_checksum = process_network_packet()
print(f"Result: {final_checksum}")