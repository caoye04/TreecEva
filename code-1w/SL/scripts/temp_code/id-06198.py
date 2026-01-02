def calculate_network_capacity():
    base_speeds = [120, 85, 200, 90, 150]
    efficiency_factors = [0.8, 1.0, 0.75, 0.9, 0.85]
    
    # Apply efficiency scaling to each link
    adjusted_caps = []
    for i, speed in enumerate(base_speeds):
        adjusted_caps.append(speed * efficiency_factors[i])
    
    # Irrelevant auxiliary variable (minor distraction)
    temp_status = "calculation_in_progress"
    
    total_capacity = sum(adjusted_caps)
    
    # Additional unrelated but harmless operation
    status_log = [f"Link {idx}: {cap:.1f} Mbps" for idx, cap in enumerate(adjusted_caps)]
    
    print(f"Result: {total_capacity}")
    
    return total_capacity

result = calculate_network_capacity()