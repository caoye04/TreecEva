def analyze_network_packet(packet_data, header_size=12):
    # Network packet analysis simulator
    # Extracts and processes various packet fields
    
    # Configuration parameters (most are distractors)
    protocol_types = {
        1: "ICMP",
        6: "TCP",
        17: "UDP",
        47: "GRE"
    }
    error_codes = tuple(range(100, 600, 100))
    priority_levels = [3, 1, 4, 1, 5, 9, 2, 6]  # Based on network QoS
    
    # Initialize processing variables
    packet_length = len(packet_data)
    timestamp = 1654863420  # Unix timestamp for packet receipt
    sequence_num = ((packet_length * 17) & 0xFF) ^ 0x3A
    
    # Header processing - extract protocol type (distractor)
    if packet_length > header_size:
        protocol_id = packet_data[3] & 0x7F
        protocol_name = protocol_types.get(protocol_id, "UNKNOWN")
    else:
        protocol_name = "INVALID"
        return -1
    
    # Calculate checksum offset based on packet properties
    base_offset = packet_data[2] & 0x0F
    extended_offset = packet_data[5] >> 2
    
    # Distractor calculation - packet timing metrics
    transit_delay = timestamp % 100
    if transit_delay > 50:
        priority_index = transit_delay % len(priority_levels)
        priority = priority_levels[priority_index]
    else:
        priority = 0
    
    # Key position calculation
    position_factor = (packet_data[1] ^ packet_data[4]) & 0x3F
    position_modifier = packet_data[6] % 10
    raw_position = position_factor + position_modifier
    
    # Error handling section (distractor)
    error_condition = False
    if packet_data[0] > 200:
        error_code = error_codes[2]
        error_condition = True
    elif sequence_num < 20:
        error_code = error_codes[0]
        error_condition = True
    
    # Adjust position based on packet properties
    if error_condition and packet_data[7] > 100:
        effective_position = raw_position + 5
    else:
        # This is the key calculation
        effective_position = (raw_position * 2) % (packet_length - 5)
    
    # Extract various fields (most are distractors)
    source_port = (packet_data[8] << 8) | packet_data[9]
    destination_port = (packet_data[10] << 8) | packet_data[11]
    
    # Important: Extract the checksum value from the packet
    packet_checksum = 0
    if effective_position + 4 <= packet_length:
        # This is the key statement
        packet_checksum = packet_data[effective_position:effective_position+4]
        packet_checksum = sum(packet_checksum)
    
    # Verification (distractor)
    calculated_verification = (source_port ^ destination_port) & 0xFFFF
    if calculated_verification == 0:
        status = "VERIFIED"
    else:
        status = "UNVERIFIED"
    
    print(f"Result: {packet_checksum}")
    return packet_checksum

# Test with sample packet data
network_data = [132, 75, 18, 6, 43, 92, 7, 50, 192, 168, 1, 1, 10, 20, 30, 40, 50, 60, 70, 80]
result = analyze_network_packet(network_data)
