def calculate_system_capacity():
    base_units = [12, 15, 10, 20, 18]
    efficiency_rates = [0.8, 0.9, 0.75, 0.88, 0.91]
    
    # Irrelevant debug variable (minor distraction)
    debug_mode = False
    
    # Compute adjusted loads using element-wise multiplication via zip
    adjusted_loads = []
    for unit, rate in zip(base_units, efficiency_rates):
        adjusted_loads.append(unit * rate)
    
    # Additional unrelated intermediate variable (low interference)
    peak_demand = max(adjusted_loads)
    
    total_capacity = sum(adjusted_loads)
    
    # Print result as required
    print(f"Result: {total_capacity}")

    return total_capacity

# Execute function
calculate_system_capacity()