def analyze_system_efficiency(config, runtime_data):
    base_threshold = config['threshold']
    scaling_factor = config['scale']
    
    # Extract relevant metrics
    baseline = runtime_data['init_power']
    execution_time = runtime_data['exec_time_sec']
    energy_used = runtime_data['energy_kwh']
    temp_fluctuation = runtime_data['temp_change_c']  # Distractor: not used in final calc

    # Auxiliary computation - looks important but only partially relevant
    efficiency_ratio = (baseline / (execution_time + 1)) * scaling_factor
    thermal_loss = temp_fluctuation * 0.78  # Dead computation

    # Simulated fault detection (no impact on result)
    if efficiency_ratio > base_threshold:
        status_flag = 1
        recovery_sequence = [0] * 3
    else:
        status_flag = 0
        recovery_sequence = None

    # Core logic disguised among other ops
    def calculate_performance(base, time, energy):
        # Conditional expression usage (required feature)
        penalty = 10 if time > 50 else 5
        
        # Bitwise mix of base and energy (relevant)
        intermediate = (base ^ int(energy)) & 0xFF
        
        # Modular arithmetic with nested condition
        if time > 0:
            performance = (intermediate * scaling_factor) % base_threshold
            if performance % 2 == 0:
                performance += penalty
        else:
            performance = base_threshold

        # Extra logic branch that doesn't trigger due to data
        if energy < 0:
            performance = -1  # Unreachable
            
        return performance

    # Secondary distraction: system health simulation
    health_metrics = []
    for i in range(3):
        val = (scaling_factor * i) % 7
        health_metrics.append(val)  # Collected but unused

    # Critical assignment
    final_score = calculate_performance(baseline, execution_time, energy_used)
    
    # Output required format
    print(f"Result: {final_score}")
    
    return final_score

# Inputs
configuration = {
    'threshold': 23,
    'scale': 4
}

runtime_stats = {
    'init_power': 17,
    'exec_time_sec': 68,
    'energy_kwh': 12.0,
    'temp_change_c': 3.5
}

# Execute
analyze_system_efficiency(configuration, runtime_stats)