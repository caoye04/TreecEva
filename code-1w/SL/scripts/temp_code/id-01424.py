def simulate_growth(biomass, nutrients, stress_factors):
    # Irrelevant simulation overhead
    temp_accum = 0
    for day in range(len(stress_factors)):
        if nutrients[day] > 50:
            biomass *= 1.05
        elif nutrients[day] > 20:
            biomass += 3.2
        else:
            biomass -= 1.1

        # Distractor: temperature effect that's never used
        temp_accum += (biomass % 7) * 0.3

        if stress_factors[day] > 80:
            biomass *= 0.85  # Stress reduces growth

    return int(biomass)


def calculate_water_footprint(cycles):
    # Dead code path — never called but looks important
    total = 0
    for c in cycles:
        total += sum([x * 0.7 for x in c if x > 30])
    return total * 1.5

# Misleading intermediate variables
total_biowaste = 0
aux_data = [0] * 5
metadata_log = set()

# Simulate nutrient depletion over time (unused in final result)
deplete_rate = 0.95
projected_loss = [100 * (deplete_rate ** i) for i in range(10)]

# Core data: actual production input
growth_cycles = [
    [45, 60, 70],
    [55, 65, 50],
    [40, 50, 60]
]

# Red herring function — appears related but unused
def assess_efficiency(data):
    efficiency_score = 0
    for row in data:
        if len(row) == 3:
            efficiency_score += sum(row) / 3
    return efficiency_score / len(data)

# Unused but plausible-looking transformation
normalized_cycles = [[val / max(sum(cycle), 1) for val in cycle] for cycle in growth_cycles]

# Real logic buried under noise
baseline_mass = 10.0
stress_profile = [75, 60, 85]
nutrient_input = [45, 52, 48]

# Key computation chain
processed_output = []
for cycle in growth_cycles:
    adjusted_biomass = baseline_mass + sum(cycle) / 10
    # Only this mutation affects the real result
    if sum(cycle) > 150:
        adjusted_biomass *= 1.2
    processed_output.append(int(adjusted_biomass))

# Another decoy: complex set operation with no impact
unique_values = set()
for out in processed_output:
    unique_values.add(out % 13)

# Actual answer derivation path
aggregated = 0
for i, val in enumerate(processed_output):
    if i % 2 == 0:
        aggregated += val * 2
    else:
        aggregated += val

# Final transformation hidden among distractions
def harvest_results(data):
    result = 0
    for x in data:
        if x > 25:
            result += x * 1.5
        else:
            result += x * 0.8
    # Apply correction factor from unrelated list comprehension
    factors = [i * 0.1 for i in range(5)]
    adjustment = sum(f for f in factors if f < 0.3)  # Always 0.3
    return int(result + adjustment)

# Critical assignment — this is what the question targets
final_yield = harvest_results(processed_output)

# Print required output
print(f"Result: {final_yield}")