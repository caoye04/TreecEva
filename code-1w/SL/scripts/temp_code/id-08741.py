def simulate_growth(biomass, nutrients, cycle):
    growth_rate = 0.3 if cycle % 2 == 0 else 0.15
    nutrient_factor = max(nutrients / (cycle + 1), 0.5)
    decay = biomass * 0.05
    bonus = 1.2 if cycle in [2, 4] else 1.0
    # Distractor computation - not directly used
    theoretical_max = 1000 * nutrient_factor * bonus
    biomass = biomass + (biomass * growth_rate * nutrient_factor * bonus) - decay
    return min(biomass, 900)


def calculate_stress_factors(cycles):
    stress = []
    for c in cycles:
        s = abs((c - 2) * (c - 5))  # peaks at extremes
        stress.append(s * 0.1)
    return stress

# Irrelevant helper function (dead code path)
def unused_utility(data):
    return [x ** 0.5 for x in data if x > 10]

# Main simulation setup
initial_biomass = 100
initial_nutrients = 80
production_cycles = list(range(6))

# Simulate environmental fluctuations (distractor)
environmental_data = ['wind', 'sun', 'rain', 'cloud', 'storm', 'clear']
weather_scores = {cond: len(cond) % 4 for cond in environmental_data}
adjusted_cycles = [c + weather_scores[environmental_data[c]] for c in production_cycles]

# Compute stress but only use length
stress_levels = calculate_stress_factors(production_cycles)
dynamic_modifier = sum([int(s * 2) for s in stress_levels]) / len(stress_levels)

# Core state tracking with distractors
history = []
current_nutrients = initial_nutrients
biomass = initial_biomass

for cycle in production_cycles:
    prev_biomass = biomass
    biomass = simulate_growth(biomass, current_nutrients, cycle)
    uptake = (biomass - prev_biomass) * 0.4
    current_nutrients -= uptake
    efficiency = (biomass / (cycle + 1)) * 0.1 if cycle > 0 else 0
    history.append({
        'cycle': cycle,
        'biomass': biomass,
        'efficiency': efficiency,
        'nutrients_left': current_nutrients
    })

# Secondary processing with list comprehension and set operations
biomass_values = [entry['biomass'] for entry in history]
unique_efficiencies = list(set([round(entry['efficiency'], 2) for entry in history]))
filtered_biomass = [b for b in biomass_values if b > 300]

# Aggregation with distractor variables
total_observed = sum(biomass_values)
avg_biomass = total_observed / len(biomass_values)
peak_biomass = max(biomass_values)
unused_ratio = peak_biomass / total_observed if total_observed > 0 else 0

# Final yield calculation - key statement
final_yield = int(avg_biomass // 10 * len(filtered_biomass))

# Additional irrelevant computations
shadow_calc = [x for x in range(len(unique_efficiencies))]
symbolic_sum = sum(ord(str(x)[0]) for x in shadow_calc)
metadata_checksum = len(environmental_data) * 17 % 13

Result: final_yield