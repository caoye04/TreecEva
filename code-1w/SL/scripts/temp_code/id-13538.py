def analyze_production_cycle(units_produced, downtime_hours, base_capacity):
    peak_performance = 0
    efficiency_log = []
    total_waste = 0
    adjustment_factor = 0.95

    for hour, units in enumerate(units_produced):
        if units > base_capacity:
            peak_performance += 1
            overflow = units - base_capacity
            total_waste += overflow * 0.1  # 10% loss on overproduction

        hourly_efficiency = units / base_capacity
        efficiency_log.append(round(hourly_efficiency, 3))

    # Simulate maintenance impact
    maintenance_penalty = 0
    for i in range(len(downtime_hours)):
        if downtime_hours[i] > 2:
            maintenance_penalty += 0.05

    # Compute cycle time with weighted factors
    raw_cycle_time = len(units_produced)
    adjusted_cycle_time = raw_cycle_time - len(downtime_hours) + maintenance_penalty

    # Distractor: unused variables and irrelevant computation
    theoretical_max = base_capacity * raw_cycle_time
    phantom_load = sum([x * 0.02 for x in units_produced if x < base_capacity])
    debug_checksum = sum([i * val for i, val in enumerate(units_produced)]) % 17

    total_output = sum(units_produced)
    cycle_time = adjusted_cycle_time if adjusted_cycle_time > 0 else 1

    # Key statement
    efficiency_score = total_output / (cycle_time * 0.95)

    # Additional red herring logic
    if len(efficiency_log) > 5:
        smoothed = sum(efficiency_log[-3:]) / 3
        if smoothed > 0.8:
            efficiency_score *= 1.02

    # Irrelevant string processing using required Python feature
    status_codes = ['OK', 'WARN', 'OK', 'FAULT', 'OK']
    code_frequency = {}
    for idx, code in enumerate(status_codes):
        code_frequency[code] = code_frequency.get(code, 0) + idx

    metadata_tags = ['A1', 'B2', 'C3', 'D4']
    paired_data = list(zip(efficiency_log[::2], metadata_tags))

    # Final output
    print(f"Result: {efficiency_score}")

analyze_production_cycle([85, 90, 95, 100, 87, 93], [0, 0, 1, 0, 2], 100)