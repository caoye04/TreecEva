def calculate_checksum(packet):
    # Checksum calculation for network packets
    base = sum(ord(c) for c in packet['data'][:5])
    multiplier = len(packet['data']) % 4 + 1
    return (base * multiplier) % 256

def validate_packet(packet, protocols):
    # Validate packet against protocols
    if packet['protocol'] not in protocols:
        return False
    checksum = calculate_checksum(packet)
    return packet['checksum'] == checksum

def analyze_traffic(packets, target_protocols):
    # Analyze network traffic patterns
    protocol_counts = {p: 0 for p in target_protocols}
    total_size = 0
    for packet in packets:
        if packet['protocol'] in target_protocols:
            protocol_counts[packet['protocol']] += 1
            total_size += len(packet['data'])
    
    # This calculation is not used in final result
    traffic_density = total_size / max(1, sum(protocol_counts.values()))
    return protocol_counts, traffic_density

def extract_priorities(packets, valid_only=True):
    # Extract priority values from packets
    priorities = []
    for packet in packets:
        if 'priority' in packet and (not valid_only or packet.get('valid', True)):
            priorities.append(packet['priority'])
        elif 'urgent' in packet and packet['urgent']:
            # Add misleading priority values for urgent packets
            priorities.append(100)
    return priorities

def calculate_priority(packets, target_protocols):
    # Process packets and determine priority score
    valid_packets = []
    invalid_checksum = 0
    
    # Validate packets
    for packet in packets:
        # Misleading validation that doesn't affect result
        if packet['size'] < 10 or packet['ttl'] <= 0:
            continue
            
        if validate_packet(packet, target_protocols):
            valid_packets.append(packet)
        else:
            invalid_checksum += 1
    
    # Extract metrics from valid packets
    protocol_counts, _ = analyze_traffic(valid_packets, target_protocols)
    priorities = extract_priorities(valid_packets)
    
    # Calculate weighted score based on protocol distribution
    weights = {'TCP': 2, 'UDP': 1, 'ICMP': 3}
    protocol_score = sum(protocol_counts.get(p, 0) * weights.get(p, 0) for p in target_protocols)
    
    # Calculate priority metrics
    if priorities:
        avg_priority = sum(priorities) / len(priorities)
        # Misleading calculation not used in final result
        priority_variance = sum((p - avg_priority)**2 for p in priorities) / len(priorities)
    else:
        avg_priority = 0
        priority_variance = 0
    
    # This set operation is a distraction
    unique_protocols = set(p['protocol'] for p in valid_packets)
    protocol_intersection = unique_protocols.intersection(set(target_protocols))
    
    # Calculate final priority score
    base_score = protocol_score * 5
    priority_factor = max(1, avg_priority / 10)
    security_adjustment = min(invalid_checksum, 5) * 3
    
    # More distractions that don't affect the result
    ttl_values = [p['ttl'] for p in valid_packets]
    if ttl_values:
        avg_ttl = sum(ttl_values) / len(ttl_values)
    else:
        avg_ttl = 0
    
    # Final calculation
    final_priority = int(base_score * priority_factor) - security_adjustment
    
    return final_priority

# Define network packets
network_packets = [
    {'protocol': 'TCP', 'data': 'HELLO', 'checksum': 500, 'size': 20, 'ttl': 64, 'priority': 5},
    {'protocol': 'UDP', 'data': 'WORLD', 'checksum': 25, 'size': 15, 'ttl': 32, 'priority': 3},
    {'protocol': 'ICMP', 'data': 'PING!', 'checksum': 125, 'size': 12, 'ttl': 128, 'priority': 8},
    {'protocol': 'TCP', 'data': 'TEST1', 'checksum': 20, 'size': 25, 'ttl': 64, 'urgent': True},
    {'protocol': 'HTTP', 'data': 'GET /', 'checksum': 30, 'size': 30, 'ttl': 64, 'priority': 2},
    {'protocol': 'UDP', 'data': 'DATA!', 'checksum': 125, 'size': 10, 'ttl': 16, 'priority': 4, 'valid': False}
]

# Define target protocols
target_protocols = ['TCP', 'UDP', 'ICMP']

# Calculate network priority
final_priority = calculate_priority(network_packets, target_protocols)
print(f"Result: {final_priority}")