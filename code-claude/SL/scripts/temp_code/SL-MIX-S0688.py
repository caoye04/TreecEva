from collections import Counter, defaultdict

def analyze_network_traffic(packets):
    # Process network traffic data
    source_ips = [p['source'] for p in packets]
    dest_ips = [p['dest'] for p in packets]
    
    # Count packet frequencies
    source_counter = Counter(source_ips)
    dest_counter = Counter(dest_ips)
    
    # Find most active IPs
    most_active_source = source_counter.most_common(1)[0][0]
    potential_threats = [ip for ip, count in source_counter.items() if count > 5]
    
    # Calculate protocol statistics
    protocols = [p['protocol'] for p in packets]
    protocol_counter = Counter(protocols)
    most_frequent = protocol_counter.most_common(1)[0][0]
    
    # Priority mapping for different protocols
    priority_map = defaultdict(int)
    priority_map['HTTP'] = 1
    priority_map['HTTPS'] = 2
    priority_map['FTP'] = 3
    priority_map['SSH'] = 4
    priority_map['TELNET'] = 5
    
    # Traffic volume calculations
    total_bytes = sum([p.get('size', 0) for p in packets])
    avg_packet_size = total_bytes / len(packets) if packets else 0
    
    # Adjustment factors
    time_of_day = 14  # 2 PM
    day_factor = 1.5 if time_of_day > 8 and time_of_day < 18 else 2.0
    traffic_threshold = 1000 * day_factor
    
    # Security scoring
    security_score = len(potential_threats) * 10
    normalized_score = min(100, security_score)
    
    # Calculate final priority
    base_priority = priority_map[most_frequent]
    multiplier = 2 if total_bytes > traffic_threshold else 1
    final_priority = priority_map.get(most_frequent, 0) * multiplier
    
    # Generate report data
    report = {
        'most_active_source': most_active_source,
        'dominant_protocol': most_frequent,
        'priority_level': final_priority,
        'normalized_score': normalized_score
    }
    
    return report

# Sample network traffic data
packet_data = [
    {'source': '192.168.1.5', 'dest': '10.0.0.1', 'protocol': 'HTTP', 'size': 1024},
    {'source': '192.168.1.10', 'dest': '10.0.0.1', 'protocol': 'HTTPS', 'size': 2048},
    {'source': '192.168.1.5', 'dest': '10.0.0.2', 'protocol': 'HTTP', 'size': 512},
    {'source': '192.168.1.8', 'dest': '10.0.0.3', 'protocol': 'FTP', 'size': 8192},
    {'source': '192.168.1.10', 'dest': '10.0.0.4', 'protocol': 'SSH', 'size': 256},
    {'source': '192.168.1.5', 'dest': '10.0.0.1', 'protocol': 'HTTP', 'size': 1024},
    {'source': '192.168.1.5', 'dest': '10.0.0.2', 'protocol': 'HTTP', 'size': 768}
]

result = analyze_network_traffic(packet_data)
print(f"Result: {result['priority_level']}")