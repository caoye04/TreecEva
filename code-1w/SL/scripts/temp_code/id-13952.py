import math

# Simulated sensor readings from agricultural field zones
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9]
humidity_readings = [61, 58, 65, 54, 50, 57, 60]
soil_moisture = [32, 35, 30, 38, 40, 36, 33]
light_exposure = [8.2, 8.5, 7.9, 8.7, 9.0, 8.4, 8.1]

# Irrelevant baseline metrics (distractor)
baseline_yield = 1200
adjustment_factor = 0.94
phantom_offset = 42  # Unused in logic

# Preprocessing: Normalize data to index scale (0-10)
def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) * 10 for x in data]

# Misleading function - looks important but unused
def calculate_stress_index(temp, hum):
    stress = 0
    for t, h in zip(temp, hum):
        if t > 25 and h < 55:
            stress += 1.5
        elif t < 23 and h > 60:
            stress += 1.0
    return stress * 10

# Another decoy function with plausible name
def compute_frost_risk(temps):
    risk_score = 0
    for t in temps:
        if t < 22:
            risk_score += (22 - t) * 2
    return risk_score  # Never actually used

# Core processing pipeline
normalized_temp = normalize_readings(temperature_readings)
normalized_humid = normalize_readings(humidity_readings)
normalized_moist = normalize_readings(soil_moisture)
normalized_light = normalize_readings(light_exposure)

# Composite health score with weighted contributions
plant_health_scores = []
for i in range(len(temperature_readings)):
    # Weighted combination: temp (30%), moisture (40%), light (20%), humidity (10%)
    score = (normalized_temp[i] * 0.3 + 
             normalized_moist[i] * 0.4 + 
             normalized_light[i] * 0.2 + 
             normalized_humid[i] * 0.1)
    plant_health_scores.append(round(score, 3))

# Simulate pest detection events (red herring list)
pest_events = [False, False, True, False, False, False, True]
false_alarm_correction = 0.98  # Looks relevant but not used

# Data filtering based on anomalous readings
valid_zones = []
anomaly_threshold = 2.5
for idx, score in enumerate(plant_health_scores):
    deviation = abs(score - 5.0)  # Center around neutral 5.0
    if deviation <= anomaly_threshold:
        valid_zones.append(idx)

# Process only valid zones
filtered_health = [plant_health_scores[i] for i in valid_zones]

# Secondary filter: remove any zone with raw soil moisture < 31 (additional constraint)
final_zone_indices = []
for i in valid_zones:
    if soil_moisture[i] >= 31:
        final_zone_indices.append(i)

refined_health = [plant_health_scores[i] for i in final_zone_indices]

# Complex conditional expression to determine growth phase adjustment
length_days = 90
phase_weight = 1.1 if length_days > 80 else (1.05 if length_days > 60 else 1.0)

# Accumulate total potential yield before loss factors
base_potential = sum([h * 100 for h in refined_health])

# Simulate nutrient deficiency (unrelated to other variables)
nutrient_levels = [88, 91, 85, 93, 87]
deficiency_penalty = 0
for level in nutrient_levels:
    if level < 90:
        deficiency_penalty += (90 - level) * 2

# Harvest efficiency model with recursion (actual used recursive function)
def calculate_efficiency(depth, total_area=1):
    if depth <= 1:
        return 0.95
    else:
        sub_eff = calculate_efficiency(depth - 1, total_area / 2)
        return sub_eff * 0.92 + 0.03

harvest_efficiency = calculate_efficiency(len(final_zone_indices))

# Final yield calculation incorporating all factors
processed_data = {
    'potential': base_potential,
    'efficiency': harvest_efficiency,
    'penalty': deficiency_penalty,
    'count': len(final_zone_indices)
}

# Critical statement containing the answer
def harvest_results(data):
    gross = data['potential'] * data['efficiency']
    net = gross - data['penalty'] * 10
    # Additional small bonus if more than 3 zones contributed
    bonus = 50 if data['count'] > 3 else 0
    return int(net + bonus)

final_yield = harvest_results(processed_data)

# Dead code path (never executed)
if __debug__:
    validation_check = sum(humidity_readings) / len(humidity_readings)
    calibration_offset = math.sin(0.1 * validation_check)

# Print result as required
print(f"Target result: {final_yield}")