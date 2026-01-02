def analyze_growth_pattern(base_rate, days):
    if days < 10:
        return base_rate * 0.8
    elif days < 25:
        return base_rate * (1 + 0.03 * days)
    else:
        return base_rate * (1.5 - 0.01 * days)


def assess_soil_nutrition(levels):
    score = 0
    for val in levels:
        if val > 0.7:
            score += 1.2
        elif val > 0.4:
            score += 0.5
        else:
            score -= 0.3
    return score

# Simulate multi-phase crop development
base_area = 120
expansion_ratio = 1.15
phases = [7, 14, 8]
total_days = sum(phases)

# Environmental stress factors (temperature, moisture, pests)
stress_factors = {
    'temp_deviation': 2.3,
    'moisture_stress': 0.85,
    'pest_pressure': 1.4
}

# Area configuration across zones
area_config = [
    {'zone': 'A', 'size': base_area * 0.4, 'soil': [0.85, 0.62, 0.71]},
    {'zone': 'B', 'size': base_area * 0.35, 'soil': [0.52, 0.48, 0.91]},
    {'zone': 'C', 'size': base_area * 0.25, 'soil': [0.31, 0.39, 0.67]}
]

# Preliminary metrics (distractor computations)
avg_size = sum(zone['size'] for zone in area_config) / len(area_config)
disruption_index = stress_factors['temp_deviation'] * stress_factors['pest_pressure']
baseline_growth = analyze_growth_pattern(1.0, total_days)

# Assess each zone's contribution
zone_outputs = []
for zone in area_config:
    base_yield = zone['size'] * 0.9
    soil_score = assess_soil_nutrition(zone['soil'])
    adjusted_yield = base_yield * (1 + soil_score / 10)
    
    # Apply phase-based growth modulation
    growth_multiplier = 1.0
    for i, phase in enumerate(phases):
        if i == 1:  # Only middle phase significantly affects yield
            growth_multiplier *= analyze_growth_pattern(1.0, phase) / phase
    
    final_zone_yield = adjusted_yield * growth_multiplier
    zone_outputs.append(final_zone_yield)

# Compute overall efficiency with conditional weighting
moisture_factor = stress_factors['moisture_stress']
yield_weights = [
    0.5 if moisture_factor > 0.9 else 0.3,
    0.3 if moisture_factor > 0.9 else 0.4,
    0.2 if moisture_factor > 0.9 else 0.3
]

weighted_total = sum(y * w for y, w in zip(zone_outputs, yield_weights))

# Final efficiency calculation
reference_output = base_area * 0.85
harvest_efficiency = weighted_total / reference_output if reference_output != 0 else 0

# Secondary distraction: simulate equipment degradation
equipment_cycles = 0
for day in range(total_days):
    if day % 4 == 0:
        equipment_cycles += 1
maintenance_factor = 1 - (equipment_cycles * 0.012)

# Core result computation (depends only on harvest_efficiency and fixed scaling)
final_yield = int(harvest_efficiency * 1000)  # Scale for integer reporting

print(f"Result: {final_yield}")