def calculate_harvest_efficiency(plots):
    base_yield = 0
    bonus_multiplier = 1.0
    penalty_factor = 0.0
    temp_adjustment = 0
    efficiency_log = []
    total_area = sum([p['area'] for p in plots])

    for plot in plots:
        soil_quality = plot['soil']
        crop_type = plot['crop']
        is_irrigated = plot['irrigated']

        # Core calculation branch
        if soil_quality > 7:
            base_yield += plot['area'] * 12
            if is_irrigated:
                base_yield += plot['area'] * 3
        elif soil_quality > 4:
            base_yield += plot['area'] * 8
            if crop_type in {'wheat', 'corn'}:
                efficiency_log.append('moderate_optimized')
        else:
            penalty_factor += plot['area'] * 0.5

        # Distractor logic: climate sensitivity (not used in final formula)
        climate_zone = plot.get('climate', 'temperate')
        if climate_zone == 'arid':
            temp_adjustment -= 1.5
        elif climate_zone == 'tropical':
            temp_adjustment += 0.8

        # Irrelevant string processing (set operation + string method)
        flags = {'irrigated', 'fenced', 'shaded'}
        status = "irrigated" if is_irrigated else "dry"
        status_flag = status.upper().replace("D", "X")  # Dead computation
        intersection = flags & {'irrigated', 'monitored'}  # Semi-relevant but unused

        # Conditional expression for visual noise
        bonus_multiplier += 0.1 if plot['area'] > 10 and crop_type.startswith('c') else 0

    # Secondary distractor: simulate weather variance (unused)
    forecast = [0.9, 1.1, 1.0, 0.8]
    adjusted_forecast = [f * bonus_multiplier for f in forecast]
    projected_rainfall = sum(adjusted_forecast) / len(adjusted_forecast)

    # Actual answer computation
    final_yield = int((base_yield - penalty_factor) * 0.95)

    # Additional red herring: dictionary accumulation not tied to result
    summary_stats = {
        'total_plots': len(plots),
        'avg_area': total_area / len(plots),
        'temp_adjustment': temp_adjustment,
        'projected_rainfall': projected_rainfall
    }

    return final_yield

# Input data
land_plots = [
    {'area': 12, 'soil': 8, 'crop': 'corn', 'irrigated': True, 'climate': 'temperate'},
    {'area': 8, 'soil': 5, 'crop': 'wheat', 'irrigated': False, 'climate': 'arid'},
    {'area': 15, 'soil': 9, 'crop': 'cotton', 'irrigated': True, 'climate': 'tropical'},
    {'area': 5, 'soil': 3, 'crop': 'barley', 'irrigated': True, 'climate': 'temperate'}
]

final_yield = calculate_harvest_efficiency(land_plots)
print(f"Result: {final_yield}")