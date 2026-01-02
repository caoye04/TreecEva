def analyze_growth_potential(temp, rain):
    # Auxiliary calculation with limited impact
    base_score = (temp - 15) * 2.1
    bonus = 10 if rain > 80 else 5 if rain > 50 else 0
    return base_score + bonus

# Irrelevant helper for distraction
compute_stress_factor = lambda x, y: (x + y) % 7

soil_conditions = [62, 77, 85, 44, 91]
climate_data = [(22, 65), (25, 90), (19, 40), (24, 70), (27, 95)]

harvest_map = {}
buffer_values = []
threshold_met = False
running_total = 0

for i, (temp, rainfall) in enumerate(climate_data):
    # Distractor computation - not used in final result
    stress_level = compute_stress_factor(temp, rainfall)
    buffer_values.append(stress_level)

    growth_score = analyze_growth_potential(temp, rainfall)

    if growth_score > 30:
        threshold_met = True

    adjusted_rain = rainfall * 1.1 if temp < 24 else rainfall * 0.9
    efficiency = 0.8 if adjusted_rain < 60 or temp > 26 else 1.0

    yield_contribution = (temp * 3.5 + adjusted_rain * 0.4) * efficiency

    # Real data accumulation
    harvest_map[i] = round(yield_contribution, 3)

    # Running total that partially influences final step
    running_total += int(yield_contribution // 3)

# Semi-relevant transformation
intermediate_sum = sum(harvest_map[k] for k in range(0, len(harvest_map), 2))

# Key logic: filter soil zones and combine with mapped yields
valid_zones = [val for val in soil_conditions if val > 70]
scale_factor = len(valid_zones) / 4 if valid_zones else 0.5

# Final computation chain
aggregated_yield = 0
for key, value in harvest_map.items():
    if key % 2 == 0:
        aggregated_yield += value * 0.9
    else:
        aggregated_yield += value * 1.1

# Final adjustment using scale factor derived from soil
final_yield = round(aggregated_yield * scale_factor, 4)

# Print result as required
print(f"Target result: {final_yield}")