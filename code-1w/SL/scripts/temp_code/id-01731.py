def calculate_thermal_profile():
    temperatures = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 29.1]
    pressure_readings = [101.3, 102.1, 103.5, 104.0, 105.2, 106.8, 107.0]
    
    # Irrelevant preprocessing: normalize pressures (not used in final calculation)
    normalized_pressures = [round((p - min(pressure_readings)) / (max(pressure_readings) - min(pressure_readings)), 4) for p in pressure_readings]
    
    # Distractor: unused transformation
    transformed_temps = []
    for i, temp in enumerate(temperatures):
        if i % 2 == 0:
            transformed_temps.append(temp ** 1.1)
        else:
            transformed_temps.append(temp + 0.5)

    # Real data processing begins
    avg_temp = sum(temperatures) / len(temperatures)
    temp_deviation_set = {round(abs(t - avg_temp), 2) for t in temperatures}
    valid_deviations = [d for d in sorted(temp_deviation_set) if d > 0.5]

    # Simulate sensor validation flags
    validation_flags = []
    for i, (t, p) in enumerate(zip(temperatures, pressure_readings)):
        flag = (i % 3 == 0) or (p > 104.0)
        validation_flags.append(flag)
    
    # Compute base flux from average temperature and count of valid deviations
    base_flux = avg_temp * len(valid_deviations)
    
    # Efficiency factor determined by conditional logic and enumeration
    efficiency_accumulator = 0.0
    for idx, dev in enumerate(valid_deviations):
        if idx < 2:
            efficiency_accumulator += 0.1
        elif dev > 1.0:
            efficiency_accumulator += 0.05
    
    # Introduce misleading alternate path (never taken due to prior filtering)
    fallback_correction = 0
    if len([x for x in temp_deviation_set if x < 0.1]) > 0:
        fallback_correction = 1.5  # Dead code branch
    
    efficiency_factor = max(0.8, efficiency_accumulator) if efficiency_accumulator > 0 else 0.75
    
    # Key statement
    thermal_capacity = base_flux * efficiency_factor
    
    # Print result as required
    print(f"Result: {thermal_capacity}")
    
    return thermal_capacity

result = calculate_thermal_profile()