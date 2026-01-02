def calculate_energy_settings(hour, load_level):
    base_capacity = 1200
    standby_load = 300
    is_peak_hour = (hour >= 17 and hour <= 19)
    
    # Preliminary adjustment based on grid status
    grid_stress_factor = 1.1 if load_level > 1000 else 1.0
    adjusted_load = int(load_level * grid_stress_factor)
    
    # Determine energy threshold using conditional expression
    energy_threshold = load_level if is_peak_hour else min(standby_load, base_capacity)
    
    # Secondary safety check (does not affect energy_threshold)
    safety_margin = 50
    max_allowed = base_capacity - safety_margin
    system_status = 'CRITICAL' if adjusted_load > max_allowed else 'NORMAL'
    
    # Output result
    print(f"Result: {energy_threshold}")
    return energy_threshold

# Execute with specific input
calculate_energy_settings(18, 950)