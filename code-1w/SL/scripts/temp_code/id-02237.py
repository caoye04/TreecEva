def calculate_network_capacity():
    nodes = ['router_A', 'router_B', 'switch_C', 'hub_D']
    base_speeds = [1000, 500, 200, 100]
    
    # Create capacity map using dictionary comprehension and enumerate
    capacity_map = {nodes[i]: speed * (i + 1) for i, speed in enumerate(base_speeds)}
    
    # Update specific node conditionally
    if 'switch_C' in capacity_map:
        capacity_map['switch_C'] += 50
    
    # Add aggregated link using zip to pair nodes with shifted speeds
    backup_links = [b * 0.1 for b in base_speeds]
    for primary, backup in zip(base_speeds, backup_links):
        capacity_map[f'backup_{nodes[base_speeds.index(primary)]}'] = int(backup)
    
    # Compute total capacity
    total_capacity = sum(capacity_map.values())
    
    # Irrelevant tracking variable (minor distraction)
    active_connections = len([v for v in capacity_map.values() if v > 100])
    
    return total_capacity

result = calculate_network_capacity()
print(f"Result: {result}")