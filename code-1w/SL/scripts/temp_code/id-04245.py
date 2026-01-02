import itertools

# Agricultural yield simulation with environmental factors
soil_quality = {'nitrogen': 0.8, 'phosphorus': 0.6, 'potassium': 0.7}
weather_conditions = [0.9, 0.5, 0.8, 0.7, 0.6]  # Daily moisture index over 5 days

temperature_readings = [22, 25, 27, 23, 20, 26, 28]
valid_temperatures = [t for t in temperature_readings if 20 <= t <= 28]
avg_temp = sum(valid_temperatures) / len(valid_temperatures)

temp_effect = 1.0 if 22 <= avg_temp <= 26 else 0.85

# Simulate daily growth using weather data
accumulated_moisture = 0
for day in range(len(weather_conditions)):
    accumulated_moisture += weather_conditions[day]

moisture_avg = accumulated_moisture / len(weather_conditions)
moisture_effect = 0.9 + (moisture_avg - 0.6) * 0.5 if moisture_avg >= 0.6 else 0.7

# Base nutrient effect from soil
nutrient_score = (soil_quality['nitrogen'] + soil_quality['phosphorus'] + soil_quality['potassium']) / 3
if nutrient_score > 0.7:
    nutrient_effect = 1.1
elif nutrient_score > 0.5:
    nutrient_effect = 1.0
else:
    nutrient_effect = 0.8

# Phantom calculations - irrelevant to final yield but add cognitive load
phantom_data = list(itertools.combinations([1, 2, 3], 2))
dummy_sum = 0
for p in phantom_data:
    dummy_sum += p[0] * 2

# Unrelated string processing distraction
crop_name = "Wheat"
crop_code = ''.join([c.lower() for c in crop_name if c.isalpha()])
crop_code_hash = sum([ord(c) for c in crop_code]) % 100

# Actual production model
base_yield_per_hectare = 4500
hectares_farmed = 120
crop_production = base_yield_per_hectare * hectares_farmed

# Efficiency factor influenced by temp, moisture, and nutrients
efficiency_factor = temp_effect * moisture_effect * nutrient_effect

# Final calculation point
final_yield = crop_production * efficiency_factor

# Irrelevant dictionary operation distraction
diagnostic_log = {
    'readings': temperature_readings,
    'avg': round(avg_temp, 2),
    'flags': [t for t in temperature_readings if t > 27]
}
diagnostic_log['status'] = 'normal' if len(diagnostic_log['flags']) == 0 else 'caution'

# Semi-relevant but unused alternate model
potential_max_yield = base_yield_per_hectare * hectares_farmed * 1.2
theoretical_surplus = potential_max_yield - final_yield if final_yield < potential_max_yield else 0

# Output result
Result: {final_yield}