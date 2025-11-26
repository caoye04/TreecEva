def energy_tracker(func, data_array):
    # Distractor: complex-looking but irrelevant calculation
    temp_buffer = [x * 2 + 1 for x in data_array]
    capacity_metrics = sum(temp_buffer) // len(data_array)
    
    # Relevant: find minimum using lambda
    critical_points = [func(x) for x in data_array]
    min_energy = min(critical_points)
    
    # Distractor: misleading intermediate calculation
    thermal_efficiency = (capacity_metrics * 3.14159) / 2.71828
    unused_variable = thermal_efficiency ** 0.5
    
    # Dead code path that never executes
    if thermal_efficiency > 1000:
        redundant_check = thermal_efficiency - min_energy
    else:
        # This path is always taken
        system_optimization = min_energy + capacity_metrics
    
    # Key logic: combine minimum with adjustment
    power_adjustment = (system_optimization * 2) % 7
    optimization_result = min_energy + power_adjustment
    
    # Additional distractor calculations
    noise_reduction = [x % 5 for x in data_array]
    signal_quality = sum(noise_reduction) - len(data_array)
    
    print(f"Result: {optimization_result}")
    return optimization_result

efficiency_data = [1, 2, 3, 4, 5]
optimization_result = energy_tracker(lambda x: x**2 - 4*x + 4, efficiency_data)