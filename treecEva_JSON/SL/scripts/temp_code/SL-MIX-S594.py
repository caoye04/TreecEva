def analyze_packets():
    # Encoded network packets in hex
    packet_data = ['0x4F', '0x7A', '0xC3', '0x9B', '0xE7']
    
    # Convert hex to binary strings without '0b' prefix
    binary_packets = [bin(int(packet, 16))[2:].zfill(8) for packet in packet_data]
    
    # Initialize threat metrics
    threat_indicators = {
        'high_bit_sequence': 0,
        'alternating_pattern': 0,
        'consecutive_ones': 0
    }
    
    # Process each binary packet
    for packet in binary_packets:
        # Count high bit sequences (bits 7-5 are all 1s)
        if packet[:3] == '111':
            threat_indicators['high_bit_sequence'] += 1
            
        # Check for alternating pattern starting with 1
        is_alternating = True
        for i in range(len(packet)-1):
            if packet[i] == packet[i+1]:
                is_alternating = False
                break
        if is_alternating and packet[0] == '1':
            threat_indicators['alternating_pattern'] += 1
            
        # Count consecutive ones
        max_consecutive = 0
        current_count = 0
        for bit in packet:
            if bit == '1':
                current_count += 1
                max_consecutive = max(max_consecutive, current_count)
            else:
                current_count = 0
        threat_indicators['consecutive_ones'] += max_consecutive
    
    # Calculate final intrusion score using weighted factors
    weights = {'high_bit_sequence': 3, 'alternating_pattern': 5, 'consecutive_ones': 2}
    intrusion_score = sum(threat_indicators[key] * weights[key] for key in threat_indicators)
    
    # Apply penalty for specific pattern combinations
    if threat_indicators['high_bit_sequence'] > 2 and threat_indicators['consecutive_ones'] > 15:
        intrusion_score -= 4
        
    return intrusion_score

# Execute analysis
intrusion_score = analyze_packets()
print(f"Result: {intrusion_score}")