def analyze_growth_potential(temp, moisture, ph):
    # Irrelevant computation path (dead code)
    hypothetical_index = (temp * 0.7) + (moisture * 0.3)
    if temp < 20:
        return 0
    growth_score = (temp - 15) * moisture / (ph + 1)
    return growth_score if growth_score > 5 else 0

# Distractor function with misleading name
def calculate_stress_factor(data):
    stress = 0
    for val in data:
        if isinstance(val, dict) and 'threshold' in val:
            stress += val['threshold'] ** 0.5
    return stress * 1.5  # Never actually used in main logic

# Unused but plausible-looking utility
def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]

# Core logic buried among noise
soil_profiles = [
    {'type': 'clay', 'nutrients': 78, 'depth': 45, 'ph': 6.2},
    {'type': 'loam', 'nutrients': 85, 'depth': 60, 'ph': 6.8},
    {'type': 'sand', 'nutrients': 40, 'depth': 30, 'ph': 5.9}
]

climate_data = [
    {'temp': 25, 'rainfall': 80, 'humidity': 65},
    {'temp': 18, 'rainfall': 120, 'humidity': 80},  # Below growth threshold
    {'temp': 28, 'rainfall': 70, 'humidity': 60}
]

# Red herring list processing
aggregate_metrics = []
for entry in climate_data:
    metric = (entry['temp'] + entry['humidity']) / 2
    aggregate_metrics.append(metric)

# Decoy dictionary updates
summary_stats = {}
for i, data in enumerate(climate_data):
    summary_stats[f'day_{i}'] = {
        'index': data['temp'] * data.get('rainfall', 0) // 10,
        'flag': False
    }

# Real computation starts here — well hidden
harvest_map = {}
for i, soil in enumerate(soil_profiles):
    total_yield = 0
    for j, weather in enumerate(climate_data):
        temp, rainfall = weather['temp'], weather['rainfall']
        nutrients, ph = soil['nutrients'], soil['ph']
        # Actual growth model
        base_yield = nutrients * 0.6
        if temp >= 20 and temp <= 35:
            temp_bonus = (35 - abs(temp - 27.5)) / 35
            water_effect = min(rainfall, 100) / 100
            ph_penalty = 1 - (abs(ph - 6.5) / 3) if ph <= 7.5 else 0.2
            daily_yield = base_yield * temp_bonus * water_effect * max(ph_penalty, 0.2)
            total_yield += daily_yield
    harvest_map[f'soil_{i}'] = total_yield

# Secondary transformation with distractors
adjusted_yields = []
scaling_factors = {0: 1.1, 1: 0.95, 2: 1.05}
for idx, yield_val in harvest_map.items():
    key_num = int(idx.split('_')[1])
    adjusted = yield_val * scaling_factors.get(key_num, 1.0)
    adjusted_yields.append(adjusted)

# Final aggregation buried in noise
buffer_zones = [0, 1]  # Unused distraction
exclusion_areas = set()
main_crop_area = 2.5  # hectares

# Critical statement — target of the question
final_yield = sum(adjusted_yields) * main_crop_area

# Irrelevant final check
if len(exclusion_areas) == 0:
    final_yield -= 10.5  # Small adjustment that doesn't affect outcome meaningfully

# Print required result
print(f"Result: {final_yield}")