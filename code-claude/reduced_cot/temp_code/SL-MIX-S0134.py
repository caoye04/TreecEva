import itertools

def analyze_network_traffic(packets, threshold):
    # Process network packet data
    source_ips = [p['source'] for p in packets if p['size'] > 0]
    dest_ips = [p['dest'] for p in packets if p['protocol'] in ['TCP', 'UDP']]
    
    # Calculate packet statistics
    avg_size = sum(p['size'] for p in packets) / len(packets)
    max_size = max(p['size'] for p in packets)
    min_size = min(p['size'] for p in packets)
    
    # Track IP address frequencies
    counts = {}
    for ip in source_ips + dest_ips:
        if ip in counts:
            counts[ip] += 1
        else:
            counts[ip] = 1
    
    # Find common elements between sources and destinations
    common_elements = set(source_ips).intersection(set(dest_ips))
    
    # Calculate priority score for each common element
    priority_scores = {}
    for ip in common_elements:
        priority = (counts[ip] * 2) - (len(ip.split('.')) - 3)
        priority_scores[ip] = priority
    
    # Calculate the sum of counts for common elements
    overlap_sum = sum(counts[k] for k in common_elements)
    
    # Apply threshold filter (not relevant to final result)
    filtered_ips = [ip for ip in counts if counts[ip] > threshold]
    potential_issues = len(filtered_ips)
    
    # Calculate anomaly coefficient (not used in final calculation)
    anomaly_coef = (max_size - min_size) / avg_size if avg_size > 0 else 0
    
    return overlap_sum, filtered_ips, anomaly_coef

# Network packet data
packets = [
    {'source': '192.168.1.5', 'dest': '10.0.0.1', 'size': 1024, 'protocol': 'TCP'},
    {'source': '192.168.1.10', 'dest': '10.0.0.2', 'size': 512, 'protocol': 'UDP'},
    {'source': '10.0.0.1', 'dest': '192.168.1.5', 'size': 768, 'protocol': 'TCP'},
    {'source': '172.16.0.1', 'dest': '10.0.0.1', 'size': 256, 'protocol': 'ICMP'},
    {'source': '192.168.1.5', 'dest': '172.16.0.1', 'size': 1280, 'protocol': 'TCP'}
]

# Run the analysis
overlap_result, filtered, anomaly = analyze_network_traffic(packets, 2)
print(f"Result: {overlap_result}")