def analyze_system_performance():
    base_load = 42
    peak_threshold = 85
    response_times = [120, 80, 95, 60, 110]
    throughput_data = [70, 85, 77, 90, 88]
    
    # Irrelevant historical metrics (distractor)
    legacy_avg_latency = 95.3
    calibration_offset = 0.98
    temp_debug_log = [base_load * 0.1 for _ in range(5)]
    
    # Core state variables
    active_nodes = 4
    maintenance_mode = False
    system_stress = sum(1 for rt in response_times if rt > peak_threshold) / len(response_times)
    avg_throughput = sum(throughput_data) / len(throughput_data)
    
    # Misleading intermediate calculation (not used later)
    predicted_failure_rate = (system_stress * 100) ** 0.5 if system_stress > 0.3 else 0
    
    # Conditional logic with distractors
    if avg_throughput >= 80:
        performance_tier = 'high'
        stress_multiplier = 1.2
    elif avg_throughput >= 70:
        performance_tier = 'medium'
        stress_multiplier = 1.0
    else:
        performance_tier = 'low'
        stress_multiplier = 0.8

    # Secondary distraction: unused node efficiency map
    node_efficiency_map = {i: (throughput_data[i] / response_times[i]) * stress_multiplier 
                          for i in range(len(throughput_data))}
    
    # Key computation path
    baseline_efficiency = avg_throughput * (1 - system_stress)
    adjustment_factor = 0.9 if maintenance_mode else 1.1
    
    # Complex conditional expression combining multiple factors
    tier_bonus = 10 if performance_tier == 'high' else (5 if performance_tier == 'medium' else 0)
    
    # Simulated final processing phase
    final_processing = True
    efficiency_score = (baseline_efficiency * adjustment_factor + tier_bonus) * stress_multiplier
    
    # Dead code branch (never executed)
    if False:
        efficiency_score *= calibration_offset
        active_nodes += 1
    
    # Output the target result
    print(f"Result: {efficiency_score}")

analyze_system_performance()