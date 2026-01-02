def calculate_base_growth(temperature, moisture):
    # Complex but partially irrelevant growth model
    base_growth = (temperature * 0.8 + moisture * 1.2) / 2.0
    adjustment = (temperature - 25) ** 2 * -0.01  # Peaks at 25C
    return max(base_growth + adjustment, 0)

# Simulate multi-season crop behavior across zones
temperature_data = [22, 26, 28, 24, 30]
moisture_data = [60, 55, 70, 50, 65]
zones = ['north', 'east', 'south', 'west', 'central']

zone_set = set(zones)
complement_zones = {'upland', 'lowland', 'foothill'}
overlap_check = zone_set & complement_zones  # Irrelevant intersection

growth_rates = []
for i in range(len(temperature_data)):
    rate = calculate_base_growth(temperature_data[i], moisture_data[i])
    if temperature_data[i] > 27:
        rate *= 0.9  # Heat stress
    growth_rates.append(rate)

# Field capacity modeled as average growth potential
temp_sum = sum(temperature_data)
major_threshold = temp_sum / 5
minor_offset = sum([t**2 for t in temperature_data if t > major_threshold]) * 0.001  # Distractor calc

field_capacity = sum(growth_rates) / len(growth_rates)

# Stress factors from external conditions
soil_quality = [0.9, 0.7, 0.85, 0.6, 0.75]
pest_pressure = [0.1, 0.3, 0.2, 0.4, 0.25]
stress_factors = []
for sq, pp in zip(soil_quality, pest_pressure):
    combined_stress = 1.0 - (sq * 0.7 + (1 - pp) * 0.3)
    stress_factors.append(combined_stress)

# Secondary unused stress modeling (dead path)
if len(stress_factors) > 4:
    buffer_factor = 0.95
    # This block runs but doesn't contribute to final result

# Core efficiency calculation with set-based validation
valid_indices = {i for i, sf in enumerate(stress_factors) if sf < 0.3}
correction_set = {0, 2, 4}
adjusted_indices = valid_indices | correction_set  # Union for robustness

partial_yield = 0
for i in adjusted_indices:
    if i < len(growth_rates):
        partial_yield += growth_rates[i] * (1 - stress_factors[i])

normalizer = len(adjusted_indices) or 1
baseline_efficiency = partial_yield / normalizer

# Final computation
final_yield = calculate_harvest_efficiency(field_capacity, stress_factors)

# Helper function defined after use (syntactically valid due to def ordering)
def calculate_harvest_efficiency(capacity, stresses):
    base_eff = capacity * 0.5
    stress_penalty = sum(stresses) * 0.2
    efficiency = base_eff - stress_penalty
    return max(efficiency, 0.1)  # Minimum baseline

# Print result for extraction
print(f"Result: {final_yield}")