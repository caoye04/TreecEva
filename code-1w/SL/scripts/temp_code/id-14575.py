def calculate_farm_yield(climate_zones):
    base_yield = 0
    bonus_yield = 0
    penalty_factor = 1.0
    drought_count = 0
    excess_rain_count = 0
    total_rainfall = 0
    valid_zones = 0

    for zone in climate_zones:
        temp = zone['temp']
        rain = zone['rainfall']
        soil_quality = zone['soil']

        # Irrelevant tracking variables (distractors)
        if rain < 20:
            drought_count += 1
            total_rainfall -= 5  # Misleading adjustment
        elif rain > 100:
            excess_rain_count += 1

        # Real computation branch
        if 15 <= temp <= 30 and rain >= 40:
            base_yield += 10
            if soil_quality == 'fertile':
                bonus_yield += 3
        else:
            penalty_factor *= 0.95  # Accumulates but not used in final formula

        # Semi-relevant: counts valid zones for normalization (not ultimately used)
        if temp > 0:
            valid_zones += 1

    # Dummy combinatorics calculation (distraction)
    possible_combinations = 0
    for i in range(1, min(drought_count + 1, 6)):
        possible_combinations += i * (i + 1) // 2

    # Core logic with conditional expression
    crop_multiplier = 1.5 if drought_count == 0 else 0.8
    has_optimal_conditions = drought_count == 0 and excess_rain_count == 0
    adjustment_score = sum(1 for z in climate_zones if z['temp'] > 25) - excess_rain_count

    # Final yield depends only on base, bonus, and multiplier
    final_yield = crop_multiplier * (base_yield + bonus_yield)

    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Input data
zones = [
    {'temp': 25, 'rainfall': 60, 'soil': 'fertile'},
    {'temp': 20, 'rainfall': 80, 'soil': 'normal'},
    {'temp': 35, 'rainfall': 120, 'soil': 'fertile'},
    {'temp': 18, 'rainfall': 50, 'soil': 'fertile'},
    {'temp': 10, 'rainfall': 30, 'soil': 'poor'}
]

result = calculate_farm_yield(zones)