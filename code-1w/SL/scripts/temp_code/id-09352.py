def calculate_warehouse_capacity():
    locations = ['A1', 'B2', 'C3', 'D4']
    base_units = [150, 200, 175, 225]
    
    # Initialize capacity map using dictionary and enumerate
    capacity_map = {loc: unit * 2 for idx, (loc, unit) in enumerate(zip(locations, base_units))}
    
    # Adjust capacity for climate zones (only C3 has special adjustment)
    for loc, cap in capacity_map.items():
        if 'C' in loc:
            capacity_map[loc] = int(cap * 1.2)
    
    # Distractor variables - irrelevant to final result
    temp_holdings = [300, 180, 210]
    max_hold = max(temp_holdings)
    avg_hold = sum(temp_holdings) / len(temp_holdings)
    
    total_capacity = sum(capacity_map.values())
    return total_capacity

result = calculate_warehouse_capacity()
print(f"Result: {result}")