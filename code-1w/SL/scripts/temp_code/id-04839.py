import itertools

# Simulate agricultural yield optimization with environmental constraints
soil_quality = [0.85, 0.72, 0.91, 0.64, 0.79]
weather_factors = [1.05, 0.94, 1.02, 0.89, 0.97]
base_productivity = 120
temperature_shifts = [0.3, -0.1, 0.2, 0.0, -0.2]
elevation_zones = [1200, 1350, 1100, 1420, 1280]

# Irrelevant meteorological data (distractor)
wind_speeds_kph = [12.3, 15.1, 9.8, 18.4, 11.2]
humidity_levels = [45, 52, 39, 58, 43]
pressure_mb = [1013, 1009, 1015, 1007, 1011]

# Decoy function - never called (dead code path)
def calculate_wind_pressure_index(wind, pressure):
    return sum(w * p / 1000 for w, p in zip(wind, pressure))

# Unused transformation pipeline (red herring)
transformed_humidity = []
for h in humidity_levels:
    if h > 50:
        transformed_humidity.append(h * 1.1)
    else:
        transformed_humidity.append(h * 0.95)

# Real processing begins here
adjusted_yields = []
for i, (soil, weather) in enumerate(zip(soil_quality, weather_factors)):
    # Core productivity adjustment
    effective_yield = base_productivity * soil * weather
    
    # Elevation correction factor (only used in final step)
    elevation_factor = 1 + (elevation_zones[i] - 1250) * 0.0002
    effective_yield *= elevation_factor
    
    # Temperature adjustment using shift values
    temp_effect = 1 + temperature_shifts[i] * 0.05
    effective_yield *= temp_effect
    
    adjusted_yields.append(effective_yield)

# Secondary processing: filter and transform
viable_plots = []
for j, yield_val in enumerate(adjusted_yields):
    if yield_val >= 110:  # Threshold filter
        viability_score = yield_val * (1 + soil_quality[j] * 0.1)
        viable_plots.append(viability_score)

# Complex aggregation using itertools (core concept)
cumulative_growth = list(itertools.accumulate(viable_plots, lambda x, y: x * 0.9 + y))

# Set operations to identify stable performers (meaningful distractor but not final)
stabilized_set_a = set(range(len(cumulative_growth)))
stabilized_set_b = set([i for i, val in enumerate(cumulative_growth) if val > 150])
overlap_regions = stabilized_set_a.intersection(stabilized_set_b)
region_count = len(overlap_regions)

# Redundant bit manipulation on index (irrelevant computation)
bit_encoded = 0
for idx in overlap_regions:
    bit_encoded ^= (idx << 2) | (idx >> 1)

# Final transformation chain
processed_data = []
scaling_factors = [1.03, 0.98, 1.01, 0.99]

for k, val in enumerate(cumulative_growth):
    # Apply rotating scaling factor
    scaled = val * scaling_factors[k % len(scaling_factors)]
    processed_data.append(scaled)

# Another decoy structure (unused)
agricultural_matrix = [[0 for _ in range(5)] for _ in range(5)]
for row in range(5):
    for col in range(5):
        agricultural_matrix[row][col] = soil_quality[col] * weather_factors[row]

# Critical statement: harvest final result from processed data
def harvest_results(data_list):
    if not data_list:
        return 0.0
    # Weighted sum with position bias
    weights = [0.4, 0.3, 0.2, 0.1]
    weighted_sum = sum(val * weights[i] for i, val in enumerate(data_list[:4]))
    return round(weighted_sum, 4)

# Final assignment - key execution point
final_yield = harvest_results(processed_data)

# Print result as required
print(f"Target result: {final_yield}")