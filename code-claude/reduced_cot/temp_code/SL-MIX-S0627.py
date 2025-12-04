def generate_network_packet(protocol_type, data_length, priority=3):
    # Network packet header generation
    header_size = 12
    checksum = (data_length * 2) ^ (protocol_type << 4)
    
    # Priority encoding (unused in final calculation)
    priority_levels = {1: 'low', 2: 'medium', 3: 'high', 4: 'critical'}
    priority_code = ord(priority_levels.get(priority, 'medium')[0])
    
    # Protocol validation (distractor)
    valid_protocols = ['TCP', 'UDP', 'ICMP', 'ARP']
    protocol_map = {0: 'TCP', 1: 'UDP', 2: 'ICMP', 3: 'ARP'}
    current_protocol = protocol_map.get(protocol_type % 4, 'UNKNOWN')
    
    # Packet size calculation (relevant)
    total_size = header_size + data_length
    
    # Security parameters
    base_value = 0xA3
    mask = (protocol_type * 7) | (total_size & 0x1F)
    offset = sum([i for i in range(1, 6) if i % 2 == (total_size % 2)])
    
    # Traffic analysis (distractor)
    traffic_metrics = {
        'latency': [12, 15, 9, 11, 14],
        'bandwidth': [45, 62, 38, 51, 60]
    }
    avg_latency = sum(traffic_metrics['latency']) / len(traffic_metrics['latency'])
    
    # Sequence number generation (distractor)
    seq_base = total_size << 2
    seq_numbers = [seq_base + i*4 for i in range(3)]
    
    # Network addressing (distractor)
    subnet_mask = 0xFFFFFF00
    host_bits = ~subnet_mask & 0xFFFFFFFF
    available_hosts = host_bits - 1
    
    # Encryption key generation (main calculation)
    encryption_key = (base_value ^ (mask & 0xFF)) + offset
    
    # Error correction (distractor)
    error_codes = {code: f"ERR_{code:02x}" for code in range(16, 32, 4)}
    redundancy = len(error_codes) * 2
    
    # Final packet assembly
    packet = {
        "header": header_size,
        "protocol": current_protocol,
        "size": total_size,
        "checksum": checksum,
        "security": encryption_key
    }
    
    return packet

# Generate test packet
result = generate_network_packet(2, 48)
print(f"Target result: {result['security']}")