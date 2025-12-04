def process_network_packet(packet_data):
    # Parse hexadecimal packet data into bytes
    raw_bytes = [int(packet_data[i:i+2], 16) for i in range(0, len(packet_data), 2)]
    
    # Some statistical calculations that aren't directly used
    avg_byte = sum(raw_bytes) / len(raw_bytes) if raw_bytes else 0
    variance = sum((b - avg_byte) ** 2 for b in raw_bytes) / len(raw_bytes) if raw_bytes else 0
    
    # Process packet header (first 4 bytes)
    header = raw_bytes[:4] if len(raw_bytes) >= 4 else []
    version = (header[0] & 0xF0) >> 4 if header else 0
    
    # Apply packet filtering rules
    protocol_type = header[2] if len(header) > 2 else 0
    priority = header[3] % 8 if len(header) > 3 else 0
    
    # Additional metrics that don't affect the result
    metrics = {
        'max_value': max(raw_bytes) if raw_bytes else 0,
        'min_value': min(raw_bytes) if raw_bytes else 0,
        'distinct': len(set(raw_bytes))
    }
    
    # Filter bytes based on specific conditions
    is_high_priority = lambda p: p >= 5
    bytes_to_keep = []
    
    # Process payload bytes
    payload = raw_bytes[4:] if len(raw_bytes) > 4 else []
    for i, byte in enumerate(payload):
        # Skip bytes at even positions for certain protocol types
        if protocol_type == 6 and i % 2 == 0:
            continue
            
        # Apply priority filtering
        if is_high_priority(priority) or (byte % 2 == 1):
            # Keep bytes that pass either condition
            bytes_to_keep.append(byte)
    
    # Calculate checksum (unused in final result)
    checksum = 0
    for b in raw_bytes:
        checksum = (checksum + b) % 256
    
    # Calculate final result
    filtered_bytes = sum(bytes_to_keep)
    
    # Some string operations that aren't used in the result
    packet_info = f"V{version}:P{protocol_type}:{priority}"
    packet_info = packet_info.lower().replace(':', '-')
    
    print(f"Result: {filtered_bytes}")
    return filtered_bytes

# Test with sample packet
packet_data = "1A276F3982C4D21B"
result = process_network_packet(packet_data)