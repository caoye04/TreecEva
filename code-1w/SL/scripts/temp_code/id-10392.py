from itertools import compress

# Agricultural yield simulation with noise filtering
base_rates = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7, 1.3]
weather_factors = [0.95, 1.05, 0.88, 1.15, 0.99, 0.82, 1.11]
soil_quality = [7, 6, 8, 5, 9, 4, 7]
days_to_harvest = [85, 92, 87, 94, 88, 83, 90]

# Simulate raw yield per plot (in tons)
raw_yields = [b * w * 10 for b, w in zip(base_rates, weather_factors)]

# Noise threshold based on soil quality median
median_soil = sorted(soil_quality)[len(soil_quality)//2]
valid_plots = [q >= median_soil for q in soil_quality]

# Filtered yields using only high-soil-quality plots
filtered_yields = list(compress(raw_yields, valid_plots))

# Misleading calculation: average of all raw yields (not used in final result)
avg_raw_yield = sum(raw_yields) / len(raw_yields)
adjusted_avg = avg_raw_yield * 0.97  # arbitrary adjustment

# Secondary filter: exclude yields below local average
local_avg = sum(filtered_yields) / len(filtered_yields)
strong_yield_mask = [y >= local_avg for y in filtered_yields]
strong_yields = list(compress(filtered_yields, strong_yield_mask))

# Red herring: simulate hypothetical early harvest loss
early_harvest_loss = 0
for i, days in enumerate(days_to_harvest):
    if days < 88:
        early_harvest_loss += raw_yields[i] * 0.05

# Final determination of maximum yield among filtered and strong plots
final_yield = max(filtered_yields)

# Distractor: unused lambda function for scalability analysis
project_next_year = lambda y: y * 1.03 + 0.05
next_projections = [project_next_year(y) for y in strong_yields]

print(f"Result: {final_yield}")