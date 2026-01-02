from itertools import compress, cycle

# Simulate a precision agriculture scenario with sensor array data filtering
soil_moisture = [0.3, 0.5, 0.8, 0.6, 0.4, 0.2, 0.9, 0.7]
temperature_zones = [22, 25, 27, 24, 23, 26, 28, 21]
pest_presence = [True, False, True, False, True, False, True, False]
base_yield_per_plot = 150

# Irrelevant transformation - distractor
temp_classes = ['warm' if t > 24 else 'normal' for t in temperature_zones]

# Misleading intermediate calculation
baseline_adjustment = sum(temperature_zones) / len(temperature_zones) - 20

# Distractor: unused helper function
def analyze_pest_pattern(pattern):
    return [i for i, x in enumerate(pattern) if x]

# Real processing begins
moisture_ok = [0.4 <= x <= 0.7 for x in soil_moisture]
heat_stressed = [t > 26 for t in temperature_zones]

# Combine conditions with masking
viable_plots = [m and not h for m, h in zip(moisture_ok, heat_stressed)]

# Apply pest filter using logical short-circuit mimicry
filtered_yield_mask = []
for i in range(len(viable_plots)):
    if not viable_plots[i]:
        filtered_yield_mask.append(False)
    else:
        # Logical AND simulation with explicit control flow
        if pest_presence[i]:
            filtered_yield_mask.append(False)
        else:
            filtered_yield_mask.append(True)

# Use itertools to align base yield with valid plots
yield_potential = list(compress([base_yield_per_plot] * 8, filtered_yield_mask))

# Secondary adjustment based on optimal moisture deviation
moisture_score = [round(1 - abs(m - 0.55), 2) for m in soil_moisture]
optimal_boost = [score * 30 for score in moisture_score]

# Boost only applicable to plots that passed all filters
boost_vector = [optimal_boost[i] if filtered_yield_mask[i] else 0 for i in range(8)]
adjusted_boost = sum(boost_vector)  # This matters

# Distractor variables
average_boost = adjusted_boost / 8 if len(yield_potential) else 0
useless_aggregation = list(cycle([1, 0], ))[:8]  # Unused pattern

# Key state-tracking computation
plot_quality_tiers = []
for m, t in zip(moisture_score, temperature_zones):
    tier = 'A' if m >= 0.8 else 'B' if m >= 0.6 else 'C'
    plot_quality_tiers.append(tier)

# Final efficiency calculation - depends on count and boost
harvest_count = len(yield_potential)
efficiency_factor = 1 + (harvest_count / 8) * 0.25

# Critical statement
final_yield = int(base_yield_per_plot * harvest_count * efficiency_factor + adjusted_boost)

print(f"Result: {final_yield}")