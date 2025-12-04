from collections import Counter, defaultdict

# Network packet analysis function
def analyze_packets(packet_ids, packet_priorities):
    # Count packet occurrences
    packet_counter = Counter(packet_ids)
    
    # Track priority by packet type
    priority_map = defaultdict(int)
    for pid, priority in zip(packet_ids, packet_priorities):
        # Only keep the highest priority for each packet
        priority_map[pid] = max(priority_map[pid], priority)
    
    # Calculate network statistics
    unique_packets = len(packet_counter)
    total_packets = sum(packet_counter.values())
    
    # Calculate flow metrics
    base_flow = total_packets & 0xFF  # Bitwise AND with 255
    priority_flow = sum(priority_map.values()) % 100  # Modulo to keep manageable
    
    # Calculate potential flow
    potential_flow = (base_flow ^ priority_flow)  # Bitwise XOR
    
    # Compute overhead metrics (distractor)
    overhead_factor = sum(v for k, v in packet_counter.items() if v > 1)
    routing_metric = sum(p for p in packet_priorities if p % 2 == 0)
    
    # Calculate actual flow
    actual_flow = potential_flow | unique_packets  # Bitwise OR
    
    # Calculate blocked packets
    blocked_packets = [pid for pid, count in packet_counter.items() if count > 2]
    blocked_count = len(blocked_packets)
    
    # Calculate interference (distractor)
    interference = (routing_metric & 0x3F) * 2
    
    # Compute blocked flow
    blocked_flow = blocked_count * 3
    
    # Calculate final network flow
    network_flow = actual_flow - blocked_flow
    
    # Additional metrics (distractors)
    efficiency = (total_packets / (total_packets + overhead_factor)) if overhead_factor else 1.0
    capacity = (base_flow + priority_flow) * efficiency
    
    return network_flow, capacity

# Sample packet data
packet_ids = [5, 2, 8, 5, 2, 5, 10, 8, 15]
packet_priorities = [3, 1, 4, 2, 5, 1, 3, 2, 5]

# Run the analysis
network_flow, capacity = analyze_packets(packet_ids, packet_priorities)
print(f"Result: {network_flow}")