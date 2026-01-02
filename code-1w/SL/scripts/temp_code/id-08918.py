def analyze_fleet_efficiency(fleet, route):
    base_efficiency = 12.5
    fleet_set = {v[1] for v in fleet}  # vehicle types
    constraint_set = set(route)
    
    overlap = fleet_set & constraint_set  # common vehicle types allowed
    efficiency_adjustment = len(overlap) * 1.75
    
    total_capacity = 0
    for vehicle in fleet:
        id, v_type, count = vehicle
        if v_type in overlap:
            total_capacity += count * 3
    
    scaled_capacity = total_capacity // 2  # integer division
    final_capacity = int(scaled_capacity * (base_efficiency + efficiency_adjustment) // 4)
    
    # Irrelevant tracking variables (minimal interference)
    log_entry = f'Processed {len(fleet)} vehicle types'
    temp_result = sum(1 for x in fleet if x[1] in constraint_set)
    
    return final_capacity

# Input data
data_routes = ['truck', 'van']
fleet_inventory = [
    (101, 'truck', 4),
    (102, 'van', 6),
    (103, 'car', 8),
    (104, 'bus', 2)
]

result = analyze_fleet_efficiency(fleet_inventory, data_routes)
print(f"Target result: {result}")