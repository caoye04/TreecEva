def analyze_rainfall(data):
    # Irrelevant analysis with side computation
    excess = sum([x for x in data if x > 100])
    deficit = sum([1 for x in data if x < 30])
    normalized = [max(0, x - 10) for x in data]
    return sum(normalized) // len(normalized)


def assess_ph_balance(soil_list):
    # Distractor function: computes average but not used directly
    avg_ph = sum(soil_list) / len(soil_list)
    deviations = list(map(lambda x: abs(x - avg_ph), soil_list))
    stability_score = 100 - sum(deviations)
    return stability_score

# Simulate environmental conditions
climate_data = [85, 90, 110, 45, 60, 130, 75]
soil_conditions = [6.2, 5.8, 6.5, 6.0, 5.9, 6.3]

# Misleading preliminary calculations
baseline_rain = analyze_rainfall(climate_data)
total_stability = assess_ph_balance(soil_conditions)
projected_loss = 0
for day in climate_data:
    if day > 100:
        projected_loss += 3
    elif day < 50:
        projected_loss += 5

# Hidden critical logic: count optimal growth windows
consecutive_suitable = 0
max_window = 0
for rain in climate_data:
    if 60 <= rain <= 100:
        consecutive_suitable += 1
    else:
        if consecutive_suitable > max_window:
            max_window = consecutive_suitable
        consecutive_suitable = 0
if consecutive_suitable > max_window:
    max_window = consecutive_suitable

# Secondary factor: number of balanced soil readings
acceptable_readings = len([ph for ph in soil_conditions if 5.8 <= ph <= 6.4])

# Core yield model — depends only on max_window and acceptable_readings
yield_per_window = 17
base_efficiency = 0.9

# Final optimization function
def optimize_harvest(rainfall, ph_levels):
    window_factor = max_window * yield_per_window
    quality_bonus = acceptable_readings * 12
    efficiency_correction = base_efficiency if total_stability > 85 else 0.75
    
    # Dead code branch — never executed due to fixed data
    emergency_adjustment = 0
    if baseline_rain < 20:
        emergency_adjustment = -50  # Not triggered
    elif baseline_rain > 200:
        emergency_adjustment = 30   # Not triggered
    
    raw_yield = (window_factor + quality_bonus) * efficiency_correction
    loss_deduction = min(projected_loss * 4, raw_yield * 0.3)  # Capped deduction
    net_yield = raw_yield - loss_deduction
    
    # Normalize to nearest 5
    return (int(round(net_yield / 5)) * 5)

final_yield = optimize_harvest(climate_data, soil_conditions)
print(f"Result: {final_yield}")