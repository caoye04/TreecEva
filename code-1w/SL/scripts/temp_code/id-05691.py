def analyze_system_performance():
    # Simulate sensor data from a power grid subsystem
    sensor_readings = [23.4, 19.1, 27.8, 22.5, 31.0, 29.3, 24.2, 26.7]
    
    # Irrelevant preprocessing: normalize unrelated metric
    normalized_load = [round((x - min(sensor_readings)) / (max(sensor_readings) - min(sensor_readings)), 3) for x in sensor_readings]
    avg_normalized = sum(normalized_load) / len(normalized_load)

    # Extract critical phase readings using slicing
    startup_phase = sensor_readings[:3]  # First three readings
    operational_phase = sensor_readings[3:]  # Remaining readings

    # Compute base metrics
    avg_startup = sum(startup_phase) / len(startup_phase)
    avg_operational = sum(operational_phase) / len(operational_phase)

    # Simulate configuration flags
    system_mode = 'high_throughput'
    debug_flag = False

    # Auxiliary computation - does not affect final result
    if debug_flag:
        print(f'Startup Avg: {avg_startup}, Operational Avg: {avg_operational}')

    # Determine base rating from operational stability
    variance = sum((x - avg_operational) ** 2 for x in operational_phase) / len(operational_phase)
    stability_factor = 1 / (1 + variance)  # Higher variance = lower stability

    # Prepare performance tuple (target_ratio, actual_ratio)
    performance_ratios = (0.85, 0.94)
    ratio_difference = performance_ratios[1] - performance_ratios[0]

    # Calculate conditional boost based on improvement
    if ratio_difference > 0.05:
        performance_boost = 0.15
    else:
        performance_boost = 0.08

    # Dead code path - never executed due to fixed mode
    if system_mode == 'maintenance':
        performance_boost *= 0.5

    # Core calculation variables
    base_rating = avg_operational * stability_factor
    temp_adjustment = (base_rating + avg_normalized) * 0.01  # Unused distraction

    # Key statement
    efficiency_score = base_rating * (1 + performance_boost)
    
    # Final output
    return efficiency_score

result = analyze_system_performance()
print(f'Result: {result}')