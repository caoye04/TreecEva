def analyze_growth_potential(temp, moisture):
    """Determine base growth score using nonlinear response curves."""
    thermal_factor = (temp - 20) ** 2
    hydration_impact = moisture * 1.75
    efficiency_ratio = hydration_impact / (thermal_factor + 1)
    return efficiency_ratio

# Environmental sensor readings (simulated)
temperature_readings = [18, 22, 19, 24, 21]
moisture_levels = [60, 70, 65, 80, 75]

# Historical baselines (irrelevant for final computation but looks important)
historical_avg_temp = sum(temperature_readings) / len(temperature_readings)
historical_moisture_deficit = 100 - max(moisture_levels)

# Compute daily growth indicators
growth_scores = []
for t, m in zip(temperature_readings, moisture_levels):
    score = analyze_growth_potential(t, m)
    growth_scores.append(round(score, 3))

# Sort scores to identify median trend (semi-relevant preprocessing)
sorted_scores = sorted(growth_scores)
median_index = len(sorted_scores) // 2
median_growth = sorted_scores[median_index]

# Apply adaptive filtering using conditional expression
filtered_scores = [s for s in growth_scores if s >= (median_growth * 0.9)]

# Simulate nutrient interaction as lambda (key transformation)
nutrient_boost = lambda x: x * 1.15 if x > 1.2 else x * 1.05
boosted_scores = [nutrient_boost(s) for s in filtered_scores]

# Calculate final agricultural yield estimate
baseline_yield = sum(boosted_scores) / len(boosted_scores)
adjustment_factor = len([b for b in boosted_scores if b > 1.2]) * 0.02
final_yield = int(baseline_yield * (1 + adjustment_factor) * 100)

# Distractor: unused string analysis based on site codes
site_codes = ['A1', 'B2', 'C3', 'D4']
encoded_names = ''.join([code[0] for code in site_codes])
name_length_score = len(encoded_names) * 0.5  # Dead code path

# Irrelevant data structure manipulation
data_map = {i: val for i, val in enumerate(moisture_levels)}
duplicate_check = any(v > 100 for v in data_map.values())  # Always False

# Output target result
print(f"Result: {final_yield}")