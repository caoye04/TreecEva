def analyze_system_performance(parameters):
    base_rating = 0
    efficiency_factor = 1.0
    thermal_capacity = 0
    transient_load = 0
    calibration_offset = 0.023
    
    # Initial setup from sensor array
    for idx, (sensor_id, reading) in enumerate(zip([101, 102, 103], [23.5, 24.1, 22.7])):
        base_rating += int(reading)
        if idx % 2 == 0:
            transient_load += reading * 0.1
    
    base_rating = max(15, min(base_rating, 75))
    
    # Simulate signal drift compensation (distractor block)
    drift_accumulator = 0.0
    for cycle in range(3):
        drift_accumulator += calibration_offset
        calibration_offset *= 0.9  # Decay over time
    
    # Efficiency calculation with conditional modifiers
    adjustment_flags = [True, False, True]
    flag_influence = 0
    for i, flag in enumerate(adjustment_flags):
        if flag:
            flag_influence += 0.1 * (i + 1)
    
    efficiency_factor = 0.8 + flag_influence  # results in 1.0
    
    # Critical assignment point
    thermal_capacity = base_rating * efficiency_factor
    
    # Post-processing red herring (does not affect result)
    diagnostics = []
    for j, val in enumerate([transient_load, drift_accumulator]):
        diagnostics.append(f"D{str(j)}: {val:.3f}")
    
    print(f"Result: {thermal_capacity}")

# Execute function
params = {'nodes': 3, 'threshold': 0.75}
analyze_system_performance(params)