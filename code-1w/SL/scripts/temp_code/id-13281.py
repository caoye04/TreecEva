def calculate_system_response():
    # Simulate a thermal regulation system with sensor inputs
    temperatures = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 21.4]
    thresholds = {'low': 20.0, 'high': 25.0}

    # Irrelevant derived metric: average deviation (not used later)
    avg_temp = sum(temperatures) / len(temperatures)
    deviations = [abs(t - avg_temp) for t in temperatures]
    avg_deviation = sum(deviations) / len(deviations)

    # Count how many readings are out of optimal range
    excursion_count = 0
    stable_intervals = 0
    for temp in temperatures:
        if temp < thresholds['low'] or temp > thresholds['high']:
            excursion_count += 1
        else:
            stable_intervals += 1

    # Compute base flow rate based on stability
    base_flow = 100 if stable_intervals >= 4 else 60

    # Adjust flow if there were more than 2 excursions
    adjustment_factor = 0.85 if excursion_count > 2 else 1.0
    adjusted_flow = base_flow * adjustment_factor

    # Efficiency depends on XOR pattern of counts (bitwise mix)
    pattern_key = stable_intervals ^ excursion_count
    efficiency_map = {}
    for i in range(10):
        efficiency_map[i] = 0.9 + (i % 3) * 0.05  # Irregular mapping

    # Only specific keys are valid; others default to 0.95
    efficiency_factor = efficiency_map.get(pattern_key % 10, 0.95)

    # Final computation step — critical assignment
    final_flux = adjusted_flow * efficiency_factor

    # Dead code: post-processing that doesn't affect result
    if final_flux > 90:
        status = "OPTIMAL"
    elif final_flux > 70:
        status = "STABLE"
    else:
        status = "LOW_FLOW"

    # Print final result as required
    print(f"Result: {final_flux}")

    return final_flux

# Execute function
calculate_system_response()