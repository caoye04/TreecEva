def analyze_growth_factors(temperature, rainfall):
    if temperature < 15 or rainfall < 200:
        return 0
    elif temperature > 30 or rainfall > 800:
        return 1
    else:
        return 2

# Simulate seasonal crop growth cycle
temperature_readings = [22, 25, 19, 31, 27]
rainfall_data = [300, 600, 150, 700, 400]

accumulated_stress = 0
viable_days = 0
false_alarm_counter = 0

for i in range(len(temperature_readings)):
    temp = temperature_readings[i]
    rain = rainfall_data[i]
    
    # Assess daily environmental stress
    if temp < 20 and rain < 250:
        accumulated_stress += 1
    elif temp > 28 and rain > 600:
        accumulated_stress += 2
    
    # Track potentially viable growth days
    if temp >= 20 and temp <= 30 and rain >= 250:
        viable_days += 1

    # Irrelevant tracking (distractor)
    if temp == 25 or rain == 500:
        false_alarm_counter += 1

# Compute climate score based on analysis
climate_assessment = analyze_growth_factors(sum(temperature_readings) / len(temperature_readings), sum(rainfall_data) / len(rainfall_data))
climate_score = climate_assessment * viable_days - accumulated_stress

# Soil condition evaluation (mixed logic)
base_nutrients = 45
ph_level = 6.8
soil_conditions = []

if ph_level < 5.5 or ph_level > 7.5:
    soil_conditions.append('unbalanced')
else:
    soil_conditions.append('optimal')

soil_conditions.append('loamy')

# Dead code path (distractor)
if base_nutrients > 100:
    soil_conditions.append('overfertilized')

# Conditional expression for nutrient boost
nutrient_boost = 10 if 'optimal' in soil_conditions else 5

# Harvest potential calculation function
def calculate_harvest_potential(score, soil):
    base_yield = score * 15
    adjustment_factor = 1.2 if 'optimal' in soil else 0.8
    
    # Additional irrelevant check (distractor)
    texture_modifier = 1.0
    for layer in soil:
        if layer == 'clay':
            texture_modifier = 0.9

    # Final yield computation (key line)
    final_yield = base_yield * adjustment_factor + nutrient_boost
    
    return int(final_yield)

# Execute main calculation
final_yield = calculate_harvest_potential(climate_score, soil_conditions)

print(f"Result: {final_yield}")