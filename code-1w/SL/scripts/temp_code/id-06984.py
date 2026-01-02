def calculate_thermal_output(temps, eff_map):
    total_energy = 0
    peak_margins = []
    baseline_offset = 273.15
    adjusted_temps = [t + baseline_offset for t in temps]
    
    # Misleading computation: pressure simulation (not used)
    pressure_readings = [t * 0.086 for t in adjusted_temps]
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    normalized_pressure = [p / (avg_pressure + 1e-9) for p in pressure_readings]

    # Real logic starts: efficiency-weighted energy accumulation
    temp_categories = {'high': 0, 'medium': 0, 'low': 0}
    for idx, temp in enumerate(adjusted_temps):
        if temp > 373.15:
            temp_categories['high'] += 1
        elif temp > 323.15:
            temp_categories['medium'] += 1
        else:
            temp_categories['low'] += 1

    # Distractor: unused category analysis
    dominant_category = max(temp_categories, key=temp_categories.get)
    category_entropy = 0
    for count in temp_categories.values():
        if count > 0:
            prob = count / len(adjusted_temps)
            category_entropy -= prob * __import__('math').log(prob)

    # Core calculation with zip and conditional logic
    energy_contributions = []
    for temp, (zone, eff) in zip(adjusted_temps, zip(['A','B','C','D','E'], eff_map)):
        raw_contribution = temp * eff
        # Only zones B and D contribute to final output
        adjustment_factor = 1.1 if zone in ['B', 'D'] else 0.0  # deliberate zeroing
        energy_contributions.append(raw_contribution * adjustment_factor)
    
    total_energy = sum(energy_contributions)
    
    # Final capacity computed using set-based uniqueness bonus
    unique_efficiencies = len(set(eff_map))
    efficiency_bonus = 1 + (unique_efficiencies / 10.0)
    thermal_capacity = total_energy * efficiency_bonus
    
    # Dead code: safety margin simulation (not connected)
    safety_thresholds = {t: t * 1.2 for t in adjusted_temps}
    compliance_check = all(t <= safety_thresholds[t] for t in adjusted_temps)
    
    return int(thermal_capacity)

# Input data
grid_temperatures = [45, 67, 33, 89, 54]
efficiency_map = [0.78, 0.82, 0.65, 0.88, 0.71]

# Key execution point
thermal_capacity = calculate_thermal_output(grid_temperatures, efficiency_map)

print(f"Result: {thermal_capacity}")