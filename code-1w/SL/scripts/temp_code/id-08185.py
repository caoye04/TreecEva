def calculate_efficiency(load, capacity):
    base_efficiency = 0.85
    overload_penalty = 0.1 if load > capacity * 0.9 else 0.0
    efficiency = base_efficiency - overload_penalty
    
    # Simulate minor grid fluctuations (irrelevant to final result)
    fluctuation_factor = 1.01
    adjusted_load = load * fluctuation_factor
    
    # Distractor: unused variable simulating auxiliary monitoring
    monitor_log = [f"Load sample: {x}" for x in [load, adjusted_load] if x > 50]
    
    # Real computation path
    safety_margin = 0.95
    stress_ratio = min(load / capacity, 1.0)
    degradation = 0.02 * (stress_ratio ** 2)
    final_efficiency = efficiency - degradation
    
    return round(final_efficiency, 3)

# System parameters
capacity_readings = [120, 130, 140]
grid_load = 118
temperature_offset = 2.3  # Irrelevant telemetry
peak_capacity = max(capacity_readings)

# Key assignment statement
energy_threshold = calculate_efficiency(grid_load, peak_capacity)

print(f"Result: {energy_threshold}")