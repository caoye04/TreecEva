import itertools

# Simulate agricultural yield modeling with multiple irrelevant computations
def analyze_soil_composition(elements):
    # Irrelevant function - dead code path
    return sum([e['count'] * e['weight'] for e in elements])


def generate_growth_phases(cycles):
    # Distractor: generates phase data but not used in final calculation
    phases = []
    for i in range(cycles):
        phase = {
            'id': i,
            'stage': 'growth' if i % 2 == 0 else 'dormant',
            'temp_shift': (i * 0.7) % 5,
            'moisture': (i + 30) ** 0.5
        }
        phases.append(phase)
    return phases

# Misleading intermediate variables
total_biomass = 0
climate_factor = 0.87
baseline_rainfall = 42.5

# Key input data
area_metrics = [
    {'zone': 'A', 'hectares': 12, 'fertility': 0.85, 'elevation': 150},
    {'zone': 'B', 'hectares': 8,  'fertility': 0.92, 'elevation': 120},
    {'zone': 'C', 'hectares': 15, 'fertility': 0.78, 'elevation': 180}
]

growth_cycles = 6

# Unused transformation - red herring
effective_zones = list(filter(lambda x: x['fertility'] > 0.8, area_metrics))
expanded_grid = list(itertools.product(['N', 'S', 'E', 'W'], [z['zone'] for z in area_metrics]))

def calculate_nutrient_depletion(zone_list, cycles):
    # Another decoy function that computes plausible but unused values
    depletion_rates = {}
    for zone in zone_list:
        key = zone['zone']
        base_rate = (zone['hectares'] * 0.03) / (zone['fertility'] + 0.1)
        depletion_rates[key] = round(base_rate * (1.05 ** cycles), 4)
    return depletion_rates

# Real computation begins here - heavily buried
initial_estimates = []
for metric in area_metrics:
    adjusted_hectares = metric['hectares'] * metric['fertility']
    normalized_elev = (metric['elevation'] - 100) / 100
    efficiency_modifier = max(0.5, 1 - normalized_elev * 0.1)
    initial_estimates.append({'zone': metric['zone'], 'adjusted': adjusted_hectares, 'modifier': efficiency_modifier})

# Aggregation using dictionary operations
aggregate_map = {item['zone']: item['adjusted'] * item['modifier'] for item in initial_estimates}

# Use of set operations to filter valid zones (some may be excluded)
valid_zone_keys = set(aggregate_map.keys()) - {'D'}  # 'D' doesn't exist, still included as distraction

# Core logic hidden among distractors
base_yield_per_hectare = 2.4
total_weighted_area = sum(aggregate_map[k] for k in valid_zone_keys)

cycle_multiplier = 1
for i in range(2, growth_cycles + 1):  # starts at 2
    cycle_multiplier *= (1 + 0.15 / i)  # diminishing returns

# Secondary adjustment using tuple unpacking
modifiers = (0.95, 1.05, 0.98)
*_, last_mod = modifiers  # unpacking irrelevant components

# Final efficiency calculation
def calculate_harvest_efficiency(metrics, cycles):
    total_base = sum(m['hectares'] for m in metrics)
    fertility_avg = sum(m['fertility'] for m in metrics) / len(metrics)
    
    # Complex interaction of factors
    raw_efficiency = total_weighted_area * base_yield_per_hectare * cycle_multiplier
    penalty_factor = (fertility_avg < 0.85) * 0.9 + (fertility_avg >= 0.85) * 1.0
    adjusted_efficiency = raw_efficiency * penalty_factor * last_mod
    
    # Final cap based on environmental constraints (simulated)
    environmental_cap = 1000 * (1 + (len(expanded_grid) % 10) * 0.01)  # slight boost from irrelevant expanded_grid
    return min(adjusted_efficiency, environmental_cap)

# Execution point of interest
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Print result as required
print(f"Target result: {final_yield}")