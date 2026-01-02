def calculate_thermal_output(efficiency, weights):
    base_output = 1200
    adjustment_factor = 0.87
    temp_storage = [base_output * (w ** efficiency) for w in weights]
    filtered_values = [val for val in temp_storage if val > 500]
    total_energy = sum(filtered_values)
    
    # Distractor: Irrelevant computation with unused variables
    peak_load = 950
    maintenance_cycle = True
    system_diagnostics = {"voltage": 220, "current": 4.5}
    diagnostic_score = system_diagnostics["voltage"] * system_diagnostics["current"]
    
    # Another red herring
    if maintenance_cycle:
        peak_load -= 50  # Not used later

    # Actual relevant logic
    safety_margin = 1.15
    final_output = total_energy / safety_margin
    
    # More distraction: simulated sensor drift correction (unused)
    sensor_drift = 0.03
    corrected_readings = [r * (1 - sensor_drift) for r in temp_storage]
    average_corrected = sum(corrected_readings) / len(corrected_readings) if corrected_readings else 0
    
    return int(final_output)

# Main execution
phase_weights = [0.6, 0.9, 1.1, 0.8, 1.3]
efficiency_ratio = 1.25
baseline_metric = 42.5

# Dummy state tracking (distractor)
current_state = "ACTIVE"
state_log = []
for i in range(3):
    state_log.append(f"{current_state}_{i}")

# Key statement
thermal_capacity = calculate_thermal_output(efficiency_ratio, phase_weights)

# Print result
print(f"Result: {thermal_capacity}")