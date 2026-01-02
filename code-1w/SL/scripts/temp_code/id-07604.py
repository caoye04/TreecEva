def analyze_rainfall(data):
    wet_days = sum(1 for x in data if x > 5)
    total_rain = sum(data)
    avg_rain = total_rain / len(data) if data else 0
    adjusted = [x * 0.8 for x in data]  # evaporation adjustment (distractor)
    return wet_days, avg_rain

soil_nutrients = {'nitrogen': 42, 'phosphorus': 18, 'potassium': 27}
decay_rate = 0.95
projected_loss = 0  # unused variable (distractor)

for key in soil_nutrients:
    soil_nutrients[key] *= decay_rate  # simulate degradation

climate_data = [12, 3, 0, 8, 15, 22, 4, 0, 7, 11]
baseline_moisture = sum(climate_data) * 0.3
threshold_check = baseline_moisture > 50

# Irrelevant transformation (distractor)
encoded_data = ''.join([chr(97 + (i % 26)) for i in range(len(climate_data))])

soil_conditions = {
    'ph': 6.4,
    'organic_content': 3.2,
    'drainage': 'moderate',
    'nutrient_score': sum(soil_nutrients.values()) / 3
}

if threshold_check:
    temp_adj = 1.1
else:
    temp_adj = 0.9

harvest_base = 100 if threshold_check else 80

# Additional irrelevant calculation (distractor)
wind_speed_factor = [x * 0.02 for x in climate_data]

wet_days, avg_rainfall = analyze_rainfall(climate_data)

yield_potential = harvest_base * temp_adj

if soil_conditions['ph'] < 6.0 or soil_conditions['ph'] > 7.5:
    ph_penalty = 0.8
else:
    ph_penalty = 1.0

# Conditional expression (required feature)
bonus = 15 if soil_conditions['organic_content'] > 3.0 and avg_rainfall > 8 else 5

# Dictionary operation (required feature)
soil_conditions['adjusted_yield_base'] = yield_potential * ph_penalty

# Slicing operation (required feature)
historical_avg = climate_data[2:7]
recent_trend = climate_data[-3:]

recent_boost = 1.05 if sum(recent_trend) > sum(historical_avg) * 0.3 else 1.0

final_yield = soil_conditions['adjusted_yield_base'] + bonus
final_yield *= recent_boost

# Dead code path (distractor)
if False:
    final_yield = -999

Result: final_yield