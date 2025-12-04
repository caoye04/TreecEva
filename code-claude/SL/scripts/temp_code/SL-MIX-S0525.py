def calculate_checksum(packet):
    # Calculate a simple checksum for packet validation
    checksum = 0
    for i, char in enumerate(packet):
        if i % 2 == 0:
            checksum += ord(char) & 0x0F
        else:
            checksum ^= (ord(char) >> 4)
    return checksum % 256

def packet_processor(packets, filters):
    valid_packets = {}
    corrupted_count = 0
    priority_sum = 0
    security_level = 3
    
    # Track various metrics for network analysis
    metrics = {
        'total_processed': 0,
        'high_priority': 0,
        'medium_priority': 0,
        'low_priority': 0,
        'filtered': 0
    }
    
    # Process each packet with its metadata
    for idx, (packet_id, packet_data) in enumerate(packets.items()):
        metrics['total_processed'] += 1
        
        # Extract packet information
        content = packet_data.get('content', '')
        priority = packet_data.get('priority', 0)
        source = packet_data.get('source', 'unknown')
        timestamp = packet_data.get('timestamp', 0)
        
        # Security check - unused in final calculation
        if security_level > 2 and 'malicious' in content.lower():
            corrupted_count += 2
            continue
            
        # Calculate checksum for validation
        expected_checksum = packet_data.get('checksum', 0)
        actual_checksum = calculate_checksum(content)
        
        # Skip corrupted packets
        if expected_checksum != actual_checksum:
            corrupted_count += 1
            continue
        
        # Apply filters
        should_filter = False
        for filter_key, filter_value in filters.items():
            if filter_key == 'source' and source in filter_value:
                should_filter = True
                metrics['filtered'] += 1
                break
            elif filter_key == 'min_timestamp' and timestamp < filter_value:
                should_filter = True
                metrics['filtered'] += 1
                break
        
        if should_filter:
            continue
            
        # Process valid packets
        if priority >= 7:
            metrics['high_priority'] += 1
            priority_sum += priority * 2
        elif priority >= 4:
            metrics['medium_priority'] += 1
            priority_sum += priority
        else:
            metrics['low_priority'] += 1
            # Low priority packets don't contribute to priority sum
            
        # Store valid packet for further processing
        valid_packets[packet_id] = content
    
    # Calculate network congestion - not used in final result
    congestion_factor = len(packets) / max(1, len(valid_packets))
    
    # Process valid packets to extract keywords
    keywords = set()
    for content in valid_packets.values():
        words = content.split()
        for word in words:
            if word.isupper() and len(word) > 2:
                keywords.add(word)
    
    # Calculate priority value based on metrics and keywords
    if metrics['high_priority'] > 0:
        priority_factor = 2
    elif metrics['medium_priority'] > metrics['low_priority']:
        priority_factor = 1.5
    else:
        priority_factor = 1
    
    # The key calculation for priority_value
    priority_value = int((priority_sum * priority_factor) - corrupted_count)
    
    # Some additional calculations that don't affect the result
    efficiency_score = (metrics['total_processed'] - metrics['filtered']) / max(1, metrics['total_processed'])
    potential_threats = corrupted_count * security_level
    
    return priority_value

# Network packet data
data_packets = {
    'PKT001': {'content': 'ALERT System update required', 'priority': 8, 'source': 'admin', 'timestamp': 1623456789, 'checksum': 64},
    'PKT002': {'content': 'User login from 192.168.1.5', 'priority': 3, 'source': 'auth', 'timestamp': 1623456790, 'checksum': 22},
    'PKT003': {'content': 'CRITICAL Database connection lost', 'priority': 9, 'source': 'db', 'timestamp': 1623456795, 'checksum': 99},
    'PKT004': {'content': 'Potential malicious activity detected', 'priority': 7, 'source': 'security', 'timestamp': 1623456800, 'checksum': 88},
    'PKT005': {'content': 'WARNING Low disk space', 'priority': 6, 'source': 'system', 'timestamp': 1623456810, 'checksum': 47},
    'PKT006': {'content': 'New device connected to network', 'priority': 5, 'source': 'network', 'timestamp': 1623456820, 'checksum': 14},
    'PKT007': {'content': 'Routine backup completed', 'priority': 2, 'source': 'backup', 'timestamp': 1623456830, 'checksum': 11},
    'PKT008': {'content': 'ERROR File not found', 'priority': 6, 'source': 'filesystem', 'timestamp': 1623456840, 'checksum': 45}
}

# Filter settings
priority_filters = {
    'source': ['backup', 'test'],
    'min_timestamp': 1623456800
}

# Process the network packets
priority_value = packet_processor(data_packets, priority_filters)
print(f"Result: {priority_value}")