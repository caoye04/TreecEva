def analyze_network_traffic(packets):
    # Distractor variables
    total_bytes = 0
    filtered_count = 0
    protocol_stats = {}
    redundant_check = False
    
    # Main analysis with enumerate
    for i, packet in enumerate(packets):
        # Irrelevant computation
        total_bytes += len(packet) * 2 - len(packet)  # Pointless arithmetic
        
        # Distractor condition
        if i % 3 == 0:
            filtered_count += 1
            redundant_check = not redundant_check  # Dead state
        
        # Relevant logic
        if packet['size'] > 150 and packet['protocol'] == 'TCP':
            protocol_stats['tcp_large'] = protocol_stats.get('tcp_large', 0) + 1
        elif packet['size'] < 50:
            protocol_stats['small_packets'] = protocol_stats.get('small_packets', 0) + 1
    
    # Misleading intermediate calculation
    avg_size = total_bytes / len(packets) if packets else 0
    
    # Another distractor
    compression_ratio = (filtered_count * 1.5) / (len(packets) if packets else 1)
    
    # Key computation with bitwise operations
    base_count = protocol_stats.get('tcp_large', 0)
    small_count = protocol_stats.get('small_packets', 0)
    
    # Bit manipulation for final result
    result_mask = (base_count << 2) | (small_count & 0x0F)
    final_result = result_mask ^ 0b1010
    
    # Dead code path that looks important
    if compression_ratio > 2.0:
        final_result += 100  # Never executed
    
    print(f"Target result: {final_result}")
    return final_result

# Test data
packet_data = [
    {'size': 200, 'protocol': 'TCP'},
    {'size': 45, 'protocol': 'UDP'},
    {'size': 180, 'protocol': 'TCP'},
    {'size': 30, 'protocol': 'TCP'},
    {'size': 160, 'protocol': 'TCP'},
    {'size': 25, 'protocol': 'UDP'},
    {'size': 190, 'protocol': 'TCP'}
]

analyze_network_traffic(packet_data)