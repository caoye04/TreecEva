def analyze_system_performance():
    # System diagnostics with mixed relevant and irrelevant metrics
    components = ['sensor', 'actuator', 'controller', 'transmitter']
    readings = [85, 92, 78, 88]
    
    # Irrelevant health indicators (distractor variables)
    health_status = {comp: 'OK' for comp in components}
    calibration_offsets = {'sensor': 0.12, 'actuator': -0.05, 'controller': 0.0, 'transmitter': 0.08}
    adjusted_readings = [r + calibration_offsets[c] * 10 for c, r in zip(components, readings)]

    # Relevant operational parameters
    base_capacity = 500
    overload_margin = 0.15
    stress_test_mode = True

    # Simulate workload cycles
    cycles = []
    for i, val in enumerate(readings):
        if val > 80:
            cycles.append((i + 1) * 1.2)
        else:
            cycles.append((i + 1) * 0.8)
    
    cycle_time = sum(cycles) / len(cycles)

    # Resource allocation model
    resource_map = dict(zip(components, [1.1, 0.9, 1.2, 0.8]))
    active_resources = 0
    for comp, usage in resource_map.items():
        if health_status[comp] == 'OK':
            active_resources += usage * 0.75  # Partial utilization

    resource_factor = max(active_resources, 1.0)

    # Output computation chain
    peak_reading = max(readings)
    normalized_peak = (peak_reading - 70) / 30
    scaling_factor = 1 + normalized_peak * 0.5
    
    # Secondary distraction: unused efficiency matrix
    efficiency_matrix = {
        (i, j): (readings[i] * readings[j]) ** 0.5 
        for i in range(len(readings)) 
        for j in range(i+1, len(readings))
    }
    avg_efficiency_proxy = sum(efficiency_matrix.values()) / len(efficiency_matrix) if efficiency_matrix else 0

    # Core calculation path
    load_factor = 1.0
    if stress_test_mode:
        load_factor = 1.3
    
    total_output = base_capacity * scaling_factor * load_factor * overload_margin
    
    # Critical statement — target intervention point
    efficiency_score = total_output / (cycle_time * resource_factor)
    
    # Dead code branch (never executed but adds cognitive load)
    if False:
        fallback_score = 0
        for k, v in efficiency_matrix.items():
            fallback_score += v * 0.01
        efficiency_score = fallback_score

    print(f"Result: {efficiency_score}")
    return efficiency_score

analyze_system_performance()