def calculate_system_efficiency(readings, thresholds):
    total_power = 0
    efficiency_log = []
    temp_cache = {}
    cumulative_loss = 0
    adjustment_factor = 1.05

    for i, (voltage, current) in enumerate(readings):
        if i not in temp_cache:
            temp_cache[i] = voltage * current * adjustment_factor

        raw_power = voltage * current
        total_power += raw_power

        if i % 2 == 0 and i > 0:
            total_power -= 0.5 * raw_power  # Simulated fluctuation loss

        rolling_average = total_power / (i + 1) if i >= 0 else 0

        for j, threshold in enumerate(thresholds):
            if rolling_average > threshold and j not in efficiency_log:
                efficiency_log.append(int(rolling_average // (j + 1)))

    # Misleading secondary calculation (distractor)
    redundant_calc = sum([x**2 for x in temp_cache.values() if x < 50])
    ignored_metric = redundant_calc / len(temp_cache) if temp_cache else 0

    # Core logic: compute efficiencies using slicing and zip
    sliced_log = efficiency_log[1:]  # Skip first entry
    offset_log = efficiency_log[:-1]
    
    efficiencies = []
    for a, b in zip(sliced_log, offset_log):
        if a > b:
            efficiencies.append(a - b + len(thresholds))
        else:
            efficiencies.append(b - a)

    # Add dummy baseline
    efficiencies.append(10)

    peak_efficiency = max(efficiencies)

    # Dead code path (never reached due to structure)
    if False:
        fallback = sum(efficiency_log) / len(efficiency_log)
        peak_efficiency = int(fallback)

    print(f"Result: {peak_efficiency}")

# Inputs
sensor_readings = [(12, 3), (13, 4), (11, 5), (14, 2)]
thresh_levels = [20, 30, 40]

# Execute
calculate_system_efficiency(sensor_readings, thresh_levels)