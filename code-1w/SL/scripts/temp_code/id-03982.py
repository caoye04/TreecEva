def analyze_growth_rate(temperature, moisture):
    # Irrelevant helper with misleading intermediate
    base = temperature * 0.8 + moisture * 1.2
    penalty = 0
    if temperature > 35:
        penalty += (temperature - 35) * 2
    if moisture < 30:
        penalty += (30 - moisture) * 1.5
    return max(0, base - penalty)

# Unused but plausible decoy function
def predict_pest_outbreak(humidity, wind_speed):
    risk = humidity * 0.05 - wind_speed * 0.1
    return min(10, max(0, risk))

# Distractor data
pest_risk_lookup = {
    'low': [1, 2, 3],
    'medium': [4, 5, 6],
    'high': [7, 8, 9]
}

soil_profiles = [
    {'type': 'clay', 'ph': 6.5, 'nutrients': 78, 'depth': 45},
    {'type': 'loam', 'ph': 6.8, 'nutrients': 88, 'depth': 60},
    {'type': 'sandy', 'ph': 5.9, 'nutrients': 65, 'depth': 38}
]

current_irrigation_levels = [30, 45, 60, 75]  # Dead code path

climate_data = [
    {'temp': 28, 'humidity': 60, 'rainfall': 120},
    {'temp': 32, 'humidity': 45, 'rainfall': 80},
    {'temp': 25, 'humidity': 70, 'rainfall': 150}
]

# Real computation begins here
harvest_potential = []

for day in climate_data:
    temp = day['temp']
    rain = day['rainfall']
    moisture = rain * 0.3
    daily_yield = 0
    
    for profile in soil_profiles:
        nutrients = profile['nutrients']
        depth = profile['depth']
        ph = profile['ph']
        
        # Effective growth window
        if 5.5 <= ph <= 7.0 and depth >= 40:
            growth_multiplier = 1.0
            if temp > 30:
                growth_multiplier *= 0.9
            if moisture < 25:
                growth_multiplier *= 0.85
            
            # Core yield formula
            raw_yield = nutrients * 0.6 * growth_multiplier
            daily_yield += raw_yield
    
    harvest_potential.append(daily_yield)

# Misleading transformation
adjusted_potential = [x * 1.1 for x in harvest_potential if x > 50]  # Partial filter

# Red herring: unused sorting
sorted_potential = sorted(harvest_potential, reverse=True)
ranked_days = {i: val for i, val in enumerate(sorted_potential)}

# Fake aggregation
phantom_total = sum([harvest_potential[i] * (i+1) for i in range(len(harvest_potential))])

# Real optimization logic
max_yield = 0
for i, yield_val in enumerate(harvest_potential):
    effective_rain = climate_data[i]['rainfall']
    evaporation_factor = 1 - (climate_data[i]['humidity'] / 100) * 0.4
    net_water = effective_rain * evaporation_factor
    
    if net_water < 50:
        yield_val *= 0.7  # Stress penalty
    
    if yield_val > max_yield:
        max_yield = yield_val

# Final adjustment using dictionary mapping (core concept)
yield_tiers = {'low': 40, 'medium': 70, 'high': 100}
tier_bonus = 0
if max_yield < 50:
    tier_bonus = -5
elif max_yield < 80:
    tier_bonus = 3
else:
    tier_bonus = 8

final_yield = max_yield + tier_bonus

# Print required output
print(f"Result: {final_yield}")