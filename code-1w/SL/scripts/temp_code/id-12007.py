def calculate_harvest(plots):
    # Lambda to determine soil quality impact
    soil_factor = lambda quality: 0.8 if quality < 3 else (1.0 if quality < 5 else 1.3)

    base_water = 500
    temp_adjustment = 0
    cumulative_rainfall = 0
    season_multiplier = 1.1  # Default for normal season

    # Simulate intermediate weather calculations (some irrelevant)
    for day in range(7):
        temp = 20 + day % 5
        if temp > 22:
            temp_adjustment += 0.05
        cumulative_rainfall += 12 + day * 2

    # Irrelevant pest tracking (distractor)
    pest_pressure = 0
    for week in range(4):
        if week % 3 == 0:
            pest_pressure += 1

    total_yield = 0.0
    high_quality_count = 0

    for plot in plots:
        size = plot['size']
        soil_q = plot['soil_quality']
        water_avail = base_water + cumulative_rainfall * 0.3

        # Core yield calculation
        base_yield_per_unit = 120
        yield_factor = soil_factor(soil_q)

        adjusted_yield = base_yield_per_unit * yield_factor

        if water_avail > 600:
            adjusted_yield *= 1.1
        elif water_avail < 400:
            adjusted_yield *= 0.9

        harvest = size * adjusted_yield * season_multiplier

        if soil_q >= 5:
            high_quality_count += 1

        total_yield += harvest

    # Final adjustment based on high-quality plot bonus
    if high_quality_count >= 2:
        total_yield *= 1.05

    final_yield = int(total_yield)  # Critical assignment point

    return final_yield

# Input data
plots_data = [
    {'size': 3, 'soil_quality': 2},
    {'size': 4, 'soil_quality': 5},
    {'size': 2, 'soil_quality': 6}
]

# Execution
final_yield = calculate_harvest(plots_data)
print(f"Result: {final_yield}")