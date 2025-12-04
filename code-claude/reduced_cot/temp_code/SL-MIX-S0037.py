def analyze_network_packets(packets, filter_flag=True):
    # Initialize tracking variables
    valid_packets = 0
    total_size = 0
    checksum = 0
    error_count = 0
    
    # Process each packet with its index
    for i, packet in enumerate(packets):
        # Extract packet data and apply initial processing
        packet_id = packet['id']
        packet_size = packet['size']
        packet_type = packet['type']
        
        # Calculate packet priority (unused in final result)
        priority = (packet_id * 3) % 10
        
        # Process only certain packet types if filter is enabled
        if filter_flag and packet_type not in ['DATA', 'ACK']:
            error_count += 1
            continue
            
        # Update packet statistics
        valid_packets += 1
        total_size += packet_size
        
        # Apply bit manipulation for packet verification
        if i % 2 == 0:
            checksum = (checksum + packet_size) & 0xFF
        else:
            checksum = (checksum ^ packet_id) & 0xFF
    
    # Calculate average packet size (not used in final calculation)
    avg_size = total_size / valid_packets if valid_packets > 0 else 0
    
    # Generate metrics report
    metrics = {
        'processed': valid_packets,
        'errors': error_count,
        'avg_size': avg_size
    }
    
    # Calculate hash based on processed packets
    base_hash = (valid_packets * 17) ^ total_size
    packet_hash = (base_hash + checksum) | 0x40
    
    # Apply final transformation to get result
    final_hash = (packet_hash & 0xFF) ^ checksum
    
    # These operations don't affect the result
    verification_code = (error_count << 4) | (valid_packets & 0xF)
    timestamp = sum([p['id'] for p in packets[-2:]], 0) if len(packets) >= 2 else 0
    
    print(f"Result: {final_hash}")
    return final_hash

# Test with sample packet data
packet_data = [
    {'id': 101, 'size': 64, 'type': 'DATA'},
    {'id': 102, 'size': 128, 'type': 'ACK'},
    {'id': 103, 'size': 32, 'type': 'SYN'},
    {'id': 104, 'size': 96, 'type': 'DATA'}
]

result = analyze_network_packets(packet_data)