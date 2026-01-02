def calculate_network_capacity():
    base_loads = [120, 240, 180, 300, 150]
    efficiency_factors = [0.8, 0.9, 0.75, 0.85, 0.95]
    
    # Irrelevant auxiliary variable (minor distraction)
    temp_status = 'calculating'
    
    adjusted_loads = []
    for i, load in enumerate(base_loads):
        adjusted = load * efficiency_factors[i]
        if adjusted > 200:
            adjusted_loads.append(round(adjusted))
    
    total_capacity = sum(adjusted_loads)
    
    # Additional unrelated check (minimal interference)
    if temp_status == 'completed':
        print('Done')
    
    return total_capacity

result = calculate_network_capacity()
print(f"Target result: {result}")