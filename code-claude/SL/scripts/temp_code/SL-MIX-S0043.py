import itertools

def analyze_network_traffic(packets_data):
    # Network traffic analyzer that calculates priority metrics
    # for different types of data packets
    
    # Process incoming packets
    processed_packets = []
    for i, packet in enumerate(packets_data):
        # Add processing metadata
        processed = {
            'id': i,
            'size': packet['size'],
            'type': packet['type'],
            'priority': 0,
            'route': packet.get('route', 'default'),
            'encrypted': packet.get('encrypted', False)
        }
        
        # Calculate packet importance score (distractor)
        importance = (processed['size'] * 0.7) + (15 if processed['encrypted'] else 0)
        processed['importance'] = importance
        
        # Set initial priority based on type
        if processed['type'] == 'video':
            processed['priority'] = 3
        elif processed['type'] == 'audio':
            processed['priority'] = 4
        elif processed['type'] == 'text':
            processed['priority'] = 2
        else:
            processed['priority'] = 1
        
        # Apply routing adjustment (distractor)
        if processed['route'] == 'express':
            processed['latency'] = 0.8
        elif processed['route'] == 'secure':
            processed['latency'] = 1.5
        else:
            processed['latency'] = 1.0
            
        processed_packets.append(processed)
    
    return processed_packets

def calculate_priority(packets):
    # Calculate the priority sum with specific rules
    priority_total = 0
    type_counts = {'video': 0, 'audio': 0, 'text': 0, 'data': 0}
    
    # Create lookup tables (distractor)
    size_multipliers = {'small': 1.0, 'medium': 1.5, 'large': 2.0}
    encryption_bonus = {'none': 0, 'basic': 5, 'advanced': 10}
    
    # Group packets by type
    packets_by_type = {}
    for packet in packets:
        packet_type = packet['type']
        if packet_type not in packets_by_type:
            packets_by_type[packet_type] = []
        packets_by_type[packet_type].append(packet)
        type_counts[packet_type] += 1
    
    # Calculate weighted priorities
    for packet in packets:
        # Apply size-based modifier (relevant)
        size_modifier = 1
        if packet['size'] < 50:
            size_modifier = 0.8
        elif packet['size'] > 200:
            size_modifier = 1.2
        
        # This is the key calculation for the answer
        adjusted_priority = packet['priority'] * size_modifier
        priority_total += adjusted_priority
        
        # Distractor calculations that don't affect the result
        if packet.get('encrypted', False):
            security_score = packet['priority'] * 2
        else:
            security_score = packet['priority'] * 0.5
    
    # More distractor operations
    type_combinations = list(itertools.combinations(type_counts.keys(), 2))
    combination_count = len(type_combinations)
    
    # Return only the priority sum (other calculations are distractors)
    return priority_total

# Test data - mixture of packet types
packets_data = [
    {'size': 120, 'type': 'video', 'route': 'express', 'encrypted': True},
    {'size': 30, 'type': 'text', 'route': 'default'},
    {'size': 75, 'type': 'audio', 'encrypted': False},
    {'size': 250, 'type': 'video', 'route': 'secure'},
    {'size': 45, 'type': 'audio', 'route': 'express'},
    {'size': 180, 'type': 'data', 'encrypted': True}
]

# Process packets
processed_packets = analyze_network_traffic(packets_data)

# Filter packets based on complex criteria (distractor)
def filter_packets(packets, min_size=0, types=None, routes=None):
    result = []
    for packet in packets:
        if packet['size'] <= min_size:
            continue
        if types and packet['type'] not in types:
            continue
        if routes and packet.get('route') not in routes:
            continue
        result.append(packet)
    return result

# Apply different filters (most are distractors)
encrypted_packets = [p for p in processed_packets if p.get('encrypted', False)]
route_packets = filter_packets(processed_packets, routes=['express', 'secure'])
large_packets = filter_packets(processed_packets, min_size=100)

# The actual filter we care about
filtered_packets = [p for p in processed_packets if p['size'] > 25]

# The key calculation that determines our answer
priority_sum = calculate_priority(filtered_packets)

# Distractor calculations
encryption_ratio = len(encrypted_packets) / len(processed_packets) if processed_packets else 0
avg_size = sum(p['size'] for p in processed_packets) / len(processed_packets) if processed_packets else 0
route_priority = sum(p['priority'] for p in route_packets)

# Output
print(f"Network analysis complete")
print(f"Average packet size: {avg_size:.2f}")
print(f"Encryption ratio: {encryption_ratio:.2f}")
print(f"Route priority: {route_priority}")
print(f"Priority sum: {priority_sum}")