def analyze_network_packets(packet_data):
    # Irrelevant network simulation setup
    max_bandwidth = 1000
    min_latency = 5
    protocol_headers = ['TCP', 'UDP', 'ICMP', 'HTTP']
    
    # Distractor calculations that don't affect final result
    total_bytes = sum(len(p) for p in packet_data)
    avg_packet_size = total_bytes / len(packet_data) if packet_data else 0
    protocol_distribution = {proto: 0 for proto in protocol_headers}
    
    # Relevant data processing with slicing and enumerate
    valid_packets = []
    for i, packet in enumerate(packet_data):
        if i % 2 == 0:  # Skip every other packet (misleading condition)
            continue
        if len(packet) > 10:  # Actual filtering condition
            valid_packets.append(packet)
    
    # More irrelevant computations
    redundant_sum = sum(ord(c) for packet in packet_data for c in packet[:3])
    temp_buffer = [x * 2 for x in range(len(packet_data))]
    
    # Critical logic section with zip
    source_dest_pairs = list(zip(packet_data[::2], packet_data[1::2]))
    processed_pairs = []
    for src, dst in source_dest_pairs:
        if src and dst:  # Dead code path - always true
            processed_pairs.append((len(src), len(dst)))
    
    # Key variables for final calculation
    valid_count = len(valid_packets)
    weight_factor = 3
    offset_value = 7
    
    # Final answer computation
    final_metric = valid_count * weight_factor - offset_value
    
    # Print result
    print(f"Result: {final_metric}")
    return final_metric

# Test data
packet_samples = ['data_packet_001', 'data_packet_002_extra', 'cmd_003', 
                  'response_004_longer', 'ack_005', 'sync_006_extended',
                  'fin_007', 'rst_008_special']

# Execute
result = analyze_network_packets(packet_samples)