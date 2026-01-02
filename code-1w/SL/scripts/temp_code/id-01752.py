def calculate_energy_profile():
    base_load = 127
    peak_multiplier = 1.8
    system_active = True
    
    # Simulate sensor readings for load distribution
    sensor_a = base_load * 0.9
    sensor_b = base_load * 1.1
    sensor_c = base_load * 0.95
    operational_loads = [sensor_a, sensor_b, sensor_c]
    
    standby_loads = [base_load * 0.1, base_load * 0.05, base_load * 0.2]
    
    # Irrelevant calibration offset (minimal distraction)
    calibration_offset = 3.2
    
    energy_threshold = min(operational_loads) if system_active else max(standby_loads)
    
    # Additional unrelated computation (low interference)
    efficiency_ratio = (sum(operational_loads) / len(operational_loads)) / base_load
    
    return energy_threshold

result = calculate_energy_profile()
print(f"Result: {result}")