def calculate_network_load():
    base_stations = ['A', 'B', 'C', 'D']
    user_counts = [124, 156, 98, 203]
    signal_strengths = [87, 92, 76, 88]
    
    # Irrelevant intermediate calculation (mild distraction)
    avg_strength = sum(signal_strengths) / len(signal_strengths)
    threshold_met = [s > 85 for s in signal_strengths]
    
    # Core logic: compute usage level per station using user count and signal
    usage_levels = []
    for i, count in enumerate(user_counts):
        efficiency = 1.0 if threshold_met[i] else 0.85
        usage_levels.append(count * efficiency)
    
    # Key assignment
    peak_capacity = max(usage_levels)
    
    # Additional benign operation
    total_capacity = sum(usage_levels)
    
    print(f"Result: {peak_capacity}")

calculate_network_load()