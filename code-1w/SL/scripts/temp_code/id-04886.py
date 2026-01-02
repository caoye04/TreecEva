def calculate_resource_allocation():
    machines = ['m1', 'm2', 'm3', 'm4']
    status = ['active', 'inactive', 'active', 'active']
    base_capacity = [8, 12, 16, 10]
    utilization = [0.5, 0.7, 0.4, 0.6]

    # Irrelevant list for slight distraction (intervention level 5)
    maintenance_cycles = [30, 45, None, 25]

    active_indices = [i for i, s in enumerate(status) if s == 'active']
    
    # Calculate available slots per machine
    available_slots = []
    for idx in active_indices:
        slot = int(base_capacity[idx] * (1 - utilization[idx]))
        available_slots.append(slot)
    
    total_capacity = sum(available_slots)
    
    # Additional irrelevant operation (minor interference)
    avg_cycle = sum([c for c in maintenance_cycles if isinstance(c, int)]) / 3
    
    print(f"Result: {total_capacity}")

calculate_resource_allocation()