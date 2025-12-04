def calculate_network_metrics():
    packet_sizes = [512, 1024, 768, 2048, 1536, 512, 2560, 1024]
    bandwidth_limit = 1500
    
    # Filter packets that exceed bandwidth limit
    filtered_packets = [size for size in packet_sizes if size <= bandwidth_limit]
    
    # Calculate some intermediate metrics (distraction)
    total_size = sum(packet_sizes)
    average_size = total_size / len(packet_sizes)
    
    # Process packet sequence
    processed_packets = []
    for packet in filtered_packets:
        # Add some processing overhead (distraction)
        processed = packet + 32
        processed_packets.append(processed)
    
    # Final throughput calculation
    if len(processed_packets) > 0:
        final_throughput = processed_packets[-1]
    else:
        final_throughput = 0
    
    # More distraction calculations
    theoretical_max = max(packet_sizes) * 2
    efficiency_ratio = total_size / theoretical_max
    
    print(f"Result: {final_throughput}")
    return final_throughput

calculate_network_metrics()