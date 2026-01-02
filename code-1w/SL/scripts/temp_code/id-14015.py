def calculate_network_capacity(links):
    base_multiplier = 2.5
    total_capacity = 0
    
    for idx, (bandwidth, active) in enumerate(links):
        if not active:
            continue
        
        # Adjust capacity based on index and bandwidth using conditional expression
        adjustment = 1.2 if idx % 2 == 0 else 0.8
        total_capacity += bandwidth * base_multiplier * adjustment
    
    # Irrelevant tracking variable (minor distraction, intervention=4)
    link_count = len([link for link in links if link[1]])
    
    return int(total_capacity)

# Network link data: (bandwidth in Gbps, isActive)
links = [
    (10, True),
    (20, False),
    (15, True),
    (25, True)
]

# Calculation entry point
total_capacity = calculate_network_capacity(links)
print(f"Result: {total_capacity}")