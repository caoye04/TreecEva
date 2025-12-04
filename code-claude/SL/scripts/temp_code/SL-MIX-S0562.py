from collections import Counter, defaultdict

# Network packet processing simulation
def process_packets(packets, max_retries=3):
    # Process network packets and calculate priorities
    packet_types = Counter([p['type'] for p in packets])
    
    # Track packet success rates (not used in final calculation)
    success_tracking = defaultdict(int)
    for p in packets:
        if p.get('success', False):
            success_tracking[p['type']] += 1
    
    # Calculate network congestion factor
    congestion = len(packets) / 100 * 1.5
    
    # Generate priority values for each packet
    priorities = []
    retry_counts = defaultdict(int)
    
    for idx, packet in enumerate(packets):
        # Base priority calculation
        base_priority = packet.get('size', 0) * 0.01
        
        # Apply type-specific multipliers
        type_multiplier = 1.0
        if packet['type'] == 'urgent':
            type_multiplier = 2.5
        elif packet['type'] == 'standard':
            type_multiplier = 1.0
        elif packet['type'] == 'bulk':
            type_multiplier = 0.5
        
        # Calculate packet age factor (unused in final priority)
        age_factor = min(packet.get('age', 0) / 10, 1.0)
        
        # Simulate retry penalties
        retry_penalty = retry_counts[packet['id']] * 0.2 if 'id' in packet else 0
        retry_counts[packet.get('id', idx)] += 1
        
        # Calculate final priority
        priority = base_priority * type_multiplier - retry_penalty
        priorities.append(priority)
    
    # Apply threshold filtering - only keep priorities above threshold
    threshold = 0.5 if congestion > 1.0 else 0.25
    priority_queue = list(filter(lambda x: x > threshold, priorities))
    
    # Generate some diagnostic data (not used in final calculation)
    diagnostic = {
        'dropped': len(priorities) - len(priority_queue),
        'avg_priority': sum(priorities) / len(priorities) if priorities else 0
    }
    
    # Calculate the final priority sum
    filtered_priority = sum(priority_queue)
    
    print(f"Result: {filtered_priority}")
    return filtered_priority

# Test data
packet_data = [
    {'id': 'p1', 'type': 'urgent', 'size': 75, 'age': 5, 'success': True},
    {'id': 'p2', 'type': 'standard', 'size': 40, 'age': 2, 'success': False},
    {'id': 'p3', 'type': 'bulk', 'size': 120, 'age': 1, 'success': True},
    {'id': 'p4', 'type': 'urgent', 'size': 60, 'age': 8, 'success': True},
    {'id': 'p5', 'type': 'standard', 'size': 55, 'age': 3, 'success': False}
]

# Process the packets
result = process_packets(packet_data)