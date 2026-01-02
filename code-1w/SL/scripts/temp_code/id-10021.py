from collections import defaultdict

# Simulate a reactor diagnostics system with state tracking and efficiency analysis
def main():
    reactor_state = {
        'core_temp': 3200,
        'neutron_flux': 1450,
        'moderator_level': 87.5,
        'control_rod_depth': 63
    }

    # Efficiency log over last 5 cycles (dummy historical data)
    efficiency_log = [0.88, 0.91, 0.87, 0.93, 0.90]

    # Auxiliary monitoring variables (not directly used in final calculation)
    safety_margin = 0.05
    threshold_breach_count = 0
    diagnostic_timestamps = ['T0', 'T1', 'T2']

    # Distractor: Unrelated sensor array (simulates red herring data)
    pressure_readings = [210, 215, 208, 212, 214]
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    normalized_pressure = avg_pressure / 220.0

    # Secondary distractor: Unused fault detection map
    fault_codes = defaultdict(lambda: 0)
    fault_codes['overheat'] = 1
    fault_codes['leak'] = 0
    fault_codes['pump_fail'] = 0

    # Intermediate computation: stability index (used indirectly)
    stability_index = (reactor_state['moderator_level'] * 1.2) - (reactor_state['control_rod_depth'] * 0.7)

    # Distractor: Dummy loop simulating data validation (no side effects)
    for code in diagnostic_timestamps:
        if code == 'T0':
            continue  # No meaningful operation

    # Core calculation function
    def calculate_thermal_output(state, log):
        base_temp = state['core_temp']
        flux_ratio = state['neutron_flux'] / 1000.0
        recent_efficiency = sum(log) / len(log)

        # Primary formula: thermal capacity based on temp, flux, and efficiency
        capacity = base_temp * flux_ratio * recent_efficiency

        # Modifier based on stability (uses intermediate variable)
        if stability_index > 60:
            capacity *= 1.1

        # Distractor: Unused conditional branch (dead code path)
        if normalized_pressure > 1.0:
            capacity *= 0.95  # Never reached due to average pressure < 220

        return int(capacity)

    # Lambda function for dynamic threshold (not used but adds complexity)
    threshold_fn = lambda x: x * 0.75 if x > 1000 else x * 0.85

    # Key execution point
    thermal_capacity = calculate_thermal_output(reactor_state, efficiency_log)

    # Additional irrelevant transformation
    formatted_capacity = f"{thermal_capacity:.0f} MW"

    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()