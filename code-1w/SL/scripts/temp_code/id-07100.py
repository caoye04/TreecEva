def calculate_harvest_efficiency(plots):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 80
    efficiency_scores = []

    for plot in plots:
        size = plot['size']
        crop_type = plot['crop']
        health = plot['health']
        elevation = plot['elevation']

        # Irrelevant environmental factor (distractor)
        wind_exposure = plot.get('wind', 0) * 0.01

        # Primary yield calculation
        base_yield = size * health * base_multiplier

        # Crop-specific adjustment (relevant logic)
        if crop_type == 'wheat':
            base_yield *= 1.2
        elif crop_type == 'corn':
            base_yield *= 1.4
        else:
            base_yield *= 1.1

        # Elevation penalty (semi-relevant, but capped)
        elevation_penalty = max(0.7, 1 - (elevation * 0.005))
        adjusted_yield = base_yield * elevation_penalty

        # Bonus for high health (only if above threshold)
        if health > bonus_threshold:
            adjusted_yield *= 1.3

        # Dead code path - never executed due to data constraint (distractor)
        if crop_type == 'rice':
            adjusted_yield += 10  # unreachable in current data

        efficiency_scores.append(adjusted_yield)

    # Irrelevant list comprehension: computes unused statistic
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores) if efficiency_scores else 0
    std_deviation = [round((x - avg_efficiency) ** 2, 3) for x in efficiency_scores]  # distractor

    # Final aggregation using weighted contribution based on original plot size
    total_size = sum(plot['size'] for plot in plots)
    weighted_yield = sum(
        (score * plots[i]['size']) / total_size 
        for i, score in enumerate(efficiency_scores)
    )

    # Secondary adjustment based on global conditions (mock)
    weather_bonus = 0.05
    final_yield = int(round(weighted_yield * (1 + weather_bonus)))  # key assignment

    return final_yield

# Simulated agricultural data
plots = [
    {'size': 10, 'crop': 'wheat', 'health': 85, 'elevation': 200},
    {'size': 15, 'crop': 'corn', 'health': 75, 'elevation': 150},
    {'size': 12, 'crop': 'barley', 'health': 90, 'elevation': 300},
    {'size': 8, 'crop': 'wheat', 'health': 95, 'elevation': 100}
]

# Misleading intermediate analysis (dead computation)
high_elevation_plots = [p for p in plots if p['elevation'] > 200]
degraded_soil_count = len([p for p in plots if p['health'] < 70])

# Key execution point
final_yield = calculate_harvest_efficiency(plots)
print(f"Result: {final_yield}")