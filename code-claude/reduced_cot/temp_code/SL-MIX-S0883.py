def process_network_packets(packet_data):
    # Initialize counters
    error_count = 0
    dropped_packets = 0
    checksum_failures = 0
    
    # Process each packet's status
    statuses = [p % 7 for p in packet_data]  # Get status codes by modulo 7
    
    # Track packet processing metrics
    processed = []
    for i, status in enumerate(statuses):
        if status == 0:  # Valid packet
            processed.append(packet_data[i])
        elif status == 1:  # Error packet
            error_count += 1
        elif status == 2:  # Dropped packet
            dropped_packets += 1
        elif status == 3:  # Checksum failure
            checksum_failures += 1
            if packet_data[i] % 2 == 0:  # Even packets can be recovered
                processed.append(packet_data[i])
        else:  # Other statuses are valid
            processed.append(packet_data[i])
    
    # Calculate network quality score (not used for final result)
    quality_score = 100 - (error_count * 2 + dropped_packets * 3 + checksum_failures)
    
    # Identify valid packets (those divisible by 3 or 5)
    valid_packets = [p for p in processed if p % 3 == 0 or p % 5 == 0]
    
    # Track unique packet IDs (not used for final result)
    unique_ids = set([p % 100 for p in valid_packets])
    
    # Calculate total valid packets
    total_valid_packets = sum(valid_packets)
    
    # Apply network latency adjustment (not used for final result)
    latency_factor = len(processed) / max(1, len(packet_data))
    adjusted_total = total_valid_packets * latency_factor
    
    print(f"Result: {total_valid_packets}")
    return total_valid_packets

# Network packet data (packet values)
packet_data = [15, 22, 37, 45, 51, 60, 13, 25, 30, 44]
result = process_network_packets(packet_data)