from collections import defaultdict

# Simulate agricultural yield analysis with noise and intermediate calculations
soil_quality = {'loam': 0.8, 'clay': 0.5, 'sand': 0.3}
weather_conditions = {'rainfall': 120, 'temperature': 22.5, 'sunlight_hours': 7.2}

crop_data = defaultdict(lambda: defaultdict(float))
crop_data['wheat']['base_yield'] = 3.2
crop_data['wheat']['area'] = 150
crop_data['wheat']['soil_requirement'] = 'loam'
crop_data['corn']['base_yield'] = 2.8
crop_data['corn']['area'] = 200

efficiency_factor = 1.0
if weather_conditions['rainfall'] > 100:
    efficiency_factor *= 1.1
if weather_conditions['temperature'] > 20:
    efficiency_factor *= 1.05

# Irrelevant computation: simulate pest resistance (not used in final result)
pest_resistance_score = 0
for crop in ['wheat', 'corn']:
    if crop == 'wheat':
        pest_resistance_score += 0.7
    else:
        pest_resistance_score += 0.5

# Distractor: unused nutrient tracking
nutrient_levels = defaultdict(int)
nutrient_levels['nitrogen'] = 85
nutrient_levels['phosphorus'] = 45
nutrient_levels['potassium'] = 60

# Compute effective yield with soil adjustment
soil_match = soil_quality[crop_data['wheat']['soil_requirement']]
yield_adjustment = soil_match if soil_match > 0.6 else 0.8
intermediate_yield = crop_data['wheat']['base_yield'] * yield_adjustment

# Multiple assignment distraction
total_area, unused_buffer = crop_data['wheat']['area'], crop_data['corn']['area']

# Real calculation path
baseline_production = intermediate_yield * total_area
efficiency_factor = round(efficiency_factor, 3)  # Minor precision adjustment

# Key statement
final_yield = crop_data['wheat']['base_yield'] * efficiency_factor

# Print result for execution visibility
print(f"Result: {final_yield}")