def analyze_system_load():
    base_loads = [120, 150, 130, 175, 200, 160, 190, 145]
    maintenance_factor = 0.9
    
    # Apply maintenance adjustment to get actual system loads
    adjusted_loads = [load * maintenance_factor for load in base_loads]
    
    # Filter out systems operating below safe threshold
    safe_threshold = 140
    system_loads_filtered = [load for load in adjusted_loads if load >= safe_threshold]
    
    # Determine peak capacity from filtered, adjusted loads
    peak_capacity = max(system_loads_filtered)
    
    # Irrelevant tracking variable (minimal distraction)
    total_hours_monitored = len(base_loads) * 8
    
    print(f"Result: {peak_capacity}")

analyze_system_load()