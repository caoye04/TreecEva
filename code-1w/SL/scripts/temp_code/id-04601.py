import itertools

# Simulated agricultural plot data with yield metrics
soil_quality = {'A': 3.2, 'B': 2.8, 'C': 3.5, 'D': 2.1}
treatment_effects = [1.1, 0.95, 1.2, 0.8]
irrigation_levels = {1: 'low', 2: 'medium', 3: 'high'}

# Irrelevant meteorological decoy data
weather_forecast = [
    {'temp': 22, 'humidity': 60, 'pressure': 1013},
    {'temp': 25, 'humidity': 55, 'pressure': 1010},
    {'temp': 19, 'humidity': 70, 'pressure': 1015}
]

total_rainfall = sum([forecast['humidity'] * 0.1 for forecast in weather_forecast])  # Distraction

# Decoy function – looks important but unused in critical path
def calculate_ideal_temperature(altitude):
    return 25 - (altitude / 100) * 0.6

# Unused transformation path (dead code)
transformed_effects = []
for effect in treatment_effects:
    if effect > 1.0:
        transformed_effects.append(effect ** 0.5)
    else:
        transformed_effects.append(effect)

# Real processing begins here
plot_ids = ['A', 'B', 'C', 'D']
base_yields = [soil_quality[p] * 100 for p in plot_ids]

# Apply actual treatment effect based on index mapping (relevant)
effective_yields = []
for i, yield_val in enumerate(base_yields):
    adjusted = yield_val * treatment_effects[i % len(treatment_effects)]
    effective_yields.append(adjusted)

# Filtering high-quality plots using set logic (relevant)
preferred_soils = {'A', 'C'}
selected_plots = {p for p in plot_ids if p in preferred_soils}
processed_plots = [effective_yields[i] for i, p in enumerate(plot_ids) if p in selected_plots]

# Red herring: complex-looking grouping that isn't used
grouped_data = list(itertools.groupby(sorted(effective_yields), key=lambda x: x // 50))
decoy_aggregation = {k: list(g) for k, g in grouped_data}  # Dead end

# Efficiency factor computed via list comprehension with filtering (relevant)
efficiency_scores = [max(0, y - 200) for y in processed_plots if y > 220]
efficiency_factor = sum(efficiency_scores) / len(processed_plots) if processed_plots else 0

# Core optimization function with misleading complexity
def optimize_harvest(yields, factor):
    if not yields:
        return 0
    
    # Multi-step transformation chain
    boosted = [y * (1 + factor / 300) for y in yields]
    capped = [min(b, 350) for b in boosted]
    
    # Bit manipulation twist: use parity to adjust final boost
    total_int = int(sum(capped))
    if (total_int & 1) == 1:  # XOR-like logic check
        total_int ^= 1  # Neutralize oddness
    
    # Conditional scaling based on logical combination
    is_high_potential = all(y > 250 for y in yields) or factor > 15
    multiplier = 1.1 if is_high_potential else 1.0
    
    # Final aggregation
    raw_total = sum(capped)
    final_value = raw_total * multiplier
    
    # Decoy side computation (never used)
    shadow_buffer = [final_value / (i+1) for i in range(3)]
    shadow_buffer.reverse()
    
    return final_value

# Critical execution point
final_yield = optimize_harvest(processed_plots, efficiency_factor)

# Output result as required
print(f"Target result: {final_yield}")