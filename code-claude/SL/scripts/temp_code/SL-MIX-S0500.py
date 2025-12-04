def analyze_network_packets(packets):
    # Network packet analysis simulation
    active_connections = [True, False, True, True, False]
    packet_sizes = [64, 128, 256, 512, 1024]
    error_count = 0
    
    # Process packets with various filters
    filtered_packets = [p for p in packets if p % 3 != 0]  # Filter out packets divisible by 3
    
    # Track network metrics (not relevant to final calculation)
    total_bytes = sum(packet_sizes)
    avg_packet_size = total_bytes / len(packet_sizes) if packet_sizes else 0
    network_load = total_bytes * (sum(active_connections) / len(active_connections))
    
    # Security check calculations
    security_level = 4
    encryption_overhead = 16
    timestamp = 1234567890
    
    # Analyze packet integrity
    corrupted = False
    for i, packet in enumerate(filtered_packets):
        if i >= len(packets) - 2:
            break
            
        # Check for potential security threats
        threat_level = (packet & 0x0F) + security_level
        if threat_level > 10:
            error_count += 1
            if error_count > 3:
                corrupted = True
                break
    
    # Generate hash value from filtered packets
    hash_value = 0
    for p in filtered_packets:
        hash_value = ((hash_value << 3) | (hash_value >> 29)) & 0xFFFFFFFF
        hash_value ^= p
    
    # Calculate protocol version from timestamp
    protocol_version = (timestamp % 100) // 10
    
    # Prepare decryption components
    key_parts = [0xA5, 0xF1, 0x3C, 0x77, 0xBE, 0x2D, 0x8F]
    valid_index = 0
    
    # Find valid index based on packet analysis
    for i, packet in enumerate(packets):
        if i < len(key_parts) and packet % 2 == 0:
            valid_index = (valid_index + (packet & 0x07)) % len(key_parts)
    
    # These calculations don't affect the result
    checksum = sum([p & 0xFF for p in packets]) % 256
    integrity_factor = (checksum * protocol_version) % 100
    redundancy_code = (integrity_factor + encryption_overhead) & 0xFF
    
    # Generate the decryption key
    decryption_key = key_parts[valid_index] ^ (hash_value & 0xFF)
    
    # Verify the key with alternative approach (unused)
    verification = 0
    for i in range(5):
        verification = (verification + key_parts[i % len(key_parts)]) & 0xFF
        if i == protocol_version:
            verification ^= 0x42
    
    print(f"Result: {decryption_key}")
    return decryption_key

# Test with sample data
packet_data = [18, 24, 12, 42, 30, 50]
result = analyze_network_packets(packet_data)