def analyze_packet_flow(packets):
    # Distractor: network flow analysis (unused)
    flow_rate = len(packets) * 0.25
    max_capacity = 1000
    utilization = (flow_rate / max_capacity) * 100
    return utilization

def filter_packets(packet_list, threshold):
    filtered = [p for p in packet_list if p <= threshold]
    # Distractor: misleading intermediate calculation
    avg_size = sum(packet_list) / len(packet_list) if packet_list else 0
    total_bandwidth = avg_size * 1.5  # Dead code path
    return filtered

def calculate_xor_sum(data):
    # Relevant: XOR operation chain
    result = 0
    for value in data:
        result ^= (value & 0xFF)  # Mask to byte range
    return result

def process_network_traffic(packets, config):
    # Distractor: configuration processing (unused)
    base_threshold = config['base']
    scaling_factor = config.get('scale', 1.0)
    dynamic_threshold = base_threshold * scaling_factor
    
    # Relevant: actual packet processing
    valid_packets = filter_packets(packets, base_threshold)
    
    # Distractor: unused analysis
    network_load = analyze_packet_flow(valid_packets)
    
    # Critical path: XOR calculation on valid packets
    checksum = calculate_xor_sum(valid_packets)
    
    # Final computation with bit manipulation
    final_result = (checksum << 2) | (len(valid_packets) & 0x3)
    
    # Distractor: misleading alternate result
    alternate_result = final_result ^ 0x55  # Dead code path
    
    return final_result

# Main execution
incoming_packets = [150, 80, 220, 65, 180, 95, 120, 200]
threshold_config = {'base': 150, 'scale': 1.2}

# Distractor: unused variables
total_packets = len(incoming_packets)
max_packet = max(incoming_packets)
min_packet = min(incoming_packets)

# Critical execution point
result = process_network_traffic(incoming_packets, threshold_config)

# Final output
final_output = result + (total_packets % 4)  # Minor adjustment

print(f"Target result: {final_output}")