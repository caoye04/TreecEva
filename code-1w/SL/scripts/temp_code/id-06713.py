def analyze_growth_patterns(data, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [x * 1.05 for x in data]
    above_threshold = [x for x in data if x > thresholds[0]]
    return len(above_threshold) > 3

# Simulate agricultural sensor readings (domain-specific context)
temperature_readings = [23.4, 25.1, 22.7, 26.3, 24.8, 23.9]
humidity_levels = [61, 67, 59, 72, 65, 63]
soil_nutrients = [88, 94, 82, 96, 89, 91]

# Misleading intermediate calculations (dead code path)
avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_humidity = sum(humidity_levels) / len(humidity_levels)
dummy_score = avg_temp * 0.3 + avg_humidity * 0.7

# Core logic: nutrient zones and growth potential
nutrient_set_a = {88, 94, 82, 96}
nutrient_set_b = {82, 89, 91}
common_nutrients = nutrient_set_a & nutrient_set_b  # intersection: {82}
unique_to_a = nutrient_set_a - nutrient_set_b        # {88, 94, 96}

# Initialize key variables
area_metrics = [5.2, 3.8, 4.1, 6.3]
yield_factors = [0.88, 0.76, 0.91, 0.83]

# Secondary distraction: unused helper function
def estimate_water_usage(area_list):
    total = 0
    for a in area_list:
        if a > 5.0:
            total += a * 1.4
        else:
            total += a * 1.1
    return total

# Complex conditional with nested logic and distractors
if len(common_nutrients) >= 1:
    adjustment_factor = 1.15
    temp_impact = 0
    for t in temperature_readings:
        if 22 <= t <= 24:
            temp_impact += 1
        elif t > 26:
            temp_impact -= 0.5
    
    # Red herring computation (not used later)
    stability_index = temp_impact / len(temperature_readings)
    
    # Real but obfuscated calculation
    base_yield = 0
    for i in range(len(area_metrics)):
        base_yield += area_metrics[i] * yield_factors[i]
    
    # Another misleading set operation
    humidity_set = set(humidity_levels)
    high_humidity = {h for h in humidity_set if h > 65}
    humidity_penalty = len(high_humidity) * 0.05
    
    # Final efficiency depends only on base_yield and adjustment_factor
    final_yield = base_yield * adjustment_factor
else:
    final_yield = sum(area_metrics) * 0.5

# Unrelated logging (distractor output)
print(f"Sensor points analyzed: {len(temperature_readings)}")
print(f"Nutrient consistency score: {len(common_nutrients) * 2.5}")

Target result: {final_yield}