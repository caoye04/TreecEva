from itertools import compress, count

def analyze_reactor_sequence():
    # Simulate reactor core state over time with sensor fluctuations
    base_temperature = 23.5
    pressure_readings = [101.3, 102.1, 101.8, 103.5, 104.0, 103.9, 105.2]
    fluctuation_mask = [i % 2 == 0 for i in range(len(pressure_readings))]
    filtered_pressure = list(compress(pressure_readings, fluctuation_mask))  # every other reading

    # Auxiliary calculation: energy drift (not directly used)
    drift_accumulator = 0.0
    for p in pressure_readings:
        drift_accumulator += (p - 100) * 0.05

    # Reactor state vector: active zones
    reactor_state = [1, 0, 1, 1, 0, 1]
    zone_ids = list(count(1001, 1))  # [1001, 1002, 1003, ...] - just for logging

    # Efficiency degradation log over cycles
    efficiency_log = []
    temp = 1.0
    for _ in range(6):
        temp *= 0.92
        efficiency_log.append(round(temp, 4))

    # Secondary metric: stress_factor (distractor)
    stress_factor = 0
    for i, val in enumerate(reactor_state):
        if val:
            stress_factor += efficiency_log[i] ** 2

    # Critical function call embedded in logic
    thermal_capacity = calculate_thermal_output(reactor_state, efficiency_log)

    # Post-correction calibration (does not alter thermal_capacity)
    calibration_offset = sum(filtered_pressure[:3]) * 0.001
    adjusted_base = base_temperature + calibration_offset

    return thermal_capacity

def calculate_thermal_output(state, eff_log):
    output = 0
    for i, active in enumerate(state):
        if active:
            # Main physics model: capacity = index^2 * efficiency
            contribution = (i + 1) ** 2 * eff_log[i]
            output += contribution
            # Early termination if unstable
            if eff_log[i] < 0.6:
                break
    return round(output, 4)

# Execute and print result
result_value = analyze_reactor_sequence()
print(f"Result: {result_value}")