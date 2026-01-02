def analyze_system_performance():
    # Simulated sensor readings from industrial subsystems
    temperatures = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 23.7]
    pressures = [101.3, 102.1, 100.9, 103.2, 101.8, 102.5, 101.6]
    energy_consumption = [880, 905, 870, 930, 895, 915, 885]
    
    # Irrelevant derived metrics (distractors)
    avg_temp = sum(temperatures) / len(temperatures)
    total_pressure = sum(pressures)
    temp_pressure_product = [t * p for t, p in zip(temperatures, pressures)]
    fluctuation_index = sum(abs(temperatures[i] - temperatures[i-1]) for i in range(1, len(temperatures)))
    
    # Core analysis: compute efficiency ratios based on normalized consumption and pressure
    normalized_consumption = [(ec - min(energy_consumption)) / (max(energy_consumption) - min(energy_consumption)) for ec in energy_consumption]
    normalized_pressure = [(p - min(pressures)) / (max(pressures) - min(pressures)) for p in pressures]
    
    # Compute ratio of normalized values; this is critical
    raw_ratios = []
    for i, (norm_c, norm_p) in enumerate(zip(normalized_consumption, normalized_pressure)):
        if norm_p > 0:
            raw_ratios.append(norm_c / norm_p)
        else:
            raw_ratios.append(0)
    
    # Apply smoothing filter (only affects transient behavior, not max)
    smoothed_ratios = []
    for i in range(len(raw_ratios)):
        window = raw_ratios[max(0, i-1):min(i+2, len(raw_ratios))]
        smoothed_ratios.append(sum(window) / len(window))
    
    # Normalize again to [0,1] range
    min_ratio = min(smoothed_ratios)
    max_ratio = max(smoothed_ratios)
    normalized_ratios = [(r - min_ratio) / (max_ratio - min_ratio) if max_ratio != min_ratio else 0 for r in smoothed_ratios]
    
    # Critical assignment point
    efficiency_score = max(normalized_ratios)
    
    # Dead code path (never executed, adds distraction)
    if False:
        backup_system_load = 0
        for idx, val in enumerate(temperatures):
            if val > avg_temp:
                backup_system_load += energy_consumption[idx]
    
    # Unused intermediate variables (increase cognitive load)
    zipped_data = list(zip(enumerate(temperatures), pressures))
    outlier_count = len([t for t in temperatures if abs(t - avg_temp) > 0.5])
    
    return efficiency_score

result = analyze_system_performance()
print(f"Target result: {result}")