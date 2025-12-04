import itertools

def analyze_packet(packet):
    """Analyzes network packet data and returns importance rating"""
    # Extract header fields (only protocol and size matter)
    protocol = packet['protocol']
    size = packet['size']
    timestamp = packet['timestamp']
    source = packet['source']
    
    # Calculate basic importance rating
    if protocol == 'TCP':
        importance = size * 0.5
    elif protocol == 'UDP':
        importance = size * 0.3
    elif protocol == 'ICMP':
        importance = size * 0.8
    else:
        importance = size * 0.1
        
    # Add source-based adjustment (doesn't affect result)
    if source.startswith('192.168'):
        importance += 5
    elif source.startswith('10.'):
        importance -= 3
    
    # Timestamp doesn't actually matter for our calculation
    hour = int(timestamp.split(':')[0])
    if hour > 23 or hour < 0:
        return 0  # Invalid timestamp
    
    return importance

def calculate_priority(packets):
    """Calculate network traffic priority score"""
    # Initialize counters
    total_packets = len(packets)
    total_size = sum(p['size'] for p in packets)
    protocol_counts = {'TCP': 0, 'UDP': 0, 'ICMP': 0, 'OTHER': 0}
    
    # These values don't affect the result
    max_size = 0
    min_timestamp = '23:59:59'
    suspicious_sources = []
    
    # Count packets by protocol
    for packet in packets:
        proto = packet['protocol']
        if proto in protocol_counts:
            protocol_counts[proto] += 1
        else:
            protocol_counts['OTHER'] += 1
            
        # Track largest packet (unused)
        if packet['size'] > max_size:
            max_size = packet['size']
            
        # Track earliest timestamp (unused)
        if packet['timestamp'] < min_timestamp:
            min_timestamp = packet['timestamp']
            
        # Flag suspicious sources (unused)
        if packet['source'] in ['1.2.3.4', '5.6.7.8']:
            suspicious_sources.append(packet['source'])
    
    # Calculate weighted protocol ratio (key calculation)
    tcp_weight = protocol_counts['TCP'] * 3
    udp_weight = protocol_counts['UDP'] * 1
    icmp_weight = protocol_counts['ICMP'] * 5
    other_weight = protocol_counts['OTHER'] * 2
    
    # Calculate traffic diversity score (misleading)
    diversity = len([c for c in protocol_counts.values() if c > 0])
    
    # This is never used but looks important
    normalized_weights = [w/total_packets if total_packets > 0 else 0 
                         for w in [tcp_weight, udp_weight, icmp_weight, other_weight]]
    
    # Calculate priority score
    priority_base = (tcp_weight + udp_weight + icmp_weight + other_weight) / 10
    
    # Adjust for traffic distribution (misleading)
    distribution_factor = diversity * 2.5
    
    # This adjustment doesn't happen - dead code path
    if len(suspicious_sources) > 0:
        priority_base *= 1.5
        
    # Apply size factor - real calculation
    size_factor = total_size / 1000 if total_size > 0 else 0
    
    # Final calculation
    return int(priority_base + size_factor)

# Network packet data
all_packets = [
    {'protocol': 'TCP', 'size': 120, 'timestamp': '14:25:36', 'source': '192.168.1.5'},
    {'protocol': 'UDP', 'size': 80, 'timestamp': '14:25:40', 'source': '10.0.0.2'},
    {'protocol': 'ICMP', 'size': 64, 'timestamp': '14:26:10', 'source': '8.8.8.8'},
    {'protocol': 'TCP', 'size': 1024, 'timestamp': '14:26:32', 'source': '172.16.0.10'},
    {'protocol': 'HTTP', 'size': 2048, 'timestamp': '14:27:05', 'source': '192.168.1.10'},
    {'protocol': 'UDP', 'size': 512, 'timestamp': '14:27:18', 'source': '10.0.0.5'},
    {'protocol': 'TCP', 'size': 768, 'timestamp': '14:28:01', 'source': '1.2.3.4'}
]

# Filter packets based on various criteria
def filter_packets(packets, min_size=0, protocols=None, exclude_sources=None):
    """Filter packets based on criteria"""
    result = []
    for p in packets:
        # Skip packets that are too small
        if p['size'] < min_size:
            continue
            
        # Skip packets with excluded protocols
        if protocols and p['protocol'] not in protocols:
            continue
            
        # Skip packets from excluded sources
        if exclude_sources and p['source'] in exclude_sources:
            continue
            
        result.append(p)
    
    return result

# Process packets
filtered_packets = filter_packets(
    all_packets,
    min_size=100,  # Exclude small packets
    protocols=['TCP', 'UDP', 'ICMP'],  # Only include these protocols
    exclude_sources=['5.6.7.8']  # Exclude these sources
)

# Calculate importance of each packet
importance_ratings = [analyze_packet(p) for p in filtered_packets]

# These metrics aren't used in final calculation
avg_importance = sum(importance_ratings) / len(importance_ratings) if importance_ratings else 0
max_importance = max(importance_ratings) if importance_ratings else 0
min_importance = min(importance_ratings) if importance_ratings else 0

# This list comprehension isn't used
high_importance_packets = [p for i, p in enumerate(filtered_packets) 
                         if importance_ratings[i] > avg_importance]

# Calculate the priority score
priority_score = calculate_priority(filtered_packets)

# Generate permutations for analysis (not used)
protocol_permutations = list(itertools.permutations(['TCP', 'UDP', 'ICMP'], 2))

# Print the result
print(f"Result: {priority_score}")