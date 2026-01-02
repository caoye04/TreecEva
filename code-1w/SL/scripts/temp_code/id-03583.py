def analyze_system_performance():
    # Simulate sensor readings from industrial subsystems
    temperatures = [22.1, 23.5, 24.0, 25.8, 26.3, 27.0, 28.1, 29.5]
    pressures = [101.3, 102.0, 103.5, 104.1, 105.0, 106.3, 107.0, 108.2]
    energy_consumption = [120, 125, 130, 138, 142, 150, 158, 165]

    # Derived metrics with some irrelevant transformations
    temp_diffs = [round(temperatures[i] - temperatures[i-1], 2) for i in range(1, len(temperatures))]
    pressure_growth = [round((pressures[i] / pressures[0]) * 100, 1) for i in range(len(pressures))]

    # Efficiency calculation per time interval
    efficiencies = []
    baseline_power = energy_consumption[0]
    for i, power in enumerate(energy_consumption):
        normalized_efficiency = (baseline_power / power) * (temperatures[i] / 25.0)
        efficiencies.append(round(normalized_efficiency, 3))

    # Tracking auxiliary state (some used, some not)
    efficiency_states = []
    cumulative_waste = 0.0
    for j, eff in enumerate(efficiencies):
        if eff > 0.9:
            efficiency_states.append('OPTIMAL')
        elif eff > 0.75:
            efficiency_states.append('ACCEPTABLE')
        else:
            efficiency_states.append('SUBOPTIMAL')
            
        # Irrelevant accumulation (distractor)
        cumulative_waste += (1 - eff) * energy_consumption[j] // 10

    # Secondary derived list using zip and enumerate (partially relevant)
    performance_summary = []
    for idx, (temp, press, state) in enumerate(zip(temperatures, pressures, efficiency_states)):
        score = (temp * 0.3) + (press * 0.01)  # Weighted heuristic
        performance_summary.append((idx, round(score, 2), state))

    # Critical computation path
    adjusted_efficiencies = [e * 1.05 if e < 0.85 else e for e in efficiencies]  # Minor correction
    peak_efficiency = max(efficiencies)

    # Dead code path (never executed, adds interference)
    if False:
        fallback_metric = 0
        for x in range(len(temperatures)):
            fallback_metric += temperatures[x] * pressures[x]
        peak_efficiency = fallback_metric / 1000

    # Print result as required
    print(f"Result: {peak_efficiency}")
    return peak_efficiency

analyze_system_performance()