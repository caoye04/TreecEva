def calculate_efficiency(load):
    base_factor = 0.85
    peak_modifier = 1.2 if load > 75 else 0.9
    efficiency = load * base_factor * peak_modifier
    return int(efficiency)

# System calibration data (irrelevant but plausible)
calibration_offset = 5
system_uptime_hours = 120

# Network load simulation
current_load = 80

# Efficiency calculation based on current network load
energy_threshold = calculate_efficiency(current_load)

# Additional telemetry (distractor variables)
telemetry_data = [12, 45, 67, energy_threshold, 91]
data_quality_score = sum([x > 50 for x in telemetry_data])

# Final output
print(f"Result: {energy_threshold}")