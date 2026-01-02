def analyze_system_performance():
    base_loads = [120, 150, 135, 180, 200, 175, 190, 210, 165, 140]
    maintenance_factor = 0.9
    threshold = 160

    # Apply maintenance adjustment to all loads
    adjusted_loads = [load * maintenance_factor for load in base_loads]

    # Filter periods where system exceeds threshold after adjustment
    system_loads_filtered = [load for load in adjusted_loads if load > threshold]

    # Track number of high-load periods (distractor variable)
    high_load_count = len(system_loads_filtered)

    # Compute peak operational capacity
    peak_capacity = max(system_loads_filtered)

    # Print result in required format
    print(f"Target result: {peak_capacity}")

analyze_system_performance()