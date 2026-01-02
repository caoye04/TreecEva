def calculate_thermal_output(state):
    base_yield = 23.7
    modifier = 1.8 if state['temperature'] > 450 else 0.9
    efficiency = len(state['cores']) * modifier
    decay_factor = sum([v ** 0.5 for v in state['output_history']]) / 100
    
    # Distractor: Irrelevant computation with unused variables
    dummy_data = {x: x**2 for x in range(10)}
    temp_cache = [i * 1.5 for i in range(len(dummy_data))]
    cached_sum = sum(temp_cache) / (len(temp_cache) + 1e-5)
    
    # Semi-relevant but not critical set operation
    active_sensors = {'s1', 's2', 's3', 's4'}
    failed_sensors = {'s3'}
    operational_sensors = active_sensors - failed_sensors
    sensor_correction = len(operational_sensors) * 0.1
    
    # Core calculation chain
    raw_output = base_yield * efficiency * decay_factor
    stability_penalty = 0.0
    if state['fluctuation_index'] > 0.7:
        stability_penalty = raw_output * 0.15
    elif state['fluctuation_index'] > 0.3:
        stability_penalty = raw_output * 0.05
    
    final_output = raw_output - stability_penalty + sensor_correction
    return round(final_output, 4)

# Initialization of reactor state
reactor_state = {
    'temperature': 480,
    'cores': ['core_A', 'core_B'],
    'output_history': [16, 25, 36],
    'fluctuation_index': 0.5,
    'last_maintenance': '2023-11-05'
}

# Unused but misleading variable assignments
maintenance_days = 30
redundancy_check = [False, True, True]
consistency_flag = all(redundancy_check)

# Key execution point
thermal_capacity = calculate_thermal_output(reactor_state)

# Output result
print(f"Result: {thermal_capacity}")