def calculate_optimal_yield(temps, pressures):
    # Simulate a scientific experiment analyzing reaction yield under varying conditions
    base_multiplier = 1.5
    adjustment_factor = 0.8
    cumulative_error = 0.0
    temp_threshold = 75
    pressure_margin = 10

    # Irrelevant tracking variables (distractors)
    readings_count = len(temps)
    high_temp_events = 0
    stability_score = 0
    fluctuation_log = []

    # Preprocess: filter valid temperature-pressure pairs
    valid_conditions = []
    for i in range(len(temps)):
        if temps[i] > 0 and pressures[i] > 0:  # Only consider physically valid readings
            valid_conditions.append((temps[i], pressures[i]))

    # Compute derived metrics (some unused later)
    temp_avg = sum(t for t, p in valid_conditions) / len(valid_conditions)
    pressure_avg = sum(p for t, p in valid_conditions) / len(valid_conditions)

    # Distractor: analyze fluctuations (not used in final result)
    for i in range(1, len(valid_conditions)):
        delta_t = abs(valid_conditions[i][0] - valid_conditions[i-1][0])
        delta_p = abs(valid_conditions[i][1] - valid_conditions[i-1][1])
        fluctuation_log.append((delta_t, delta_p))
        if delta_t > 5 or delta_p > 8:
            stability_score += 1

    # Identify high-temp events (distractor)
    for t, p in valid_conditions:
        if t > temp_threshold:
            high_temp_events += 1

    # Core logic: compute yield using specific formula
    adjusted_sum = 0.0
    efficiency_map = {}
    for idx, (t, p) in enumerate(valid_conditions):
        # Efficiency depends on normalized deviation from average
        t_norm = (t - temp_avg) / temp_avg
        p_norm = (p - pressure_avg) / pressure_avg

        # Efficiency calculated but only conditionally applied
        efficiency = (1 + t_norm) * (1 + p_norm)
        efficiency_map[idx] = efficiency

        # Only use efficiencies within acceptable range
        if abs(t_norm) < 0.25 and abs(p_norm) < 0.3:
            adjusted_sum += efficiency * base_multiplier

    # Secondary adjustment using lambda (key python feature)
    apply_correction = lambda x, f: x * f if x > 0 else x
    corrected_yield = apply_correction(adjusted_sum, adjustment_factor)

    # Dictionary operation to count efficiency categories (distractor)
    category_count = {'high': 0, 'medium': 0, 'low': 0}
    for e in efficiency_map.values():
        if e > 1.2:
            category_count['high'] += 1
        elif e > 0.8:
            category_count['medium'] += 1
        else:
            category_count['low'] += 1

    # Final yield depends only on corrected_yield and number of valid conditions
    final_yield = corrected_yield + len(valid_conditions) * 0.1

    return final_yield

# Experimental data
temperature_data = [68, 72, 74, 80, 85, 69, 71]
pressure_data = [22, 25, 24, 30, 35, 23, 26]

# Execute main computation
final_yield = calculate_optimal_yield(temperature_data, pressure_data)
print(f"Result: {final_yield}")