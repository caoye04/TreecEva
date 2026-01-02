def calculate_system_peak():
    base_loads = [120, 150, 130, 175, 200, 180, 160, 190]
    maintenance_factor = 0.9
    threshold = 140

    # Apply maintenance adjustment
    adjusted_loads = [load * maintenance_factor for load in base_loads]
    
    # Filter loads above threshold for peak analysis
    system_loads_filtered = [load for load in adjusted_loads if load > threshold]
    
    # Identify peak operational capacity
    peak_capacity = max(system_loads_filtered)
    
    # Irrelevant tracking variable (minor distraction)
    total_checkpoints = len(adjusted_loads)
    
    return peak_capacity

result = calculate_system_peak()
print(f"Target result: {result}")