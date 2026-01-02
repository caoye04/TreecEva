def calculate_thermal_output(efficiency_data):
    base_load = 87.5
    peak_multiplier = 1.3
    penalty_rate = 0.08

    # Misleading computations with dead-end variables
    transient_flux = base_load * 0.12
    auxiliary_buffer = [x ** 0.5 for x in range(1, 6)]
    normalization_factor = sum(auxiliary_buffer) / 5  # Not actually used later

    # Real logic begins: process efficiency map
    adjusted_values = []
    for node_id, efficiency in efficiency_data.items():
        if efficiency < 0.75:
            penalty_applied = True if node_id % 2 == 0 else False
            adjusted_eff = efficiency * (1 - penalty_rate) if penalty_applied else efficiency
        else:
            adjusted_eff = efficiency

        # Conditional expression usage (required feature)
        capped_eff = adjusted_eff if adjusted_eff <= 0.92 else 0.92
        adjusted_values.append(capped_eff * base_load)

    # Simulate load distribution across phases
    phase_outputs = []
    for i, val in enumerate(adjusted_values):
        phase_shift = 1.0 + (0.01 * (i % 3))
        phase_outputs.append(val * phase_shift)

    # Sorting not affecting final result but adds cognitive load
    sorted_phases = sorted(phase_outputs, reverse=True)
    dropped_phase = sorted_phases.pop()  # Red herring: one element removed but not used

    # Final computation
    raw_total = sum(sorted_phases)
    stability_correction = 1.05 if len(sorted_phases) > 3 else 1.0
    thermal_capacity = raw_total * stability_correction

    # Unused state tracking (distractor)
    system_health = {'nodes': len(efficiency_data), 'peak': max(phase_outputs), 'corrected': True}

    return thermal_capacity

# Main execution
if __name__ == '__main__':
    efficiency_map = {1: 0.82, 2: 0.73, 3: 0.88, 4: 0.70, 5: 0.91}
    
    # Irrelevant pre-computations
    baseline_score = sum(efficiency_map.values()) / len(efficiency_map)
    threshold_check = baseline_score >= 0.78
    metadata_log = {'version': '2.1', 'valid': threshold_check, 'timestamp': 1712345678}
    
    # Key statement
    thermal_capacity = calculate_thermal_output(efficiency_map)
    
    # Output result as required
    print(f"Result: {thermal_capacity}")