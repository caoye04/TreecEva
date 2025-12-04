def analyze_network_packets(raw_data, filter_flag=True):
    # Initialize packet counters for different protocols
    network_traffic = {
        'TCP': 0,
        'UDP': 0,
        'ICMP': 0,
        'HTTP': 0,
        'HTTPS': 0
    }
    
    # Parse raw data (simulated packet data)
    packets = raw_data.split('|')
    
    # Flags for special protocol handling
    apply_security_filter = filter_flag and len(packets) > 5
    prioritize_encrypted = any(p.count('S') > 2 for p in packets)
    
    # Process each packet
    for packet in packets:
        if not packet.strip():
            continue
            
        # Extract protocol (first character) and size (sum of character values)
        protocol = packet[0].upper()
        packet_size = sum(ord(c) for c in packet)
        
        # Update traffic counters based on protocol
        if protocol == 'T':
            network_traffic['TCP'] += 1
            security_score = packet.count('S') * 2
        elif protocol == 'U':
            network_traffic['UDP'] += 1
            security_score = packet.count('S')
        elif protocol == 'I':
            network_traffic['ICMP'] += 1
            security_score = packet.count('S') * 3
        elif protocol == 'H':
            if 'S' in packet:
                network_traffic['HTTPS'] += 1
            else:
                network_traffic['HTTP'] += 1
            security_score = packet.count('S') * 4
        
        # Apply security adjustments (not relevant to final result)
        if apply_security_filter and security_score > 5:
            potential_threats = packet_size & 0xFF
            blocked_packets = potential_threats >> 2
        
    # Calculate traffic metrics (distractors)
    total_packets = sum(network_traffic.values())
    encrypted_ratio = (network_traffic['HTTPS'] / total_packets) if total_packets > 0 else 0
    vulnerability_index = (network_traffic['UDP'] * 2 + network_traffic['ICMP'] * 3) & 0x1F
    
    # Determine primary and secondary protocols
    protocol_ranking = sorted(network_traffic.items(), key=lambda x: x[1], reverse=True)
    primary_protocol = protocol_ranking[0][0]
    secondary_protocol = protocol_ranking[1][0]
    
    # Calculate alternate metrics (distractors)
    alternate_score = network_traffic[primary_protocol] * 2
    if prioritize_encrypted:
        weighted_score = network_traffic['HTTPS'] * 3 + network_traffic['TCP']
        risk_factor = vulnerability_index ^ (weighted_score & 0x0F)
    else:
        weighted_score = network_traffic['TCP'] * 2 + network_traffic['UDP']
        risk_factor = (vulnerability_index + weighted_score) % 32
    
    # Target calculation - sum of primary and secondary protocol counts
    target_value = network_traffic[primary_protocol] + network_traffic.get(secondary_protocol, 0)
    
    # Final processing (distractor)
    if apply_security_filter:
        adjusted_target = target_value ^ risk_factor
    else:
        adjusted_target = target_value + (vulnerability_index // 2)
    
    print(f"Network analysis complete. Protocol distribution: {network_traffic}")
    print(f"Primary protocol: {primary_protocol}, Secondary protocol: {secondary_protocol}")
    print(f"Target result: {target_value}")
    return target_value

# Sample network data
raw_network_data = "T123|U456S|ICMP789S|HTTPS123SS|TCP456|UDP789S|TSS123|ICMPSS|"
result = analyze_network_packets(raw_network_data)
