import math

# Simulated agricultural dataset (irrelevant to final computation but looks important)
soil_profiles = [
    {'ph': 6.5, 'moisture': 0.3, 'nutrients': 80, 'depth': 30},
    {'ph': 7.2, 'moisture': 0.4, 'nutrients': 65, 'depth': 25},
    {'ph': 5.8, 'moisture': 0.35, 'nutrients': 90, 'depth': 35}
]

crop_rotation = ['wheat', 'corn', 'soybean']
temperature_log = [22, 24, 19, 25, 23, 20, 21]

# Distractor function: unused in final calculation
def analyze_rainfall(patterns):
    total = 0
    for p in patterns:
        if p > 0.5:
            total += p * 1.5
    return total if total > 10 else round(total, 2)

# Irrelevant climate scoring system (dead path)
climate_scores = {}
for i, temp in enumerate(temperature_log):
    score = (temp - 20) ** 2 + 5
    climate_scores[f'day_{i}'] = score

# Real input data disguised among distractors
climate_data = {
    'avg_temp': 22.5,
    'sunlight_hours': 7.2,
    'humidity_index': 0.68,
    'wind_stability': 0.88
}

# Unused transformation pipeline (misleading intermediate steps)
processed_inputs = []
for key, val in climate_data.items():
    processed = round((val * 1.1) ** 0.5, 3)
    processed_inputs.append(processed)

# Decoy model weights (look computational but unused)
weights = [0.25, 0.18, 0.33, 0.24]
weighted_sum = sum(w * p for w, p in zip(weights, processed_inputs))

# Hidden relevant data embedded in string metadata (requires parsing)
data_header = "HDR|YIELDv3|TEMP_ADJ=0.77|SOIL_MOD=1.03|YEAR=2023"
temp_adj = float(data_header.split('|')[2].split('=')[1])
soil_mod = float(data_header.split('|')[3].split('=')[1])

# Core logic hidden behind lambda and conditional expression
base_productivity = lambda t, h: (t * 0.8) + (h * 10)

# Simulate pest resistance level from string pattern (distractor)
pest_sequence = "AGCTTGAC"
resistance_score = pest_sequence.count('G') * pest_sequence.count('C') // max(1, len(pest_sequence) // 4)

# Actual core calculation buried in complex conditional
if climate_data['avg_temp'] > 20:
    growth_factor = 1.25
    if climate_data['sunlight_hours'] >= 7:
        growth_factor += 0.15
        # Nested condition with red herring
        if resistance_score > 2:
            growth_factor *= 1.05  # never reached
    else:
        growth_factor -= 0.2
else:
    growth_factor = 0.8

# Secondary adjustment using bit manipulation (appears cryptic)
humidity_int = int(climate_data['humidity_index'] * 100)
adjusted_mask = (humidity_int << 2) ^ 0b1010
mask_effect = bin(adjusted_mask).count('1') % 3 / 10  # yields 0.2

growth_factor += mask_effect

# Final optimization function combining multiple concepts
def optimize_harvest(climate, soils):
    # Extract values using dictionary get method with default (real inputs)
    t = climate.get('avg_temp', 20)
    s = climate.get('sunlight_hours', 6)
    
    # Use lambda inside function
    base = base_productivity(t, climate['humidity_index'])
    
    # Conditional expression with nested arithmetic
    modifier = 1.1 if s > 6.5 else 0.95
    
    # Incorporate hidden constants from string parsing
    modifier *= temp_adj  # 0.77
    
    # Real productivity calculation
    raw_yield = base * modifier * growth_factor
    
    # Final adjustment using soil nutrients from first profile only
    primary_nutrients = soils[0]['nutrients']  # 80
    nutrient_boost = 1 + (primary_nutrients - 70) / 100  # 1.1
    
    # Apply boost
    final = raw_yield * nutrient_boost
    
    # Dead code branch (looks like correction but unused)
    if final > 100:
        scaling = math.log(final) / 10
        final /= scaling  # not triggered
    
    return int(round(final))

# Misleading post-processing (not assigned)
[math.sqrt(x['ph']) for x in soil_profiles]

# Key execution point
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print result as required
print(f"Target result: {final_yield}")