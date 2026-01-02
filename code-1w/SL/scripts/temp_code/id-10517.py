from itertools import compress

# Simulate sensor data from a chemical reactor
temperature_data = [298, 305, 310, 295, 315, 320, 300]
pressure_data = [1.0, 1.2, 1.4, 0.9, 1.6, 1.8, 1.1]

# Irrelevant auxiliary data (distractor)
humidity_data = [45, 47, 50, 44, 52, 55, 46]
elevation_data = [120, 125, 130, 115, 135, 140, 122]

# Misleading intermediate calculations (distractor)
avg_humidity = sum(humidity_data) / len(humidity_data)
corrected_elevation = list(map(lambda x: x * 1.01, elevation_data))

# Threshold filters based on safety limits (semi-relevant)
safe_temp_mask = [300 <= t <= 315 for t in temperature_data]
stable_pressure_mask = [1.0 <= p <= 1.5 for p in pressure_data]

# Combined operational window
valid_conditions = [t and p for t, p in zip(safe_temp_mask, stable_pressure_mask)]

# Extract valid readings
filtered_temps = list(compress(temperature_data, valid_conditions))
filtered_pressures = list(compress(pressure_data, valid_conditions))

# Red herring function that computes unrelated metric
def compute_humidity_index(data):
    return sum(x ** 0.5 for x in data if x > 45)

# Auxiliary calculation not used in final result (dead code path)
humidity_index = compute_humidity_index(humidity_data)

# Core logic: yield model based on quadratic response surface
def reaction_yield(temp, pressure):
    base = temp * 0.1
    bonus = pressure ** 2 * 5
    penalty = abs(temp - 305) * 0.2  # Optimal at 305K
    return base + bonus - penalty

# Calculate individual yields only for valid conditions
individual_yields = [
    reaction_yield(t, p) 
    for t, p in zip(filtered_temps, filtered_pressures)
]

# Secondary filter: ignore low-yield runs (additional logic step)
effective_yields = [y for y in individual_yields if y >= 40.0]

# Final aggregation with adjustment factor
adjustment_factor = 0.95 if len(effective_yields) > 2 else 1.0
raw_sum = sum(effective_yields)
final_yield = raw_sum * adjustment_factor

# Output result as required
print(f"Target result: {final_yield}")