import itertools

# Environmental sensor simulation with data filtering and capacity calculation
def analyze_thermal_system():
    temperatures = [22.5, 23.0, 24.8, 25.1, 26.0, 27.3, 28.0, 29.5]
    humidity_readings = [45, 47, 50, 52, 55, 58, 60, 63]
    pressure_data = [1013, 1012, 1010, 1009, 1008, 1007, 1006, 1005]

    # Simulate time-series alignment using itertools
    time_aligned = list(itertools.zip_longest(temperatures, humidity_readings, pressure_data, fillvalue=0))

    # Derived metrics (some are red herrings)
    avg_temp = sum(temperatures) / len(temperatures)
    total_humidity = sum(humidity_readings)
    max_pressure = max(pressure_data)
    temp_variance = sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)
    temp_amplitude = max(temperatures) - min(temperatures)

    # Irrelevant transformation chain (distractor)
    normalized_humidity = [h / 100 for h in humidity_readings]
    scaled_pressure = [p / max_pressure for p in pressure_data]
    derived_ratio = sum(normalized_humidity) / (sum(scaled_pressure) + 1e-8)

    # Core system parameters (only some are used)
    base_capacity = 1500
    load_fluctuation = temp_amplitude * 10
    stress_factor = 1 + (temp_variance / 100)
    degradation_rate = 0.02 * (max(temperatures) - 20)

    # Efficiency computation with conditional adjustment (short-circuit logic)
    high_load = load_fluctuation > 30
    stable_conditions = temp_variance < 2.0
    efficiency_factor = 0.9 if high_load and stable_conditions else 0.75

    # Redundant state tracking (dead code path)
    system_status = {}
    if degradation_rate > 0.3:
        system_status['state'] = 'degraded'
        system_status['maintenance_due'] = True
    else:
        system_status['state'] = 'optimal'
        system_status['maintenance_due'] = False  # Not used later

    # Key assignment point
    thermal_capacity = base_capacity * efficiency_factor

    # Post-computation distraction
    projected_loss = thermal_capacity * degradation_rate
    adjusted_capacity = thermal_capacity - projected_loss
    capacity_margin = adjusted_capacity * 0.1

    # Final result output
    print(f"Result: {thermal_capacity}")

analyze_thermal_system()