import itertools

def process_logistics():
    # Package data: (destination_code, weight, priority_multiplier)
    packages = [
        ('ALPHA_123', 15, 2),
        ('BETA_456', 8, 3),
        ('GAMMA_789', 22, 1),
        ('DELTA_000', 5, 4),
        ('EPSILON_111', 18, 2)
    ]
    
    # Destination mapping using hash table
    destination_zones = {
        'ALPHA': 'Zone_A',
        'BETA': 'Zone_B',
        'GAMMA': 'Zone_C',
        'DELTA': 'Zone_D',
        'EPSILON': 'Zone_E'
    }
    
    # Process packages using stack (LIFO)
    package_stack = []
    for pkg in packages:
        package_stack.append(pkg)
    
    accumulated_priority_score = 0
    zone_loads = {'Zone_A': 0, 'Zone_B': 0, 'Zone_C': 0, 'Zone_D': 0, 'Zone_E': 0}
    
    # Greedy processing: prioritize by priority_multiplier * weight
    while package_stack:
        # Pop from stack
        dest_code, weight, priority = package_stack.pop()
        
        # Tokenize destination code
        tokens = dest_code.split('_')
        base_dest = tokens[0]
        
        # Transform to zone
        zone = destination_zones.get(base_dest, 'Unknown')
        
        # Calculate priority score
        priority_score = priority * weight
        
        # Apply zone-based modifier using divide and conquer approach for load balancing
        current_load = zone_loads[zone]
        if current_load > 20:
            priority_score = priority_score // 2  # Reduce priority for overloaded zones
        
        # Update accumulated score
        accumulated_priority_score += priority_score
        
        # Update zone load
        zone_loads[zone] += weight
    
    return accumulated_priority_score

# Execute logistics processing
final_score = process_logistics()
print(f"Result: {final_score}")