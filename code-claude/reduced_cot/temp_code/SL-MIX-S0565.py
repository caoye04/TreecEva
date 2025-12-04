def analyze_network_packet(packet_data, header_size=16):
    # Packet analysis function for network traffic prioritization
    raw_data = packet_data.strip().lower()
    
    # Extract packet type from first segment
    packet_type = raw_data[:4]
    
    # Calculate checksum (unused in priority calculation)
    checksum = 0
    for i in range(len(raw_data)):
        if i % 2 == 0:
            checksum += ord(raw_data[i])
        else:
            checksum -= ord(raw_data[i])
    checksum = abs(checksum) % 256
    
    # Priority calculation based on packet type and contents
    priority_map = {
        'data': 100,
        'ctrl': 200,
        'mgmt': 50,
        'voip': 150
    }
    
    # Extract protocol version (misleading calculation)
    protocol_version = sum([ord(c) for c in raw_data[4:8]]) % 10
    
    # Calculate base priority
    base_priority = priority_map.get(packet_type, 75)
    
    # Apply adjustments based on packet contents
    urgent_flag = 'urgent' in raw_data
    encrypted = raw_data.endswith('enc')
    fragmented = '-f' in raw_data
    
    # Priority adjustments
    priority_value = base_priority
    
    if urgent_flag:
        priority_value += 25
    elif fragmented:
        priority_value -= 10
    
    # Secondary priority calculation (never used)
    alt_priority = min(255, base_priority * (protocol_version + 1) // 2)
    
    # Apply encryption modifier
    if encrypted:
        priority_value = max(1, priority_value + 15)
    
    # Apply header size adjustment
    header_modifier = min(header_size, 32) // 8
    priority_value += header_modifier
    
    # Calculate hop count from packet data
    hop_count = 0
    for i in range(min(len(raw_data), 10)):
        if raw_data[i] in 'aeiou':
            hop_count += 1
    
    # Adjust priority based on hop count (this is applied)
    if hop_count > 3:
        priority_value += hop_count
    
    # Convert to hexadecimal representation for routing
    hex_priority = hex(priority_value)[2:].zfill(4)
    
    # Calculate routing metric (unused)
    routing_metric = (priority_value * protocol_version) % 100
    
    # Bit manipulation for encryption
    encrypted_priority = ((priority_value & 0xFF) << 4) | ((priority_value & 0xF00) >> 8)
    
    # Final QoS marking (unused)
    qos_mark = (encrypted_priority & 0xFF) ^ checksum
    
    return {
        'type': packet_type,
        'priority': priority_value,
        'encrypted_priority': encrypted_priority,
        'checksum': checksum
    }

# Process a sample packet
packet = "ctrl-urgent-packet-v3-enc"
result = analyze_network_packet(packet)
print(f"Result: {result['encrypted_priority']}")