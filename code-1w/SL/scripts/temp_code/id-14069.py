def calculate_system_efficiency(load_levels):
    base_efficiency = 85.5
    efficiency_scores = [(base_efficiency + load * 2.3) for load in load_levels if load > 0]
    
    # Irrelevant diagnostic log
    debug_mode = True
    if debug_mode:
        log_entries = len(efficiency_scores)

    system_multiplier = 1.15
    peak_capacity = max(efficiency_scores) * system_multiplier
    return peak_capacity

loads = [12, -5, 0, 18, 7]
result = calculate_system_efficiency(loads)
print(f"Target result: {result}")