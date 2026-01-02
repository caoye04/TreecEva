from collections import defaultdict
from itertools import combinations

# Simulate crop yield data across zones and seasons
zones = ['north', 'south', 'east', 'west']
seasons = ['spring', 'summer', 'autumn']
temperature_bias = {'north': -0.3, 'south': 0.4, 'east': 0.1, 'west': -0.2}
moisture_levels = [0.65, 0.78, 0.91, 0.72]

# Base yields per zone (tonnes per hectare)
base_yields = defaultdict(float, {
    'north': 4.2,
    'south': 5.1,
    'east': 4.8,
    'west': 4.5
})

# Initialize tracking variables
harvest_data = []
running_totals = {zone: 0 for zone in zones}
seasonal_adjustments = []
phantom_counter = 0  # Distractor: used in dead logic

# Simulate growth cycles with environmental factors
for season in seasons:
    cycle_yield = 0
    adjustment_factor = 0

    for i, zone in enumerate(zones):
        temp_effect = temperature_bias[zone]
        moisture_effect = moisture_levels[i] * 0.5

        # Primary yield calculation
        effective_yield = base_yields[zone] * (1 + temp_effect) * (moisture_effect + 0.6)

        # Record per-zone adjusted yield
        running_totals[zone] += effective_yield
        cycle_yield += effective_yield

        # Distractor computation: irrelevant to final result
        phantom_counter += int(effective_yield % 2.3 * 10)

    # Store seasonal aggregate
    harvest_data.append(cycle_yield)
    seasonal_adjustments.append(cycle_yield * 0.05)  # Minor correction factor (unused)

# Generate all possible two-zone partnerships for resource pooling (distractor)
partnerships = list(combinations(zones, 2))
partnership_gains = []
for p in partnerships:
    gain = (running_totals[p[0]] + running_totals[p[1]]) * 0.02
    partnership_gains.append(round(gain, 3))

# Real processing: compute weighted efficiency across cycles
weight_map = [0.3, 0.5, 0.2]  # weights for spring, summer, autumn
weighted_efficiency = sum(harvest_data[i] * weight_map[i] for i in range(3))

# Secondary transformation: apply logarithmic scaling for sustainability index
import math
sustainability_score = sum(math.log(running_totals[zone] + 1) for zone in zones)

# Final output variable - key result
final_yield = round(weighted_efficiency, 4)

# Print target result
print(f"Result: {final_yield}")