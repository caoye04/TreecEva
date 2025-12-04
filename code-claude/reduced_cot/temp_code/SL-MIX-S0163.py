from collections import Counter, defaultdict

def network_analyzer(packets, priority_threshold):
    # Process network traffic data
    traffic_stats = defaultdict(int)
    priority_map = {}
    error_codes = set()
    
    # Initialize counters for different metrics
    total_bytes = 0
    dropped_packets = 0
    successful_packets = 0
    retransmissions = 0
    
    # Track packet IDs to detect duplicates
    seen_packets = set()
    
    # Process each packet
    for i, packet in enumerate(packets):
        packet_id, size, priority, status, destination = packet
        
        # Track bytes processed
        total_bytes += size
        
        # Map packet priorities
        priority_map[packet_id] = priority
        
        # Count packets by destination
        traffic_stats[destination] += 1
        
        # Track unique error codes
        if status < 0:
            error_codes.add(status)
            dropped_packets += 1
        else:
            successful_packets += 1
        
        # Check for retransmissions
        if packet_id in seen_packets:
            retransmissions += 1
        else:
            seen_packets.add(packet_id)
    
    # Calculate network efficiency
    if total_bytes > 0:
        efficiency = (successful_packets * 100) / len(packets)
    else:
        efficiency = 0
    
    # Extract high-priority destinations
    high_priority_destinations = [dest for dest, count in traffic_stats.items() 
                               if count > 3 and dest.startswith('srv')]
    
    # Calculate load balancing index using Counter
    dest_counter = Counter(packet[4] for packet in packets)
    most_common_dest = dest_counter.most_common(1)[0][1] if dest_counter else 0
    load_balance_index = most_common_dest / len(packets) if packets else 0
    
    # Calculate bit-wise hash for error tracking
    error_hash = 0
    for code in error_codes:
        error_hash = (error_hash ^ abs(code)) << 1
        if error_hash > 1024:
            error_hash = error_hash % 997  # Prime number to reduce collisions
    
    # This is the critical calculation for high-priority packet analysis
    critical_count = sum(1 for _, _, p, _, _ in packets if p >= priority_threshold)
    
    # Calculate weighted priority score (distraction)
    weighted_score = sum(p * s for _, s, p, _, _ in packets) / total_bytes if total_bytes else 0
    
    # Network health metric (distraction)
    health_metric = (successful_packets - dropped_packets) * (1 - load_balance_index)
    
    # Packet distribution analysis (distraction)
    size_distribution = defaultdict(int)
    for _, size, _, _, _ in packets:
        size_category = size // 128  # Group by size ranges
        size_distribution[size_category] += 1
    
    # Calculate protocol efficiency (distraction)
    protocol_overhead = sum(24 for _ in packets)  # Assume 24 bytes header per packet
    payload_bytes = total_bytes - protocol_overhead
    
    # Return the count of critical packets
    return critical_count

# Sample network traffic data: (packet_id, size_bytes, priority, status_code, destination)
packets = [
    (1001, 256, 3, 1, 'srv01'),
    (1002, 512, 5, 1, 'srv02'),
    (1003, 128, 2, -4, 'srv01'),
    (1004, 1024, 4, 1, 'srv03'),
    (1005, 768, 5, 1, 'srv01'),
    (1006, 256, 1, -2, 'srv02'),
    (1007, 512, 4, 1, 'srv01'),
    (1008, 128, 3, 1, 'srv03'),
    (1001, 256, 3, 1, 'srv02'),  # Retransmission
    (1009, 384, 5, -1, 'srv01'),
    (1010, 256, 2, 1, 'srv04'),
    (1011, 512, 5, 1, 'srv01')
]

# Set priority threshold for critical packets
priority_threshold = 4

# Analyze the network traffic
critical_packet_count = network_analyzer(packets, priority_threshold)
print(f"Critical packet count: {critical_packet_count}")

# Alternate analysis with different threshold (distraction)
low_priority_packets = sum(1 for _, _, p, _, _ in packets if p < 3)

# Calculate average packet size (distraction)
average_size = sum(size for _, size, _, _, _ in packets) / len(packets)

# Traffic distribution by destination (distraction)
dest_traffic = defaultdict(int)
for _, size, _, _, dest in packets:
    dest_traffic[dest] += size
    
# Calculate network congestion index (distraction)
congestion_factor = sum(1 for _, _, _, status, _ in packets if status < 0) / len(packets)
