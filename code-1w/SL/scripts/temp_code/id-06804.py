def analyze_rainfall(data):
    rainy_days = len([x for x in data if x > 5])
    total_rain = sum(data)
    avg_rain = total_rain / len(data) if data else 0
    threshold_met = [day for day, rain in enumerate(data) if rain > 10]
    return avg_rain, rainy_days

soil_quality = {'nitrogen': 0.8, 'phosphorus': 0.4, 'potassium': 0.6}
decay_factor = 0.95
projected_loss = 0

for i in range(3):
    projected_loss += (1 - decay_factor) * 10

climate_data = [12, 3, 8, 15, 6, 4, 10, 14, 2, 11]
baseline_temp = 22
adjustment = 0.5 if baseline_temp > 20 else 0.3

adjusted_data = [x * adjustment for x in climate_data]
scaled_data = [x * 1.1 for x in adjusted_data if x > 4]

surplus = sum(scaled_data) - sum(climate_data)
phantom_buffer = surplus * 0.1  # Unused distraction

soil_conditions = []
for nutrient, level in soil_quality.items():
    if level < 0.5:
        soil_conditions.append(f"{nutrient}_deficient")
    elif level > 0.7:
        soil_conditions.append(f"{nutrient}_rich")
    else:
        soil_conditions.append(f"{nutrient}_moderate")

# Irrelevant transformation chain
temp_analysis = list(map(lambda x: x ** 0.5, [100, 81, 64]))
offset_correction = sum(temp_analysis) / 10

flagged_days = []
i = 0
while i < len(climate_data):
    if climate_data[i] > 12:
        flagged_days.append(i)
    i += 1

ignored_metric = len(flagged_days) * offset_correction

interim_result = analyze_rainfall(climate_data)
rain_avg, wet_days = interim_result

# Core logic embedded with distractions
def optimize_harvest(rainfall, soil):
    base_yield = 100
    stress_penalty = 0
    
    if wet_days > 5:
        stress_penalty += 15
    elif wet_days < 3:
        stress_penalty += 20
    
    rich_count = len([s for s in soil if "rich" in s])
    deficient_count = len([s for s in soil if "deficient" in s])
    
    yield_boost = rich_count * 8
    yield_cut = deficient_count * 12
    
    # Distractor: complex but unused calculation
    phantom_risk = (sum(rainfall) / 100) ** 2 + (len(soil) * 0.5)
    dummy_score = 100 - phantom_risk
    
    # Actual yield computation
    effective_yield = base_yield + yield_boost - yield_cut - stress_penalty
    
    # Secondary adjustment based on rainfall distribution
    peak_events = len([r for r in rainfall if r > 10])
    if peak_events > 4:
        effective_yield *= 0.9  # Over-rainfall reduces efficiency
    
    final_yield = round(effective_yield)
    
    return final_yield

result = optimize_harvest(climate_data, soil_conditions)
final_yield = result
print(f"Target result: {final_yield}")