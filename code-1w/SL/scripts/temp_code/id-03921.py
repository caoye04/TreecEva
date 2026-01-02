def calculate_thermal_output(efficiency):
    base_load = 87.5
    overhead = 0.023
    adjustment_factor = 1.08

    # Distractor: Power grid simulation (not directly used)
    grid_stability = [0.98, 0.95, 0.99, 1.02]
    stability_score = sum([abs(1 - x) for x in grid_stability])
    penalty_rate = stability_score * 0.15 if stability_score > 0.1 else 0.0

    # Real computation begins
    efficiency_values = list(efficiency.values())
    avg_efficiency = sum(efficiency_values) / len(efficiency_values)

    # Conditional expression for dynamic load scaling
    load_multiplier = 1.2 if avg_efficiency > 0.8 else (1.0 if avg_efficiency > 0.6 else 0.8)

    # Intermediate irrelevant calculation (distractor)
    theoretical_max = base_load * adjustment_factor * load_multiplier
    deprecated_buffer = theoretical_max * 0.05  # Unused

    # Core thermal model
    temperature_rise = 0
    for temp in efficiency_values:
        if temp < 0.5:
            temperature_rise += 10
        elif temp < 0.75:
            temperature_rise += 5
        else:
            temperature_rise += 2

    # Final capacity depends on efficiency and rise
    normalized_rise = max(1, 10 - temperature_rise)  # Cap improvement
    thermal_capacity = (base_load * avg_efficiency * load_multiplier) / (overhead + normalized_rise * 0.01)

    # Dead code path (misleading)
    if penalty_rate > 1.0:
        thermal_capacity *= 0.9  # Never reached

    return thermal_capacity

# Main execution
config_modes = ['eco', 'performance', 'balanced']
mode_settings = {m: len(m) for m in config_modes}  # Irrelevant mapping

# Actual input data
efficiency_map = {
    'core_a': 0.82,
    'core_b': 0.78,
    'core_c': 0.85,
    'core_d': 0.63,
    'core_e': 0.91
}

# Extraneous pre-processing
filtered_cores = [k for k, v in efficiency_map.items() if v >= 0.75]
system_health = len(filtered_cores) / len(efficiency_map)

# Key statement
thermal_capacity = calculate_thermal_output(efficiency_map)

# Output result
print(f"Result: {thermal_capacity}")