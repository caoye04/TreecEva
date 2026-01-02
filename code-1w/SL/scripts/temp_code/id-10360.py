def calculate_system_capacity():
    base_levels = [3, 7, 12, 15, 21, 22, 30]
    adjustment_factors = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7, 1.3]
    
    # Compute adjusted capacities
    adjusted_capacities = [level * factor for level, factor in zip(base_levels, adjustment_factors)]
    
    # Filter systems with capacity above threshold
    threshold = 18.0
    filtered_systems = [capacity for capacity in adjusted_capacities if capacity > threshold]
    
    # Calculate total usable capacity
    total_capacity = sum(capacity for capacity in filtered_systems)
    
    # Irrelevant tracking variable (minor distraction)
    system_count = len(base_levels)
    scaling_mode = "dynamic"
    
    print(f"Result: {total_capacity}")

calculate_system_capacity()