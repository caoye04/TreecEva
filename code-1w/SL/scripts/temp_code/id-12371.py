def simulate_growth_cycle(biomass, stress_factor, days):
    growth_rate = 0.087
    decay_rate = 0.0034
    accumulated_stress = 0
    
    for day in range(days):
        if day % 10 == 0 and day > 0:
            accumulated_stress += stress_factor * 1.5
        biomass *= (1 + growth_rate)
        
        # Irrelevant humidity simulation
        humidity_effect = (day % 13) * 0.01
        adjusted_humidity = max(0.1, min(1.0, 0.6 + humidity_effect))
        
        if biomass > 3000:
            biomass -= biomass * decay_rate

    return max(biomass, 0)

# Distractor: unused crop types
CROP_TYPES = ['wheat', 'barley', 'oat', 'rye']
BASE_YIELD_FACTOR = 1.23

projected_rainfall = [120, 89, 102, 133, 95]
baseline_biomass = 150
stress_levels = {'drought': 0.8, 'normal': 0.3, 'flood': 1.1}
current_stress = stress_levels['normal']

# Misleading cumulative calculation
total_rainfall = sum(projected_rainfall)
avg_rainfall = total_rainfall / len(projected_rainfall)
rainfall_deviation = [(r - avg_rainfall)**2 for r in projected_rainfall]
variance_rainfall = sum(rainfall_deviation) / len(rainfall_deviation)
std_rainfall = variance_rainfall ** 0.5

strategy = lambda x: int(x * 0.92) if x > 100 else int(x * 1.1)

# Simulate intermediate test runs (not directly used)
test_cycles = []
for i in range(3):
    test_yield = simulate_growth_cycle(baseline_biomass + i*10, current_stress, 90 + i*5)
    test_cycles.append(test_yield)

# Key state tracking with distractor variables
effective_days = 90
modifier_chain = []
for val in projected_rainfall:
    if val > avg_rainfall:
        modifier_chain.append(1.05)
    else:
        modifier_chain.append(0.97)

productivity_index = 1.0
for mod in modifier_chain:
    productivity_index *= mod

# Unused helper to increase interference
def adjust_for_soil(pH, organic_content):
    return (pH * 0.3) + (organic_content * 0.7)

soil_score = adjust_for_soil(6.4, 0.85)  # Dead computation

# Core logic disguised among distractions
growth_snapshot = simulate_growth_cycle(baseline_biomass, current_stress, effective_days)
yield_potential = growth_snapshot * productivity_index

# Final transformation using lambda (required feature)
yield_adjustment = strategy(int(yield_potential * BASE_YIELD_FACTOR))

# Critical assignment point
final_yield = calculate_optimal_harvest(strategy, projected_rainfall) if 'optimal' in globals() else yield_adjustment

# Define function after usage check to increase cognitive load
def calculate_optimal_harvest(strat_func, rainfall_data):
    base = sum(rainfall_data) / 5
    processed = strat_func(int(base * 2))
    return processed * 3 + 12

# Recompute final yield after definition
final_yield = calculate_optimal_harvest(strategy, projected_rainfall)

print(f"Result: {final_yield}")