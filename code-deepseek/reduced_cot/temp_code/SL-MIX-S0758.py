def calculate_network_efficiency(transmissions, sizes, limit):
    # Distractor: unused network metrics
    latency_stats = [45, 67, 89, 23, 156]
    jitter_analysis = sum(latency_stats) * 0.1
    
    # Relevant: packet filtering and processing
    filtered_packets = [size for size in sizes if size > 64]
    total_payload = sum(filtered_packets)
    
    # Misleading: bandwidth calculation (distractor)
    max_possible = limit * 1.25
    bandwidth_utilization = (total_payload / max_possible) * 100
    
    # Relevant: transmission efficiency calculation
    successful_transmissions = transmissions * 0.85  # 15% packet loss
    efficiency_factor = successful_transmissions / len(filtered_packets)
    
    # Distractor: unused network optimization
    compression_ratio = [0.6, 0.7, 0.8, 0.9]
    optimal_compression = max(compression_ratio) * 1.1
    
    # Relevant: final throughput calculation
    if total_payload > limit:
        actual_throughput = limit * efficiency_factor
    else:
        actual_throughput = total_payload * efficiency_factor
    
    # More distractors: protocol overhead calculations
    tcp_overhead = actual_throughput * 0.05
    udp_loss_factor = actual_throughput * 0.03
    
    return actual_throughput

# Main execution
packet_sizes = [128, 256, 512, 64, 1024, 32, 768]
transmission_count = 150
bandwidth_limit = 50000

# Distractor: unused network configuration
network_latency = [25, 30, 35, 40]
average_latency = sum(network_latency) / len(network_latency)

# Key execution
result = calculate_network_efficiency(transmission_count, packet_sizes, bandwidth_limit)
final_throughput = round(result, 2)

# More distractors: quality metrics (unused)
quality_scores = [8.5, 7.2, 9.1, 6.8]
mean_quality = sum(quality_scores) / len(quality_scores)

print(f"Target result: {final_throughput}")