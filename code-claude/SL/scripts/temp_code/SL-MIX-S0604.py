def calculate_network_metrics(packets, routes):
    # Network monitoring system simulation
    active_connections = {}
    packet_loss = 0
    latency_sum = 0
    
    # Process route information (distractor)
    for route in routes:
        hop_count = len(route['path'])
        bandwidth = route.get('bandwidth', 100)
        congestion_factor = 1.0 - (0.05 * min(10, hop_count))
        
        # Store connection data
        active_connections[route['id']] = {
            'hops': hop_count,
            'efficiency': bandwidth * congestion_factor
        }
    
    # Initialize monitoring variables
    total_packets = len(packets)
    processed_packets = 0
    is_critical = False
    base_priority = 0
    adjustment = 0
    
    # Analyze packet data
    for idx, packet in enumerate(packets):
        packet_type = packet['type'].lower()
        packet_size = packet['size']
        route_id = packet['route_id']
        
        # Track processed packets
        processed_packets += 1
        
        # Calculate packet importance factors
        if packet_type == 'data':
            importance = 1
        elif packet_type == 'control':
            importance = 2
        elif packet_type == 'priority':
            importance = 3
        else:
            importance = 0
        
        # Update metrics based on packet analysis
        if route_id in active_connections:
            route_data = active_connections[route_id]
            latency = packet_size / (route_data['efficiency'] + 1)
            latency_sum += latency
            
            # Determine if packet meets critical threshold
            if importance >= 2 and packet_size > 1000:
                is_critical = True
                base_priority = 75
                adjustment = 15
            elif importance >= 1 and packet_size > 500:
                is_critical = False
                base_priority = 50
                adjustment = 10
            else:
                is_critical = False
                base_priority = 25
                adjustment = 5
        else:
            # Track packets with invalid routes (distractor)
            packet_loss += 1
            
    # Calculate reliability metrics (distractor)
    reliability = ((total_packets - packet_loss) / total_packets) * 100 if total_packets > 0 else 0
    avg_latency = latency_sum / processed_packets if processed_packets > 0 else 0
    
    # Calculate final priority level based on network conditions
    priority_level = base_priority * (1 if is_critical else 0.5) + adjustment
    
    # Generate detailed report (distractor)
    report = {
        'connections': len(active_connections),
        'reliability': reliability,
        'latency': avg_latency,
        'priority': priority_level
    }
    
    print(f"Target result: {priority_level}")
    return report

# Test the network monitoring system
packet_data = [
    {'type': 'DATA', 'size': 1200, 'route_id': 'R001'},
    {'type': 'CONTROL', 'size': 800, 'route_id': 'R002'},
    {'type': 'PRIORITY', 'size': 1500, 'route_id': 'R001'}
]

route_data = [
    {'id': 'R001', 'path': ['A', 'B', 'C'], 'bandwidth': 150},
    {'id': 'R002', 'path': ['A', 'D', 'E', 'F'], 'bandwidth': 120},
    {'id': 'R003', 'path': ['X', 'Y'], 'bandwidth': 200}
]

result = calculate_network_metrics(packet_data, route_data)