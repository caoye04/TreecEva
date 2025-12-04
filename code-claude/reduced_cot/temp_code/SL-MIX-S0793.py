def analyze_packet_metadata(metadata, priority_bits=0x0F):
    # Extract routing information from packet metadata
    route_hash = 0
    for i, byte in enumerate(metadata):
        if i % 2 == 0:  # Even positions contain routing data
            route_hash = (route_hash << 3) | (byte & priority_bits)
        else:  # Odd positions contain checksum data (unused)
            continue
    
    # Calculate priority score (unused in main calculation)
    priority_score = sum(b for b in metadata if b > 128) / max(1, len(metadata))
    return route_hash ^ (len(metadata) * 2)

def simulate_network_congestion(packets, bandwidth=100):
    # Simulate network congestion effects
    congestion_factor = min(1.0, len(packets) / bandwidth)
    dropped_packets = int(len(packets) * congestion_factor * 0.3)
    
    # Calculate theoretical throughput (unused)
    theoretical_throughput = bandwidth * (1 - congestion_factor)
    
    # Return effective packet count
    return len(packets) - dropped_packets

def calculate_network_efficiency(packet_data, hop_threshold):
    # Initialize tracking variables
    total_hops = 0
    valid_packets = 0
    error_count = 0
    retry_packets = []
    network_stats = {'congestion': [], 'latency': [], 'throughput': []}
    
    # Process each packet in the data
    for packet in packet_data:
        # Extract packet properties
        packet_id, hops, retry_count = packet
        
        # Skip packets with excessive retries (distractor)
        if retry_count > 5:
            retry_packets.append(packet_id)
            error_count += 1
            continue
        
        # Track network statistics (mostly distractors)
        packet_latency = hops * 2.5 + retry_count * 10
        network_stats['latency'].append(packet_latency)
        
        # Calculate congestion score (unused)
        congestion_score = min(10, hops + retry_count) / 10
        network_stats['congestion'].append(congestion_score)
        
        # Only count packets below hop threshold
        if hops <= hop_threshold:
            total_hops += hops
            valid_packets += 1
    
    # Apply lambda function to calculate theoretical efficiency (distractor)
    theoretical_efficiency = lambda p, h: 100 * (1 - h/(p*10)) if p > 0 else 0
    theo_value = theoretical_efficiency(len(packet_data), sum(p[1] for p in packet_data))
    
    # Create efficiency lookup table (distractor)
    efficiency_table = {i: i**2 / 100 for i in range(10, 100, 10)}
    
    # Extract metadata for analysis (distractor)
    metadata = [p[0] % 256 for p in packet_data]
    metadata_score = analyze_packet_metadata(metadata)
    
    # Calculate actual network efficiency
    if valid_packets == 0:
        return 0
    
    # Simulate network conditions (distractor)
    effective_packets = simulate_network_congestion(packet_data)
    
    # Final efficiency calculation
    avg_hops = total_hops / valid_packets
    network_efficiency = int(100 - (avg_hops * 5))
    
    # List comprehension for packet quality score (distractor)
    quality_scores = [100 - (p[1] * 5 + p[2] * 2) for p in packet_data if p[1] < hop_threshold]
    
    return network_efficiency

# Packet data format: (packet_id, hop_count, retry_count)
packet_data = [
    (1001, 4, 0),
    (1002, 3, 1),
    (1003, 7, 2),  # Exceeds hop threshold
    (1004, 2, 0),
    (1005, 8, 0),  # Exceeds hop threshold
    (1006, 5, 6),  # Too many retries
    (1007, 3, 2),
    (1008, 6, 1),  # Exceeds hop threshold
    (1009, 4, 3),
    (1010, 1, 0)
]

hop_threshold = 5  # Maximum acceptable hop count

# Calculate network quality metrics
packet_success_rate = len([p for p in packet_data if p[1] <= hop_threshold and p[2] <= 5]) / len(packet_data)
average_retry = sum(p[2] for p in packet_data) / len(packet_data)

# Calculate the network efficiency
network_efficiency = calculate_network_efficiency(packet_data, hop_threshold)

# Dictionary operations on network data (distractor)
network_metrics = {
    'efficiency': network_efficiency,
    'success_rate': packet_success_rate * 100,
    'avg_retry': average_retry,
    'total_packets': len(packet_data)
}

print(f"Result: {network_efficiency}")