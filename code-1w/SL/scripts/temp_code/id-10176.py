def analyze_system_performance():
    # Simulate sensor readings from different subsystems
    temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
    pressure_readings = [101.3, 102.1, 100.7, 103.4, 101.8]
    vibration_levels = [0.45, 0.67, 0.53, 0.89, 0.76]

    # Derived metrics
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    max_vibration = max(vibration_levels)

    # Noise threshold filtering (irrelevant for final answer)
    filtered_vibrations = [v for v in vibration_levels if v > 0.5]
    vibration_spike_count = len(filtered_vibrations)

    # System state classification
    system_states = []
    for temp in temperature_readings:
        state = 'normal' if 22 <= temp <= 24 else 'elevated'
        system_states.append(state)
    
    normal_count = system_states.count('normal')
    elevated_count = system_states.count('elevated')

    # Secondary derived stats (distraction)
    temp_variance = sum((t - avg_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
    pressure_trend = pressure_readings[-1] - pressure_readings[0]

    # Core logic: efficiency depends on temp stability and pressure consistency
    temp_stable = 1 if abs(max(temperature_readings) - min(temperature_readings)) < 2.5 else 0
    pressure_stable = 1 if abs(pressure_trend) < 2.0 else 0

    # Efficiency formula
    baseline_efficiency = 85.0
    stability_bonus = 10 * temp_stable * pressure_stable
    vibration_penalty = 5 if max_vibration > 0.8 else 0
    
    # Final efficiency score calculation
    efficiency_score = baseline_efficiency + stability_bonus - vibration_penalty

    # Tracking dictionary (used to print result)
    final_metrics = {
        'baseline': baseline_efficiency,
        'stability_flag': temp_stable and pressure_stable,
        'max_vibration': max_vibration
    }
    final_metrics.update({'efficiency_score': efficiency_score})
    
    # Irrelevant debug output
    debug_info = {"run_id": "DBG_9283", "checksum": hex(hash(tuple(temperature_readings)))[:8]}
    
    # Output target variable
    print(f"Result: {efficiency_score}")

analyze_system_performance()