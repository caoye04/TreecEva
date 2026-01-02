def analyze_power_grid():
    voltage_stable = True
    current_peak = 145.7
    threshold = 130.0
    base_level = 85
    safety_factor = 1.2
    max_surge = 205

    # Preliminary diagnostics (irrelevant to final result)
    diagnostic_code = 0x2B
    system_uptime_hours = 1876

    # Key decision logic
    energy_threshold = max_surge if (voltage_stable and current_peak > threshold) else base_level * safety_factor

    # Post-analysis logging (no effect on outcome)
    log_entry = f"Threshold set: {energy_threshold}"

    print(f"Result: {energy_threshold}")

analyze_power_grid()