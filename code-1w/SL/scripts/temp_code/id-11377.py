def calculate_thermal_response(input_energy, threshold=450):
    activation_level = 0
    decay_rate = 0.98
    base_yield = input_energy * 1.75
    
    # Simulate preliminary sensor readings (distractor computations)
    sensor_a = (input_energy + 127) % 89
    sensor_b = (input_energy * 2 + 41) % 97
    diagnostic_flag = True if sensor_a > sensor_b else False
    
    # Secondary energy absorption phase (semi-relevant)
    absorbed = input_energy * 0.85
    residual = input_energy - absorbed
    adjustment_cycle = 0
    
    while residual > 50 and adjustment_cycle < 3:
        residual *= decay_rate
        adjustment_cycle += 1
    
    # Determine operational mode based on threshold
    mode = 'high' if input_energy >= threshold else 'normal'
    
    # Efficiency calculation with conditional expression
    efficiency_factor = 1.2 if mode == 'high' and diagnostic_flag else 0.85
    
    # Key computation: thermal output
    thermal_output = base_yield * efficiency_factor
    
    # Post-processing diagnostics (irrelevant to final result)
    final_diagnostic = f'Mode: {mode}, Cycles: {adjustment_cycle}'
    log_entry = len(final_diagnostic)  # unused variable
    
    # Print final result as required
    print(f"Result: {thermal_output}")
    
    return thermal_output

# Execute with fixed input
result = calculate_thermal_response(320)