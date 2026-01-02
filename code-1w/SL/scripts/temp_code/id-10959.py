def analyze_system_performance():
    components = ['sensor_a', 'sensor_b', 'actuator_x', 'controller_y']
    readings = [12, 15, 0, 8]
    statuses = [True, True, False, True]
    
    # Initialize tracking variables
    active_count = 0
    total_output = 0
    cycle_count = 0
    temp_buffer = []
    diagnostic_log = {}

    for idx, (name, value, status) in enumerate(zip(components, readings, statuses)):
        cycle_count += 1
        
        # Simulate intermediate processing with side computations
        adjusted_value = value * (1.1 if 'sensor' in name else 1.05)
        temp_buffer.append(adjusted_value)
        
        if status:
            active_count += 1
            if value > 0:
                total_output += value ** 2
        else:
            # Placeholder for potential fault recovery logic (unused path)
            recovery_factor = value + 10
            diagnostic_log[name] = recovery_factor

    # Misleading secondary calculation (not part of final result)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stability_index = avg_temp * 0.75

    # Key assignment point
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0
    
    # Redundant normalization (no effect on answer)
    normalized_efficiency = efficiency_score / 1.0
    
    print(f"Result: {efficiency_score}")

analyze_system_performance()