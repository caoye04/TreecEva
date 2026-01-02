from itertools import combinations

# Environmental and system parameters
temperature_zones = [22, 19, 25, 18, 24]
humidity_levels = [45, 60, 55, 50, 65]
pressure_readings = [1013, 1008, 1015, 1006, 1010]

# Initial device ratings
device_ratings = [88, 92, 85, 90, 87]
base_rating = sum(device_ratings) // len(device_ratings)

# Auxiliary calculations (some irrelevant)
avg_temp = sum(temperature_zones) / len(temperature_zones)
temp_variance = sum((t - avg_temp) ** 2 for t in temperature_zones) / len(temperature_zones)

# Irrelevant combinatorial analysis of pressure pairs
pressure_pairs = list(combinations(pressure_readings, 2))
high_pressure_count = sum(1 for p1, p2 in pressure_pairs if (p1 + p2) > 2020)

# Humidity mapping (semi-relevant but not used directly)
humidity_map = {zone: humidity for zone, humidity in enumerate(humidity_levels)}
dew_points = []
for h in humidity_levels:
    if h > 55:
        dew_points.append(h * 0.37)
    else:
        dew_points.append(h * 0.32)

# Efficiency factors based on conditional logic
efficiency_factor = 1.0
status_flags = []
for i, temp in enumerate(temperature_zones):
    adjusted_rating = device_ratings[i] * (temp / 20.0)
    if adjusted_rating > 90:
        efficiency_factor *= 1.05
    elif adjusted_rating < 80:
        efficiency_factor *= 0.92
    else:
        efficiency_factor *= 1.0
    # Flag tracking (not used later)
    status_flags.append(f"Zone{i}: {'Optimal' if adjusted_rating >= 85 else 'Suboptimal'}")

# Critical calculation point
efficiency_factor = round(efficiency_factor, 4)
thermal_capacity = base_rating * efficiency_factor

# Redundant data restructuring
zipped_data = list(zip(temperature_zones, device_ratings, humidity_levels))
processed_entries = []
for idx, (t, r, h) in enumerate(zipped_data):
    processed_entries.append({
        'index': idx,
        'rating_norm': r / base_rating,
        'risk_score': (t - 20) * (h / 100)
    })

# Dead code branch (never executed)
if False:
    fallback_value = sum(pressure_readings) / sum(humidity_levels)
    thermal_capacity -= fallback_value

print(f"Result: {thermal_capacity}")