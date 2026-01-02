def calculate_network_capacity():
    nodes = ['router_A', 'switch_B', 'firewall_C', 'bridge_D']
    base_speeds = [100, 200, 150, 300]
    overhead = {'router_A': 10, 'switch_B': 25, 'firewall_C': 40, 'bridge_D': 5}
    
    # Adjusted performance considering load distribution
    adjusted = [speed - overhead[node] for speed, node in zip(base_speeds, nodes)]
    
    # Efficiency boost for high-utilization nodes
    boosted = [val * 1.1 if val >= 175 else val for val in adjusted]
    
    # Simulate capacity allocation per segment
    capacities = [int(b) for b in boosted]
    total_capacity = sum(capacities)
    
    # Irrelevant tracking variable (minor distraction)
    active_segments = len([c for c in capacities if c > 100])
    
    return total_capacity

result = calculate_network_capacity()
print(f"Result: {result}")