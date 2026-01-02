from collections import defaultdict

# Simulate agricultural yield prediction based on environmental factors
soil_quality = [0.8, 0.6, 0.9, 0.4, 0.7]
water_levels = [120, 95, 140, 60, 100]
temperature_readings = [22, 25, 21, 26, 23]  # Irrelevant for final calculation
elevation_data = [150, 180, 130, 200, 160]  # Not used in main logic

# Distractor: mapping unrelated sensor ids
temperature_sensors = defaultdict(lambda: 'unassigned')
for i in range(len(temperature_readings)):
    temperature_sensors[f'sensor_{i}'] = temperature_readings[i]

# Helper function to normalize data
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Misleading preprocessing step (not used in final path)
normalized_temp = normalize(temperature_readings)
adjusted_elevation = [e * 0.01 for e in elevation_data if e > 140]

# Core logic with conditional expressions and relevant processing
normalized_soil = normalize(soil_quality)
normalized_water = normalize(water_levels)

# Weighted combination using conditional scaling
weighted_yield_components = []
for s, w in zip(normalized_soil, normalized_water):
    efficiency_factor = 1.2 if s > 0.5 else 0.8
    availability_modifier = 1.1 if w > 0.6 else 0.9
    # Composite calculation
    component = s * w * efficiency_factor * availability_modifier
    weighted_yield_components.append(component)

# Secondary adjustment based on pattern detection
streak_count = 0
current_streak = 0
for val in water_levels:
    if val > 80:
        current_streak += 1
    else:
        streak_count = max(streak_count, current_streak)
        current_streak = 0
streak_count = max(streak_count, current_streak)

# Final yield potential calculation
base_potential = sum(weighted_yield_components)
streak_bonus = 1.0 + (streak_count * 0.05) if streak_count >= 3 else 1.0

# Simulate minor data validation (has no effect but adds complexity)
valid_entries = [x for x in soil_quality if 0 <= x <= 1]
dropped_entries = len(soil_quality) - len(valid_entries)

# Key statement
final_yield = base_potential * streak_bonus

# Print result as required
print(f"Result: {final_yield}")