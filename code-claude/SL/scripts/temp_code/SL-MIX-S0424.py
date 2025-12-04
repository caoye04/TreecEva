def calculate_network_load(packets):
    # Calculate network congestion factor based on packet sizes
    total_size = sum(p['size'] for p in packets)
    congestion = total_size / (len(packets) * 100) if packets else 0
    return min(congestion * 1.5, 1.0)

def optimize_routing(paths, congestion_factor):
    # Find optimal path based on distance and congestion
    optimized = [(p['distance'] * (1 + congestion_factor), p['id']) for p in paths]
    optimized.sort()
    return optimized[0][1] if optimized else -1

def calculate_actual_priority():
    # Network traffic simulation with priority calculation
    active_connections = 8
    inactive_connections = 3
    pending_requests = [{'id': i, 'priority': i % 3 + 1, 'status': 'open' if i % 2 == 0 else 'closed'} 
                      for i in range(1, 11)]
    
    # Track security incidents (not used in final calculation)
    security_incidents = {'unauthorized': 5, 'suspicious': 3, 'blocked': 2}
    total_incidents = sum(security_incidents.values())
    
    # Calculate base metrics
    connection_ratio = active_connections / (active_connections + inactive_connections)
    base_priority = 10 * connection_ratio
    
    # Process packets (distracting calculation)
    packets = [{'id': i, 'size': 50 + i * 10, 'corrupted': i % 7 == 0} for i in range(12)]
    network_load = calculate_network_load(packets)
    
    # Simulate routing paths (distracting calculation)
    routing_paths = [{'id': i, 'distance': 10 + i * 3, 'capacity': 100 - i * 5} for i in range(5)]
    optimal_path = optimize_routing(routing_paths, network_load)
    
    # Filter and process requests
    open_requests = [req for req in pending_requests if req['status'] == 'open']
    priority_sum = sum(req['priority'] for req in open_requests)
    
    # Calculate weighted factors (mixed relevant and irrelevant)
    weighted_load = network_load * 25
    request_factor = priority_sum / len(pending_requests)
    
    # Apply bitwise operations (mostly distracting)
    bit_factor = (active_connections << 1) | (inactive_connections >> 1)
    bit_factor = bit_factor & 15  # Mask to 4 bits
    
    # Calculate final priority score
    adjusted_priority = base_priority + request_factor
    
    # This is the key calculation - other factors above are mostly distractions
    final_value = int(adjusted_priority * 3) + (len(open_requests) - bit_factor % 3)
    
    return final_value

# Execute the calculation
final_priority = calculate_actual_priority()
print(f"Result: {final_priority}")
