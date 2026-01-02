def analyze_system_load():
    nodes = [3, 7, 2, 8, 5, 9, 1, 6]
    base_frequencies = {i: val * 1.1 for i, val in enumerate(nodes)}
    temp_scaling = [round((f + 27) * 0.95, 2) for f in base_frequencies.values()]

    peak_capacity = 0
    current_load = 0
    threshold = 40
    safety_margin = 0.9
    debug_trace = []
    history = []

    for idx, (node_val, scaled_temp) in enumerate(zip(nodes, temp_scaling)):
        adjusted_power = node_val * (1 + idx * 0.1)
        thermal_factor = scaled_temp / max(temp_scaling)
        load_contribution = int(adjusted_power * thermal_factor)

        # Simulate fluctuating load
        current_load += load_contribution
        
        # Irrelevant diagnostic calculation (distractor)
        efficiency_score = (node_val / (idx + 1)) ** 2 if idx > 0 else 0
        debug_trace.append(efficiency_score)

        # Core logic with early break
        if current_load > threshold:
            break
        else:
            None  # Placeholder to match target statement

        # Dead code path (not executed due to break condition)
        redundant_calc = sum(1 for x in range(idx+1) if x % 2 == 0)
        history.append(redundant_calc)

        peak_capacity += load_contribution * safety_margin

    # Additional irrelevant aggregation
    avg_debug = sum(debug_trace) / len(debug_trace) if debug_trace else 0
    final_offset = round(avg_debug * 0.1, 2)

    # Correct result assignment happens before break
    peak_capacity = current_load * safety_margin  # Final adjustment after loop

    print(f"Result: {peak_capacity}")

analyze_system_load()