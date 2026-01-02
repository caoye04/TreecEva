def analyze_soil_composition(elements):
    # Irrelevant computation: counts vowels in element names
    vowel_count = sum(1 for e in elements for v in 'aeiou' if v in e)
    return {e: len(e) % 3 for e in elements}

soil_elements = ['nitrogen', 'phosphorus', 'potassium', 'calcium']
element_profile = analyze_soil_composition(soil_elements)

# Simulate growth cycles over different zones
growth_cycles = []
for i in range(4):
    cycle_data = {}
    for j in range(i+1):
        zone_key = f'zone_{i}_{j}'
        # Real logic: productivity based on index sum
        productivity = (i + j) * 1.5
        cycle_data[zone_key] = productivity
    growth_cycles.append(cycle_data)

# Area metrics with realistic naming
area_metrics = {
    'plots': [
        {'size': 10, 'fertility': 3},
        {'size': 15, 'fertility': 2},
        {'size': 20, 'fertility': 4}
    ],
    'irrigation_efficiency': 0.87
}

# Distractor: unused function that looks relevant
def estimate_water_usage(area, cycles):
    total_zones = sum(len(cycle) for cycle in cycles)
    return total_zones * area * 0.6

# Real calculation begins
base_efficiency = 0
for plot in area_metrics['plots']:
    base_efficiency += plot['size'] * plot['fertility']

# Apply cycle amplification using list comprehension
amplification_factors = [
    sum(data.values()) for data in growth_cycles
]
total_amplification = sum(amplification_factors)

adjusted_efficiency = base_efficiency * (1 + total_amplification / 100)

# Secondary adjustment using string method on irrelevant data
status_text = "Harvest season forecast: Optimal"
days_optimal = len([c for c in status_text if c.isupper()])  # Only counts uppercase letters

# Final yield calculation — this is the key statement
final_yield = adjusted_efficiency + days_optimal * 2.5

Result: final_yield