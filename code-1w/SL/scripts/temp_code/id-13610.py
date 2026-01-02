def calculate_network_flow():
    base_rate = 17.5
    peak_multiplier = 1.6
    threshold = 25
    
    # Simulate sensor readings (some are red herrings)
    sensor_a = 8
    sensor_b = 14
    sensor_c = 9
    checksum = sensor_a + sensor_b + sensor_c  # Not used in final logic
    
    inflow = int(base_rate * peak_multiplier)
    outflow = 12
    
    # Auxiliary calculations for system health (distractors)
    load_factor = (inflow / 30.0) if outflow > 0 else 0.0
    warning_level = 'HIGH' if load_factor > 0.8 else 'NORMAL'
    
    # Simulated backup values
    reserve_flow = 8
    emergency_cap = 5
    
    # Core logic with conditional expression
    net_flow = inflow - outflow if inflow > threshold else reserve_flow
    
    # Dead code path - never executed due to fixed conditions
    if False:
        net_flow += emergency_cap
        overflow_log = [inflow, outflow]
    
    # Additional irrelevant aggregation
    total_sensors = sum([sensor_a, sensor_b, sensor_c])
    avg_sensor = total_sensors / 3
    
    # Final adjustment independent of sensors
    if net_flow > 10:
        net_flow -= 2
    
    return net_flow

result = calculate_network_flow()
print(f"Target result: {result}")