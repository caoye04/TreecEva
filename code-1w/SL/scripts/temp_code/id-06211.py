def system_diagnostic(loads, efficiencies):
    baseline = 1.0
    peak_capacity = 0
    cumulative_stress = 0.0
    transient_buffer = []

    for idx, (load, eff) in enumerate(zip(loads, efficiencies)):
        normalized_load = load / 100.0
        performance_ratio = normalized_load * eff
        
        # Irrelevant tracking - distractor
        if idx % 2 == 0:
            transient_buffer.append(normalized_load ** 0.5)
        
        # Real logic: track peak effective capacity
        adjusted_capacity = load * eff
        if adjusted_capacity > peak_capacity:
            peak_capacity = adjusted_capacity

        # Misleading cumulative calculation
        stress_factor = (1 - eff) * normalized_load
        cumulative_stress += stress_factor

        # Dead code path - never executed but looks relevant
        if False:
            baseline *= 0.95

    # Secondary loop with semi-relevant filtering
    filtered_efficiencies = [e for e in efficiencies if e >= 0.75]
    efficiency_boost = len(filtered_efficiencies) * 0.05

    # Final adjustment that does NOT affect peak_capacity
    final_stress_score = cumulative_stress / len(loads) if loads else 0
    
    # Distractor: unused synthetic metric
    synthetic_index = sum(loads) * efficiency_boost

    # Key statement: final_analysis includes peak_capacity
    final_analysis_data = {
        'capacity': peak_capacity,
        'stress': final_stress_score,
        'boost': efficiency_boost
    }
    
    return final_analysis_data

# Input data
grid_loads = [85, 90, 95, 88, 92]
efficiency_rates = [0.82, 0.85, 0.78, 0.90, 0.84]

# Execution
final_analysis = system_diagnostic(grid_loads, efficiency_rates)
peak_capacity = final_analysis['capacity']
print(f"Result: {peak_capacity}")