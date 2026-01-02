def calculate_thermal_capacity(data, idx_list):
    base_multiplier = 1.75
    adjustment_factor = 0.89
    temp_offset = 273.15
    cumulative_sum = 0.0
    
    # Irrelevant pre-processing: simulates data calibration but unused
    calibrated_readings = []
    for i in range(len(data)):
        adjusted_val = data[i][1] * adjustment_factor + temp_offset
        calibrated_readings.append(adjusted_val)
    
    # Distractor loop: processes unrelated sensor flags
    stability_flags = {}
    for i, entry in enumerate(data):
        flag_key = f"sensor_{i}"
        stability_flags[flag_key] = entry[1] > 50 and entry[0] in ['A', 'B']

    # Relevant logic: sum selected temperature-pressure products with index mapping
    mapped_indices = {i: idx for i, idx in enumerate(idx_list)}
    pressure_contributions = []
    
    for pos, idx in mapped_indices.items():
        if idx < len(data):
            temp_k = data[idx][1] + temp_offset  # Convert to Kelvin
            pressure_hpa = data[idx][2]
            contribution = temp_k * pressure_hpa
            pressure_contributions.append(contribution)
    
    # Secondary distractor: sorting has no effect on final sum
    pressure_contributions.sort(reverse=True)
    
    # Actual accumulation for result
    for val in pressure_contributions:
        cumulative_sum += val * base_multiplier
    
    final_capacity = cumulative_sum / (len(pressure_contributions) or 1)
    return int(final_capacity)

# Main execution context
fluid_data = [
    ('A', 25, 1013),   # Temp in C, pressure in hPa
    ('B', 45, 980),
    ('C', 60, 1020),
    ('A', -10, 950),
    ('B', 33, 1005)
]

indices = [0, 2, 4]

# Simulated diagnostic trace (dead code path - irrelevant)
diagnostic_log = []
for i, (tag, t, p) in enumerate(fluid_data):
    status = 'OK' if t > 0 else 'WARNING'
    diagnostic_log.append(f"{tag}_{i}:{status}")

# Key computation step
thermal_capacity = calculate_thermal_capacity(fluid_data, indices)

# Output result as required
print(f"Result: {thermal_capacity}")