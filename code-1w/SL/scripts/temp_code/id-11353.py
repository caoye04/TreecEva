def analyze_rainfall(data):
    wet_days = [r for r in data if r > 5]
    total_rain = sum(wet_days)
    avg_rain = total_rain / len(wet_days) if wet_days else 0
    return avg_rain

soil_quality = {'clay': 0.3, 'silt': 0.4, 'sand': 0.3}
decay_factor = 0.9

# Simulate temperature stress adjustment
def adjust_yield(base, temp):
    if temp < 15:
        return base * 0.7
    elif temp > 30:
        return base * 0.6
    else:
        return base

# Unused function - distractor
def predict_market_price(yield_amount):
    trend = 1.05
    inflation = 0.02
    return yield_amount * 3.5 * (trend + inflation)

# Soil nutrient degradation simulation (not used in final result)
current_nutrients = 100
for day in range(10):
    current_nutrients *= 0.98

climate_data = [22, 25, 27, 23, 31, 18]
soil_conditions = {'ph': 6.5, 'moisture': 0.4, 'nitrogen': 18}

baseline_yield = 80
yield_adjustments = []

for temp in climate_data:
    adjusted = adjust_yield(baseline_yield, temp)
    yield_adjustments.append(adjusted)

avg_adjusted_yield = sum(yield_adjustments) / len(yield_adjustments)

rainfall_data = [4, 6, 7, 3, 8, 12]
mean_rainfall = analyze_rainfall(rainfall_data)

# Secondary adjustment based on moisture
if soil_conditions['moisture'] < 0.3:
    moisture_modifier = 0.8
elif soil_conditions['moisture'] > 0.5:
    moisture_modifier = 0.9
else:
    moisture_modifier = 1.1

# Distractor calculation with no impact
theoretical_max = baseline_yield * 1.2
potential_loss = theoretical_max - avg_adjusted_yield

# Final optimization logic
if mean_rainfall > 6:
    rainfall_bonus = 1.15
else:
    rainfall_bonus = 1.0

final_yield = avg_adjusted_yield * moisture_modifier * rainfall_bonus

# Additional irrelevant computation
efficiency_ratio = final_yield / (sum(soil_quality.values()) * 10)

Result: {final_yield}