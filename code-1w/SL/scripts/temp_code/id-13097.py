def analyze_soil_composition(elements):
    # Irrelevant computation on trace elements
    heavy_metals = ['pb', 'cd', 'hg']
    safe_levels = {e: 0.05 for e in heavy_metals}
    risk_score = sum([elements.get(e, 0) / safe_levels[e] for e in heavy_metals])
    return risk_score > 1.0

# Simulate agricultural yield prediction with noise
soil_data = {'n': 0.18, 'p': 0.09, 'k': 0.12, 'pb': 0.02, 'cd': 0.01}
area_metrics = [12.5, 8.3, 15.7, 6.2]
growth_factors = [0.88, 0.76, 0.94, 0.67]

# Distractor: unused crop rotation schedule
rotation_cycle = ['corn', 'wheat', 'soy', 'barley']
current_field_index = 3

# Misleading intermediate calculation (not used in final result)
temp_accumulator = 0
for i in range(len(area_metrics)):
    temp_accumulator += area_metrics[i] * (i + 1)

# Real processing begins here
adjusted_areas = list(map(lambda x: x * 1.08, area_metrics))  # Climate adjustment

# Apply growth modulation
modulated_yields = []
for i in range(len(adjusted_areas)):
    modulated_yields.append(adjusted_areas[i] * growth_factors[i])

# Filter out low-yield zones using string-based threshold labeling
yield_labels = []
for y in modulated_yields:
    if y < 8:
        yield_labels.append('low'.upper())
    elif y < 12:
        yield_labels.append('moderate'.upper())
    else:
        yield_labels.append('high'.upper())

low_yield_count = len([lbl for lbl in yield_labels if lbl == 'LOW'])

# Use set to deduplicate redundant high-yield regions (distractor)
unique_high_regions = set()
for i, lbl in enumerate(yield_labels):
    if lbl == 'HIGH':
        unique_high_regions.add(f"zone-{i % 4}")

# Core efficiency formula (depends only on modulated_yields and low_yield_count)
total_potential = sum(modulated_yields)
penalty_factor = 0.94 ** low_yield_count
base_efficiency = total_potential * penalty_factor

# Final transformation via helper function
def calculate_harvest_efficiency(areas, factors):
    adjusted = [a * 1.08 for a in areas]
    yields = [adjusted[i] * factors[i] for i in range(len(adjusted))]
    total = sum(yields)
    low_count = sum(1 for y in yields if y < 8)
    return round(total * (0.94 ** low_count), 4)

final_yield = calculate_harvest_efficiency(area_metrics, growth_factors)

# Print result as required
print(f"Result: {final_yield}")