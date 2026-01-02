def analyze_growth_factors(temperature, humidity, rainfall):
    base_index = temperature * 0.3 + humidity * 0.2
    adjusted_rainfall = max(rainfall, 10)
    efficiency = 1.0 if humidity > 60 else 0.8
    microbe_activity = (rainfall // 10) * 1.5
    return base_index * efficiency + microbe_activity


def assess_soil_nutrients(nutrient_levels):
    total_nutrients = sum(nutrient_levels)
    avg_level = total_nutrients / len(nutrient_levels)
    imbalance_penalty = abs(max(nutrient_levels) - min(nutrient_levels)) * 0.1
    stability_score = 100 - (total_nutrients % 20)
    normalized_score = (avg_level - imbalance_penalty) * 0.9
    return normalized_score if normalized_score > 0 else 5


temperature_data = [22, 25, 20, 24]
humidity_data = [55, 65, 50, 70]
rainfall_data = [80, 120, 60, 100]
nutrients = [18, 24, 15, 22, 19]

# Preliminary diagnostics (distractor computations)
diagnostic_sum = sum([t ** 0.5 for t in temperature_data])
humidity_variance = max(humidity_data) - min(humidity_data)
rain_consistency = len([r for r in rainfall_data if r > 70])

# Core evaluation chain
climate_factors = []
for i in range(len(temperature_data)):
    score = analyze_growth_factors(temperature_data[i], humidity_data[i], rainfall_data[i])
    climate_factors.append(score)

baseline_climate = sum(climate_factors) / len(climate_factors)
soil_health = assess_soil_nutrients(nutrients)

# Secondary adjustments (some are distractions)
moisture_retention = 0.4 * humidity_data[-1]
depletion_factor = (temperature_data[0] - 20) * 0.3
buffer_margin = 2.5 if rain_consistency > 2 else 1.0
irrelevant_offset = diagnostic_sum * 0.01  # unused in final logic

adjusted_climate = baseline_climate - depletion_factor
climate_score = max(adjusted_climate, 30)

# Final yield calculation with conditional expression
final_yield = 0
def calculate_harvest_potential(climate, soil):
    base_potential = climate * 0.7 + soil * 0.3
    bonus = 10 if climate > 45 and soil > 20 else 5
    penalty = 0
    if base_potential < 40:
        penalty = 15
    elif base_potential > 60:
        penalty = -5  # reward
    adjusted_potential = base_potential + bonus - penalty
    return int(adjusted_potential * 1.1)  # scaling factor applied

final_yield = calculate_harvest_potential(climate_score, soil_health)

# Distractor: logging intermediate values
temp_log = [round(x, 1) for x in climate_factors]
avg_log = round(baseline_climate, 2)

# Output result
Target result: {final_yield}