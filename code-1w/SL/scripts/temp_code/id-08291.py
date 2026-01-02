def analyze_growth_pattern(temperature_log, moisture_levels):
    peak_stress = 0
    cumulative_moisture = 0
    temp_alerts = []
    
    for i in range(len(temperature_log)):
        if temperature_log[i] > 35:
            peak_stress += 1
            temp_alerts.append(f'HighTemp_{i}')
        cumulative_moisture += moisture_levels[i]

    avg_moisture = cumulative_moisture / len(moisture_levels)
    return peak_stress, avg_moisture, temp_alerts


def normalize_sequence(raw_data):
    min_val = min(raw_data)
    max_val = max(raw_data)
    range_val = max_val - min_val or 1
    return [(x - min_val) / range_val for x in raw_data]

# Simulate environmental sensor data over 7 days
temperature_readings = [28, 36, 38, 32, 40, 34, 29]
soil_moisture = [0.6, 0.4, 0.35, 0.5, 0.2, 0.45, 0.65]
light_exposure = [8.2, 9.1, 7.8, 8.5, 6.9, 8.0, 9.3]

# Process primary growth indicators
stress_count, mean_moisture, warnings = analyze_growth_pattern(temperature_readings, soil_moisture)

# Irrelevant transformation (distractor)
moisture_flags = ["OK" if m > 0.4 else "LOW" for m in soil_moisture]
moisture_flags_str = ",".join(moisture_flags).upper()

# Normalize light data (semi-relevant)
normalized_light = normalize_sequence(light_exposure)
adjusted_light_yield = sum([x ** 1.1 for x in normalized_light])

# Core calculation setup
base_output = 1000 * (1 - stress_count * 0.1)
efficiency_factor = 0

if mean_moisture > 0.45:
    efficiency_factor = 1.2
elif mean_moisture > 0.3:
    efficiency_factor = 0.9
else:
    efficiency_factor = 0.6

# Simulate nutrient depletion based on heat exposure (distraction)
heat_days = [t for t in temperature_readings if t > 35]
depletion_rate = 0
for day in heat_days:
    depletion_rate += (day - 35) * 0.05

projected_loss = base_output * depletion_rate
theoretical_max = base_output * efficiency_factor

# Actual yield model incorporating multiple factors
stress_factors = [max(0, t - 35) * 0.02 for t in temperature_readings]
stress_factors.append((0.4 - mean_moisture) * 10 if mean_moisture < 0.4 else 0)

# Key function combining arithmetic, logic, and modular adjustment
def calculate_harvest_efficiency(output, stresses):
    base_eff = output
    total_stress_impact = sum(stresses)
    
    # Apply diminishing returns with modulo pattern
    for i in range(len(stresses)):
        if i % 2 == 0:
            base_eff *= (1 - stresses[i] * 0.8)
        else:
            base_eff *= (1 - stresses[i] * 0.6)
    
    # Final adjustment using case-insensitive string logic (red herring)
    control_mode = "AutoOverride".lower()
    if "auto" in control_mode:
        base_eff *= 0.95  # System calibration factor
    
    # Apply modular cap to simulate equipment limits
    capped_yield = base_eff % 800
    if capped_yield < 500:
        capped_yield = 500 + (capped_yield % 100)
        
    return int(capped_yield)

final_yield = calculate_harvest_efficiency(base_output, stress_factors)
print(f"Result: {final_yield}")