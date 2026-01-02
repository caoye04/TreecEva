def analyze_system_metrics():
    # Simulated sensor readings from a power grid monitoring system
    voltage_readings = [230.1, 228.7, 233.4, 229.5, 231.2]
    current_loads = [15.6, 16.1, 14.9, 16.3, 15.8]
    
    # Auxiliary diagnostic data (partially irrelevant)
    diagnostic_codes = ['OK', 'WARN_21', 'OK', 'OK', 'FAULT_9']
    temp_logs = [72.4, 73.1, 71.9, 74.0, 72.8]  # unused in final calc
    timestamp_flags = [True, False, True, True, False]

    # Step 1: Compute average power (voltage * current) per phase
    power_levels = []
    for i in range(len(voltage_readings)):
        power_levels.append(voltage_readings[i] * current_loads[i])
    
    # Step 2: Identify anomalous phases using logical checks
    anomaly_count = 0
    critical_phases = []
    for idx, code in enumerate(diagnostic_codes):
        if 'FAULT' in code or (power_levels[idx] > 3700 and current_loads[idx] > 16.0):
            anomaly_count += 1
            critical_phases.append(idx)
    
    # Step 3: Calculate stability index using enumerate and zip
    stability_index = 0.0
    for i, (v, c) in enumerate(zip(voltage_readings, current_loads)):
        deviation = abs(v - 230.0) + abs(c - 16.0)
        stability_index += deviation
        if i % 2 == 0:
            stability_index -= 0.5  # minor correction for even-indexed sensors

    # Step 4: Determine base rating from logical conditions
    base_rating = 100
    if len(critical_phases) > 0:
        base_rating -= 30
    elif anomaly_count == 0 and stability_index < 10.0:
        base_rating += 10
    
    # Irrelevant health accumulation (dead-end logic)
    system_health = 0
    for flag in timestamp_flags:
        if flag:
            system_health += 5
        else:
            system_health += 2
    system_health = min(system_health, 100)  # not used later

    # Step 5: Compute performance multiplier based on power consistency
    avg_power = sum(power_levels) / len(power_levels)
    variance = sum((p - avg_power) ** 2 for p in power_levels) / len(power_levels)
    performance_multiplier = 1.0
    if variance < 200:
        performance_multiplier = 1.2
    elif variance < 500:
        performance_multiplier = 1.0
    else:
        performance_multiplier = 0.8

    # Step 6: Compute efficiency score (TARGET STATEMENT)
    efficiency_score = base_rating * performance_multiplier

    # Final output
    print(f"Result: {efficiency_score}")

analyze_system_metrics()