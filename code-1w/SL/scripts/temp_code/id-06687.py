from itertools import compress, cycle

# Simulate environmental sensor readings over a 7-day agricultural cycle
temperature_readings = [22, 25, 28, 26, 30, 27, 24]
humidity_readings = [60, 65, 70, 55, 80, 75, 68]
sunlight_hours = [6.5, 7.2, 8.0, 6.0, 8.5, 7.0, 6.8]
pest_incidents = [0, 1, 0, 0, 2, 1, 0]

# Derived metrics (some are distractions)
degree_days = [temp - 18 for temp in temperature_readings]  # base threshold for crop growth
humidity_stress = [1 if h > 75 else 0 for h in humidity_readings]

# Mask days with excessive humidity or pest outbreaks
valid_growth_days = [humidity_stress[i] == 0 and pest_incidents[i] < 2 for i in range(7)]

# Apply filter to get usable sunlight only on valid days
effective_sunlight = list(compress(sunlight_hours, valid_growth_days))

# Misleading calculation - not used in final result
temporal_variance = sum((t - sum(temperature_readings)/7)**2 for t in temperature_readings) / 7

# Crop response model: nonlinear efficiency curve based on temp and sun
def photosynthesis_efficiency(temp, sun):
    if temp < 20 or temp > 35:
        return 0.3
    base_eff = 0.8 + 0.2 * (sun / 8.0)
    penalty = abs(temp - 26) * 0.02
    return max(0.4, base_eff - penalty)

# Water availability modulation (distraction: complex but partially unused)
rainfall_pattern = cycle([0, 3, 1, 8, 0, 0, 12])  # weekly repeating mm rainfall
irrigation_supplement = [5 if r < 2 else 0 for r in rainfall_pattern]
water_availability_index = [min(1.0, (r + 5) / 10) for r in irrigation_supplement][:7]

# Main yield calculation chain
baseline_yield_per_day = [
    photosynthesis_efficiency(temperature_readings[i], sunlight_hours[i]) * 120
    for i in range(7)
]

# Pest impact adjustment (only applies on days with incident)
adjusted_yield = []
for i in range(7):
    yield_loss_factor = 0.1 * pest_incidents[i]
    adjusted_yield.append(baseline_yield_per_day[i] * (1 - yield_loss_factor))

# Soil nutrient decay simulation (distractor: calculated but not impactful)
nutrient_levels = [100]
for day in range(1, 7):
    decay = nutrient_levels[-1] * 0.03
    nutrient_levels.append(nutrient_levels[-1] - decay + irrigation_supplement[day])

# Final harvest efficiency calculation incorporating filtered data
filtered_yield = list(compress(adjusted_yield, valid_growth_days))

def calculate_harvest_efficiency(yields, sunlight_list, degree_days):
    # Secondary filtering: only high-sunlight days contribute fully
    high_sun_mask = [s >= 7.0 for s in sunlight_list]
    partial_yields = list(compress(yields, high_sun_mask))
    
    # Core formula: weighted average using degree days as proxy
    total_weight = sum(abs(dd) for dd in degree_days)
    if total_weight == 0:
        return 0
    
    # Weighted contribution (note: uses original degree days, not filtered)
    weighted_sum = sum(
        adjusted_yield[i] * abs(degree_days[i]) / total_weight
        for i in range(len(adjusted_yield))
    )
    
    # Final nonlinear scaling based on consistency
    consistency_bonus = 1 + (len(partial_yields) / len(yields)) * 0.1
    return weighted_sum * consistency_bonus

# Critical execution point
final_yield = calculate_harvest_efficiency(adjusted_yield, effective_sunlight, degree_days)

# Distraction: secondary metric not related to final yield
economic_loss = sum(150 * p for p in pest_incidents)

# Output required variable
print(f"Result: {final_yield}")