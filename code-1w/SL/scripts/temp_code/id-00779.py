def analyze_growth_potential(temperature, rainfall):
    # Assess base growth potential from climate
    if temperature < 15 or temperature > 35:
        return 0.3
    elif rainfall < 20:
        return 0.4
    else:
        return (temperature * 0.02) + (rainfall * 0.01)

# Simulate multi-season yield tracking
total_tracker = [0] * 4
seasonal_weights = [0.8, 1.1, 0.9, 1.2]
phantom_buffer = [0.1, 0.3, 0.5]

# Fictitious sensor calibration (irrelevant to final result)
sensor_offset = sum([i * 0.05 for i in range(4)])
calibration_factor = max(seasonal_weights) - min(seasonal_weights)

climate_data = {'temp_avg': 24, 'rain_mm': 60}
soil_quality = {'ph': 6.5, 'nutrients': 80, 'toxins': False}

# Secondary metric with no impact on final yield
structural_integrity = 95 if soil_quality['ph'] > 6.0 else 70
moisture_retention = climate_data['rain_mm'] * 0.75

# Conditional expression used in optimization
base_score = analyze_growth_potential(climate_data['temp_avg'], climate_data['rain_mm'])
nutrient_boost = 1.2 if soil_quality['nutrients'] > 75 else 1.0

# Distractor: simulate unused seasonal projections
for i in range(4):
    projected = base_score * seasonal_weights[i]
    total_tracker[i] = projected * nutrient_boost

# Unused loop with side computation (adds cognitive load)
aggregate_deviation = 0.0
for val in phantom_buffer:
    aggregate_deviation += abs(val - 0.3)

# Core logic: optimization using conditional expression and checks
intermediate_yield = base_score * nutrient_boost * 100
penalty = 0.1 if soil_quality['toxins'] else 0.0
adjusted_yield = intermediate_yield * (1 - penalty)

# Final optimization step combining all valid factors
final_yield = adjusted_yield if adjusted_yield > 50 else 50

# Print target result
print(f"Target result: {final_yield}")